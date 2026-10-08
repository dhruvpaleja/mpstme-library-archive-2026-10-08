# MPSTME Library archive — 8 October 2026

Private storage backup for completed raw Library folder downloads. **368 original packages (7.62 GiB) are preserved in 16 verified release bundles.**

[Download the raw archive bundles](https://github.com/dhruvpaleja/mpstme-library-archive-2026-10-08/releases/tag/raw-archives-2026-10-08). These release assets are required for the cloud part of the archive; GitHub's automatic “Source code” ZIP does not include them.

The organized question papers, supplied elective syllabi, comparison and searchable catalog remain in the local `MPSTME_Library` folder. Local storage uses C: and D:. This repository holds selected original raw packages, their complete relative paths and restore evidence.

## Restore

1. Download `restore_raw_archives.py` and `cloud_backup_manifest.json` from this repository into the same folder.
2. Install Python 3.11+ and GitHub CLI, then sign in with the account that has access to this private repository.
3. List bundles: `python restore_raw_archives.py --list`.
4. Restore to a folder with enough free space: `python restore_raw_archives.py --destination D:/Library_Restore`.
5. To restore one bundle, add `--bundle library-raw-2024-2025-001.zip`.

The script checks every bundle's SHA-256 and every restored original package's SHA-256. It preserves the original relative hierarchy and refuses to overwrite a differing existing file. Allow space for one downloaded bundle, its extracted original packages and a 3 GiB reserve. Restoring the entire backup requires at least the total original-package size in addition to temporary space.

Each asset was CRC checked locally, and GitHub's server SHA-256 digest and size were matched before corresponding local raw packages were reclaimed. A restore from a cached, verified bundle was tested and independently rehashed; see `audit/cloud_restore_verification.json`.

## Library coverage

The completed portal census contained **30,804 file IDs across 10,141 folder routes**. The latest reconciliation accounts for **30,152 file IDs**, with **652 unresolved**. Audit status: `source_files_unresolved`. A verified cloud backup does not mean an unavailable portal source file was recovered. See `audit/unresolved_source_files.csv` for the exceptions.

Historical papers and the six supplied syllabi favor HCI + Blockchain for the requested short TEE preparation criterion; the detailed comparison stays in the local archive. Course codes changed and the current syllabi still require ICA/practical work.

Authentication links, cookies and credentials are excluded. Keep this repository private.
