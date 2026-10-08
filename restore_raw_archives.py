"""Restore private GitHub raw-archive bundles. Requires Python 3.11+ and signed-in gh CLI.

Examples:
  python restore_raw_archives.py --list
  python restore_raw_archives.py --destination D:/Library_Restore
  python restore_raw_archives.py --bundle library-raw-2024-2025-001.zip
"""
from pathlib import Path,PurePosixPath
import argparse,json,hashlib,zipfile,subprocess,shutil,os

def sha(path):
    with path.open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,default=Path(__file__).with_name('cloud_backup_manifest.json'))
    parser.add_argument('--destination',type=Path,default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--bundle',help='Restore only this exact asset filename')
    parser.add_argument('--list',action='store_true')
    args=parser.parse_args()
    manifest=json.loads(args.manifest.read_text(encoding='utf-8'))
    bundles=[x for x in manifest['bundles'] if not args.bundle or x['name']==args.bundle]
    if not bundles:raise SystemExit('No matching bundle in manifest')
    if args.list:
        for item in bundles:print(item['name'],round(item['bytes']/2**20),'MiB',len(item['files']),'original packages')
        return
    if not shutil.which('gh'):raise SystemExit('Install GitHub CLI and sign in to the account with access to this private repository.')
    root=args.destination.resolve();root.mkdir(parents=True,exist_ok=True)
    allowed=[root]
    local_storage=root/'99_Indexes/storage_locations.json'
    if local_storage.exists():
        for row in json.loads(local_storage.read_text(encoding='utf-8-sig')):
            accessible=Path(row['accessible_path'])
            if accessible.exists() and accessible.resolve()==Path(row['physical_path']).resolve():allowed.append(accessible.resolve())
    staging=root/'98_Cloud_Restore';staging.mkdir(exist_ok=True)
    for item in bundles:
        package=staging/item['name']
        if package.name!=item['name'] or '/' in item['name'] or '\\' in item['name']:raise ValueError('Unsafe bundle filename')
        if not package.exists():
            if shutil.disk_usage(staging).free<item['bytes']+3*1024**3:raise RuntimeError('Insufficient free space for bundle download and reserve')
            subprocess.run(['gh','release','download',manifest['release_tag'],'--repo',manifest['repo'],'--pattern',item['name'],'--dir',str(staging)],check=True)
        if package.stat().st_size!=item['bytes'] or sha(package)!=item['sha256']:raise ValueError('Downloaded bundle checksum does not match manifest')
        expected={x['relative_path']:x for x in item['files']}
        with zipfile.ZipFile(package) as archive:
            if {x.filename for x in archive.infolist() if not x.is_dir()}!=set(expected):raise ValueError('Bundle member inventory mismatch')
            for relative,row in expected.items():
                components=PurePosixPath(relative)
                if components.is_absolute() or any(x in ['..',''] or ':' in x for x in components.parts):raise ValueError('Unsafe relative path')
                target=root.joinpath(*components.parts);target.parent.mkdir(parents=True,exist_ok=True)
                if not any(target.resolve().is_relative_to(base) for base in allowed):raise ValueError('Restore path escapes destination')
                if target.exists():
                    if sha(target)==row['sha256']:continue
                    raise ValueError('Existing file differs; refusing to overwrite '+str(target))
                if shutil.disk_usage(target.parent).free<row['bytes']+3*1024**3:raise RuntimeError('Insufficient destination storage')
                temporary=target.with_name(target.name+'.cloudrestoring');digest=hashlib.sha256()
                try:
                    with archive.open(relative) as source,temporary.open('wb') as output:
                        while block:=source.read(1024*1024):output.write(block);digest.update(block)
                    if temporary.stat().st_size!=row['bytes'] or digest.hexdigest()!=row['sha256']:raise ValueError('Restored member checksum mismatch')
                    os.replace(temporary,target)
                finally:
                    if temporary.exists():temporary.unlink()
        package.unlink()
        print('Restored and SHA-256 verified',item['name'])

if __name__=='__main__':main()
