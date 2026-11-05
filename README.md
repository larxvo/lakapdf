# LakaPDF — Free Local PDF Editor (Alpha 0.3.1)

**LakaPDF** is a free, local-first Windows PDF desktop app developed by **Larx Vo**.  
**Author:** [vovinhlac.com](https://vovinhlac.com) (author information only; the app runs on your PC).

> **Alpha software:** LakaPDF is still under development. Do not use it as the only copy of an important document. Text replacement currently reconstructs PDF regions; it is not full native text-operator editing. PDF/A, OCR, PAdES digital signing and accurate round-trip for all Adobe/Canva/PdfCraft PDFs are not yet implemented.

## Windows download and installation

Visit **[Releases](https://github.com/larxvo/lakapdf/releases)** and look for **LakaPDF_0.3.1_Windows_x64_Setup.exe** after the Windows build is successful. Download it and run the installer. It installs per user, provides a Start Menu shortcut, and includes an uninstaller. **No Python installation, account, or network access is required on the end-user's machine** once the offline installer is available.

**Security:** The initial alpha installer is **unsigned**; Windows SmartScreen may flag an unknown publisher. Do not disable Defender. Releases should be code-signed before broad distribution. GitHub hosting alone does not eliminate SmartScreen warnings.

## Feature scope

- View PDF pages, zoom, thumbnails, search, metadata, font inspector
- Organize pages, split/merge/extract, save as PDF, export image/text
- Annotations, redaction, visual signature, watermark
- Unicode text **reconstruction in a selected region** (not in-place editing)
- Inspect vector/image/text objects, replace a shared image XObject, add vector shapes
- Basic document templates and basic undo snapshots

## Source, building and testing

The full Python source and required notices are included in the repository. GitHub Actions on a hosted Windows runner builds the **standalone application and an Inno Setup offline installer**, runs engine tests and packaged EXE smoke tests, and publishes a GitHub pre-release only on successful packaging.

For source build on Windows: Python 3.12, `pip install -r requirements-build.txt`, then `build_offline_windows.bat`. The end-user installer does not require this toolchain.

See [Windows installation & troubleshooting](docs/INSTALL_WINDOWS_VI.md) and [Technical limitations](docs/LIMITATIONS.md).

## Privacy & licensing

No mandatory account, subscription or imposed document watermark. Files are processed locally. No hard-coded artificial PDF-size cap; the current alpha remains limited by memory/CPU/disk and can be slow on large documents.

**© 2026 Larx Vo**. LakaPDF alpha source is distributed under **AGPL-3.0-only** (see `LICENSE` and `THIRD_PARTY_NOTICES.md`); PyMuPDF/MuPDF licensing must be respected. Copyright credits appear in the software, not in the user's PDFs.
