# LakaPDF — Free desktop PDF editor (Alpha 0.3.1)

**LakaPDF** is a local-first Windows PDF application created by **Larx Vo**.  
**Copyright:** © 2026 Larx Vo — [vovinhlac.com](https://vovinhlac.com) (author information only, not a required online service).

**SECURITY WARNING:** The existing `v0.3.1-alpha` installer is **UNSIGNED** and triggers Windows SmartScreen. It is a legacy testing artifact, **not a trusted public installer**. Please do not disable Defender or bypass SmartScreen. A signed installer is not yet available. See [Secure release policy](docs/SECURE_RELEASE_VI.md).

## Microsoft Store — verified publisher route

**Status: preparing for Partner Center submission, not yet approved or listed in Microsoft Store.**

- [Microsoft Partner Center](https://partner.microsoft.com/dashboard): the real publisher must enroll, verify identity and reserve the LakaPDF app name.
- [MSIX build workflow](.github/workflows/store-msix.yml): generates an **unsigned MSIX submission candidate** from exact Partner Center Package Identity Name and Publisher values.
- [Store submission guide](docs/MICROSOFT_STORE_SUBMISSION.md) · [Privacy policy](docs/PRIVACY_POLICY.md) · [Store description](docs/STORE_LISTING.md)

The unsigned MSIX is for **Partner Center submission**, not for sideload installation by end users. The old v0.3.1-alpha GitHub EXE is unsigned and not a trusted public installer. Do not disable SmartScreen or Defender to use it. Only share a genuine Store install URL **after Microsoft's approval**.

## Install on Windows

1. **Do not install the unsigned alpha.** Wait for a verified signed release. Review [the security policy](docs/SECURE_RELEASE_VI.md).
2. Verify the installer using the published **SHA256.txt** and scan using Microsoft Defender.
3. Run the installer. A Start Menu shortcut and an uninstaller are created; installation is per-user.
4. Start LakaPDF from the Start Menu. **No Python, pip, account, subscription, online server or watermark is required.**

**Security note:** The current alpha EXE is **not code-signed by a trusted publisher**. Windows SmartScreen has blocked this file. Public availability on GitHub, checksum validation and automated testing do not replace code-signing. A valid code-signing certificate is still needed; no trusted installer is currently available.

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
7. Uploads unsigned test artifacts for development only. **Does not publish unsigned installers automatically.** The separate [signed release workflow](.github/workflows/signed-windows-release.yml) requires a trusted certificate, checks Authenticode signatures and runs a Defender scan before publishing.

Developer build prerequisites: Python 3.12 and Inno Setup 6. See `build_offline_windows.bat` and [Vietnamese installation instructions](docs/INSTALL_WINDOWS_VI.md).

## Privacy, free use and licenses

No subscription, forced watermark or mandatory account. PDF files are processed locally. Website vovinhlac.com is only author information.

LakaPDF alpha source is distributed under **AGPL-3.0-only**, see [LICENSE](LICENSE). PyMuPDF/MuPDF is also subject to AGPL or commercial licensing; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). All authorship notices remain in the application, not stamped onto user PDF files.
