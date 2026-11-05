# LakaPDF — Free desktop PDF editor (Alpha 0.3.1)

**LakaPDF** is a local-first Windows PDF application created by **Larx Vo**.  
**Copyright:** © 2026 Larx Vo — [vovinhlac.com](https://vovinhlac.com) (author information only, not a required online service).

[**Download Windows installer (GitHub Releases)**](https://github.com/larxvo/lakapdf/releases/tag/v0.3.1-alpha)

## Install on Windows

1. Download **LakaPDF_0.3.1_Windows_x64_Setup.exe** from [Releases](https://github.com/larxvo/lakapdf/releases).
2. Verify the installer using the published **SHA256.txt** and scan using Microsoft Defender.
3. Run the installer. A Start Menu shortcut and an uninstaller are created; installation is per-user.
4. Start LakaPDF from the Start Menu. **No Python, pip, account, subscription, online server or watermark is required.**

**Security note:** The alpha EXE is **not code-signed by a trusted publisher**. Windows SmartScreen may warn about an unrecognized app. Publishing on GitHub does **not** automatically remove that warning. Do not turn off Windows protection to force installation. Public distribution with a publisher-verified experience requires a trusted code-signing certificate.

## Working alpha features

- Open and render PDF files, navigate pages, zoom, select PDF text, search words and inspect fonts
- Highlight text, add simple Latin text, reconstruct selected text region using a user-selected Unicode font
- Rotate and delete pages, merge and split PDFs, export PNG
- Insert a **visual signature image** (not a cryptographic PDF digital signature)
- Save PDF, Save As, basic snapshot undo

LakaPDF saves a real PDF. A save test reopens the document and validates basic PDF structure.

## What is not yet implemented

This is **alpha software**, not yet a complete Acrobat alternative:

- Direct modification of original PDF text operators (current replacement erases and reconstructs a text region)
- OCR, advanced font matching, vector object editing, PDF/A and PDF/X
- True digital certificate signatures
- Guaranteed visual/editing compatibility with all Canva, Adobe Acrobat and PdfCraft-generated PDFs
- Fully optimized handling of huge PDFs (there is no artificial MB limit, but RAM/CPU/disk constraints apply)

**Always edit a copy of important documents.**

## Development and Windows release

Source code is in `lakapdf_alpha/`; PDF tests are in `tests/`.

The [Windows build workflow](.github/workflows/windows-release.yml) runs on a Windows GitHub-hosted machine and:

1. Installs build dependencies
2. Tests PDF functionality
3. Creates a **standalone EXE** using PyInstaller
4. Runs packaged EXE smoke tests
5. Produces an offline Windows installer with Inno Setup
6. Runs a silent install / installed-app test / uninstall smoke test
7. Publishes the installer and its checksum to public GitHub Releases

Developer build prerequisites: Python 3.12 and Inno Setup 6. See `build_offline_windows.bat` and [Vietnamese installation instructions](docs/INSTALL_WINDOWS_VI.md).

## Privacy, free use and licenses

No subscription, forced watermark or mandatory account. PDF files are processed locally. Website vovinhlac.com is only author information.

LakaPDF alpha source is distributed under **AGPL-3.0-only**, see [LICENSE](LICENSE). PyMuPDF/MuPDF is also subject to AGPL or commercial licensing; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). All authorship notices remain in the application, not stamped onto user PDF files.
