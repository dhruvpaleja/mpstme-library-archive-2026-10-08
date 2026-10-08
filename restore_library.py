"""Restore all or selected MPSTME Library folders from the verified private backup.

Requires Python 3.11+ and GitHub CLI signed in to an account with repository access.
  python restore_library.py --list
  python restore_library.py --destination D:/Library_Restore
  python restore_library.py --destination D:/Study --prefix 03_Elective_Comparison/
"""
from pathlib import Path,PurePosixPath
from collections import Counter,defaultdict
import argparse,hashlib,json,os,re,shutil,subprocess,zipfile
REPO='dhruvpaleja/mpstme-library-archive-2026-10-08'
TAG='complete-library-2026-10-08'
def sha(path):
    with path.open('rb') as source:return hashlib.file_digest(source,'sha256').hexdigest()
def gh(*args):
    run=subprocess.run(['gh',*args],capture_output=True,text=True,encoding='utf-8')
    if run.returncode:raise RuntimeError(run.stderr[-800:])
    return json.loads(run.stdout) if run.stdout.lstrip().startswith(('{','[')) else run.stdout.strip()
def safe(root,relative):
    parts=PurePosixPath(relative)
    if parts.is_absolute() or any(x in {'..',''} or ':' in x or '\\' in x for x in parts.parts):raise ValueError('Unsafe backup path')
    result=root.joinpath(*parts.parts)
    if not result.resolve().is_relative_to(root):raise ValueError('Restore path escapes the destination through a link')
    return result
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path)
    parser.add_argument('--destination',type=Path)
    parser.add_argument('--prefix',action='append',default=[])
    parser.add_argument('--path',action='append',default=[],help='Restore an exact relative file path; repeatable')
    parser.add_argument('--list',action='store_true')
    parser.add_argument('--staging',type=Path,help='Optional separate temporary download directory')
    args=parser.parse_args()
    manifest_path=args.manifest or Path(__file__).resolve().with_name('full-library-manifest.json')
    if not args.manifest:
        release=gh('api','repos/'+REPO+'/releases/tags/'+TAG)
        pages=gh('api','--paginate','--slurp',f"repos/{REPO}/releases/{release['id']}/assets?per_page=100")
        asset=next(x for page in pages for x in page if x['name']=='full-library-manifest.json')
        if not manifest_path.exists():
            gh('release','download',TAG,'--repo',REPO,'--pattern',manifest_path.name,'--dir',str(manifest_path.parent))
        if manifest_path.stat().st_size!=asset['size'] or 'sha256:'+sha(manifest_path)!=asset['digest']:raise ValueError('Manifest does not match the verified release; use a fresh copy')
    data=json.loads(manifest_path.read_text(encoding='utf-8'))
    if data.get('schema')!=1 or data.get('status')!='content_verified':raise ValueError('Backup manifest is not complete')
    def selected(path):return not (args.prefix or args.path) or path in args.path or any(path.startswith(p.rstrip('/')+'/') or path==p.rstrip('/') for p in args.prefix)
    files=[x for x in data['files'] if selected(x['path'])]
    if not files:raise ValueError('No files matched that selection')
    if args.list:
        counts=Counter(x['path'].split('/')[0] for x in files)
        for name,count in sorted(counts.items()):print(name,count,'files')
        print('Logical file paths:',len(files),'unique contents:',len({x['sha256'] for x in files}))
        print('Original unavailable portal sources:',data['coverage']['unmatched_file_entries']);return
    if not args.destination:parser.error('--destination is required for restoration')
    root=args.destination.resolve();root.mkdir(parents=True,exist_ok=True)
    stage=(args.staging or root/'98_Cloud_Restore_Temporary').resolve();stage.mkdir(parents=True,exist_ok=True)
    cache=stage/'objects';cache.mkdir(exist_ok=True)
    for relative in data['directories']:
        if not (args.prefix or args.path) or any(relative==p.rstrip('/') or relative.startswith(p.rstrip('/')+'/') for p in args.prefix):safe(root,relative).mkdir(parents=True,exist_ok=True)
    canonical={};restored=[];groups=defaultdict(list);legacy=[]
    for file in files:
        if not re.fullmatch('[0-9a-f]{64}',file['sha256']):raise ValueError('Invalid file checksum')
        target=safe(root,file['path'])
        if target.exists():
            if not target.is_file() or target.stat().st_size!=file['bytes'] or sha(target)!=file['sha256']:raise ValueError('Existing file differs; refusing overwrite: '+str(target))
            canonical[file['sha256']]=target
        if 'legacy_bundle' in file:legacy.append(file)
        else:groups[file['sha256']].append(file)
    references=Counter(ident for digest,rows in groups.items() if digest not in canonical for ident in set(rows[0]['chunks']))
    def aliases(rows,source):
        for row in rows:
            target=safe(root,row['path']);target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():
                if target.stat().st_size!=row['bytes'] or sha(target)!=row['sha256']:raise ValueError('Existing file differs; refusing overwrite: '+str(target))
            elif target!=source:
                try:os.link(source,target)
                except OSError:shutil.copyfile(source,target)
                if target.stat().st_size!=row['bytes'] or sha(target)!=row['sha256']:raise ValueError('Restored alias checksum mismatch')
            restored.append({'path':row['path'],'sha256':row['sha256'],'bytes':row['bytes']})
    for digest,rows in list(groups.items()):
        if digest in canonical:aliases(rows,canonical[digest]);del groups[digest]
    def assemble_ready():
        for digest,rows in list(groups.items()):
            row=rows[0]
            if not all((cache/ident).is_file() for ident in row['chunks']):continue
            target=safe(root,row['path']);target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():
                if sha(target)!=digest:raise ValueError('Existing file differs; refusing overwrite: '+str(target))
            else:
                if shutil.disk_usage(target.parent).free<row['bytes']+2*1024**3:raise RuntimeError('Insufficient destination storage')
                temp=target.with_name('.'+digest[:16]+'.cloud-restoring')
                if temp.exists():raise ValueError('Unexpected restore temporary file')
                h=hashlib.sha256()
                try:
                    with temp.open('xb') as out:
                        for ident in row['chunks']:
                            with (cache/ident).open('rb') as inp:
                                while block:=inp.read(1024*1024):out.write(block);h.update(block)
                    if temp.stat().st_size!=row['bytes'] or h.hexdigest()!=digest:raise ValueError('Reconstructed file checksum mismatch')
                    os.replace(temp,target)
                finally:
                    if temp.exists():temp.unlink()
            canonical[digest]=target;aliases(rows,target);del groups[digest]
            for ident in set(row['chunks']):
                references[ident]-=1
                if references[ident]==0:(cache/ident).unlink()
    assemble_ready()
    def package(bundle,tag):
        name=bundle['name']
        if Path(name).name!=name or '/' in name or '\\' in name:raise ValueError('Unsafe asset name')
        path=stage/name
        if not path.exists():
            if shutil.disk_usage(stage).free<bundle['bytes']+3*1024**3:raise RuntimeError('Insufficient temporary download space')
            print('Downloading',name,flush=True)
            gh('release','download',tag,'--repo',data['repo'],'--pattern',name,'--dir',str(stage))
        if path.stat().st_size!=bundle['bytes'] or sha(path)!=bundle['sha256']:raise ValueError('Bundle checksum mismatch: '+name)
        return path
    for bundle in data['bundles']:
        needed={ident for rows in groups.values() for ident in rows[0]['chunks'] if data['chunks'][ident]['bundle']==bundle['name']}
        if not needed:continue
        path=package(bundle,data['release_tag'])
        with zipfile.ZipFile(path) as archive:
            for ident in needed:
                if not re.fullmatch('[0-9a-f]{64}',ident):raise ValueError('Invalid chunk name')
                output=cache/ident
                if output.exists():
                    if sha(output)!=ident:raise ValueError('Cached chunk checksum mismatch')
                    continue
                with archive.open('objects/'+ident) as inp,output.open('xb') as out:
                    while block:=inp.read(1024*1024):out.write(block)
                if output.stat().st_size!=data['chunks'][ident]['bytes'] or sha(output)!=ident:raise ValueError('Chunk checksum mismatch')
        assemble_ready();path.unlink();print('Restored content from',bundle['name'],flush=True)
    if groups:raise ValueError('Some required chunks were not restored')
    for bundle in data['legacy']['bundles']:
        rows=[x for x in legacy if x['legacy_bundle']==bundle['name']]
        remaining=[]
        for row in rows:
            if row['sha256'] in canonical:aliases([row],canonical[row['sha256']])
            else:remaining.append(row)
        if not remaining:continue
        path=package(bundle,data['legacy']['release_tag'])
        with zipfile.ZipFile(path) as archive:
            for row in remaining:
                target=safe(root,row['path']);target.parent.mkdir(parents=True,exist_ok=True)
                if target.exists():
                    if sha(target)!=row['sha256']:raise ValueError('Existing legacy file differs')
                else:
                    if shutil.disk_usage(target.parent).free<row['bytes']+2*1024**3:raise RuntimeError('Insufficient destination storage')
                    temp=target.with_name('.'+row['sha256'][:16]+'.cloud-restoring')
                    if temp.exists():raise ValueError('Unexpected restore temporary file')
                    try:
                        with archive.open(row['path']) as inp,temp.open('xb') as out:
                            while block:=inp.read(1024*1024):out.write(block)
                        if temp.stat().st_size!=row['bytes'] or sha(temp)!=row['sha256']:raise ValueError('Legacy restored checksum mismatch')
                        os.replace(temp,target)
                    finally:
                        if temp.exists():temp.unlink()
                canonical[row['sha256']]=target;aliases([row],target)
        path.unlink();print('Restored raw packages from',bundle['name'],flush=True)
    if len(restored)!=len(files):raise ValueError('Restored path count does not match selection')
    (root/'CLOUD_RESTORE_RECEIPT.json').write_text(json.dumps({'files':restored,'repo':data['repo'],'release_tag':data['release_tag'],'method':'Downloaded bundles, chunks, reconstructed files and aliases checked with SHA-256'},ensure_ascii=False,indent=2),encoding='utf-8')
    try:cache.rmdir();stage.rmdir()
    except OSError:pass
    print('Restoration verified:',len(restored),'file paths',flush=True)
if __name__=='__main__':main()
