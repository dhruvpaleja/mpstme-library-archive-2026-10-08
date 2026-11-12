# MPSTME Library — private cloud archive

Cloud backup verified. Local cleanup: **complete**; 40,788 inventoried file paths removed.

Snapshot: **8 October 2026**. **41,166 logical file paths** and **13,198 directory paths** are recorded with their original hierarchy. This includes raw folder ZIPs, organized papers, syllabi, audit records and duplicate logical paths. These totals are not unique portal document counts.

The portal listed **30,804 unique file IDs**: **30,152 accounted for**, **652 unavailable** after repeated empty responses. The unavailable list is preserved in the archive. This is a complete backup of the saved collection, not a claim that the portal supplied all 30,804 documents. Some original PDFs were malformed; their bytes and source-quality reports were preserved.

## PYQs by subject

All 25,064 question-paper files are sorted into **1,126 subjects** in [`subjects/`](subjects/README.md): one folder per subject, each with a README listing every paper by year, exam, semester and programme. Spelling variants of the same subject are merged (for example `APPLIED MATHEMATICES II` and `Applied Mathematics II`), and papers the portal filed in the wrong folder are moved to the subject named in the file.

Download one or more subjects, already sorted into `PYQs_By_Subject/<Subject>/<Academic year>/`:

```powershell
gh repo clone dhruvpaleja/mpstme-library-archive-2026-10-08
cd mpstme-library-archive-2026-10-08
python organize_by_subject.py list --search "operating"
python organize_by_subject.py restore --destination D:/Study --subject "Operating Systems"
```

If you have already restored the full library, `python organize_by_subject.py link --library D:/MPSTME_Library_Restored` builds the whole subject tree with hard links (no extra space on NTFS). Identical copies of a paper are placed once. To correct a subject, edit `subject_aliases.json` and run `python organize_by_subject.py catalog`.

## Question text for reading and AI analysis

Every question paper has also been read into text (PDF text layer where present, OCR for scanned papers) and split into questions with marks, year, exam, semester and department:

- `subjects/<Subject>/papers.md`: every paper of the subject in full, newest first.
- `subjects/<Subject>/questions.jsonl`: one record per question or sub-question, with marks and CO/BL tags.
- `subjects/<Subject>/papers.jsonl` and `answer_keys.md`: paper details, and answer keys where published.
- [`departments/`](departments/README.md): subjects grouped by branch (Computer, IT, EXTC, Mechanical, Civil, ...).
- [`question_bank/README.md`](question_bank/README.md): field definitions, coverage and accuracy notes.

`build_question_bank.py` regenerates all of this; see its header for the OCR requirements.

## Download and restore

You must be signed in to GitHub with access to this private repository. Install Python 3.11+ and GitHub CLI, then run `gh auth login` if needed.

```powershell
gh release download complete-library-2026-10-08 --repo dhruvpaleja/mpstme-library-archive-2026-10-08 --pattern restore_library.py
python restore_library.py --list
python restore_library.py --destination D:/Study --prefix 01_Current_Electives_2026-27/
python restore_library.py --destination D:/Study --prefix 03_Elective_Comparison/
```

Choose another writable destination if D: is unavailable. Repeat `--prefix` for several folders, or use `--path` with an exact relative file name. `--list` fetches and verifies the manifest and shows folder counts. Partial restoration downloads only bundles needed for the selection. A bundle may contain other files' chunks, so transferred bytes can exceed the selected file size.

For a full restoration to a drive with ample free space:

```powershell
python restore_library.py --destination D:/MPSTME_Library_Restored
```

Allow at least **85 GiB** of free space for a full restore; use an NTFS destination so duplicate logical files can share hard links. Other filesystems may need more. Temporary bundles/chunks need additional room while a file is reconstructed. An optional `--staging E:/RestoreTemporary` can place downloads on a different drive.

The helper verifies every downloaded bundle, content chunk and reconstructed file with SHA-256. It refuses to overwrite differing files and preserves empty folders. Re-running reuses files that already match. Original machine-specific absolute paths inside historical audit reports remain historical; the restored folder hierarchy and relative catalog links are preserved.

## Keep both releases

- [Complete collection](https://github.com/dhruvpaleja/mpstme-library-archive-2026-10-08/releases/tag/complete-library-2026-10-08): 127 content bundles, portable manifest, restore helper and verification evidence.
- [Earlier raw archive bundles](https://github.com/dhruvpaleja/mpstme-library-archive-2026-10-08/releases/tag/raw-archives-2026-10-08): 16 bundles referenced by the same manifest.

Do not delete either release: the full collection depends on both. New bundles store files as deduplicated SHA-256 chunks; use the restore helper to recover their original names and folders. The older `restore_raw_archives.py` restores only the earlier raw subset.

## Organization

| Original top-level path | File paths |
| --- | ---: |
| `00_Original_Downloads` | 573 |
| `00_Original_Downloads_Local` | 10 |
| `01_Current_Electives_2026-27` | 6 |
| `02_Question_Papers` | 25,064 |
| `03_Elective_Comparison` | 306 |
| `04_Syllabi_Archive` | 4,525 |
| `05_Library_Resources` | 24 |
| `06_Root_Files` | 1 |
| `97_Unverified_Portal_Responses` | 35 |
| `99_Indexes` | 10,616 |
| `Archive_Status.html` | 1 |
| `Archive_Status.md` | 1 |
| `README.md` | 1 |
| `START_HERE.html` | 1 |
| `bulk_manifest.json` | 1 |
| `download_manifest.json` | 1 |

The elective comparison recommends **HCI + Blockchain**, with Cloud as the next option, based on the supplied syllabi and inspected past papers. It does not guarantee a pass from 2–3 days of preparation. Restore `03_Elective_Comparison/` for the reasoning and study material.

## Verification

All new content ZIPs were CRC checked before upload; GitHub's server SHA-256 digest, byte size and uploaded state matched for every new and earlier bundle. Fresh network restoration was tested for current syllabi, an identical-content alias, a split large file and an earlier raw ZIP. Reconstruction, shared chunks, empty files/folders, repeat restoration, changed-file refusal and path traversal refusal were also tested. A complete fresh restoration of the entire collection was not performed.

See `cloud-verification.json` in the complete release for the final audit. After local cleanup, `local-cleanup-summary.json` records the measured C: and D: space change. Space figures reflect the device state when measured; other applications can change free space concurrently.
