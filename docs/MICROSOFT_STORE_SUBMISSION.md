# LakaPDF — Microsoft Store submission guide

© 2026 Larx Vo · https://vovinhlac.com

## Actual status
The repository provides a Windows workflow to build an **unsigned MSIX Store submission candidate**. It has not been submitted to, approved by, or published on Microsoft Store. The current unsigned GitHub alpha installer is not a trusted public installer.

## Required steps for the account holder
1. Visit https://partner.microsoft.com/dashboard and create or use a legitimate Partner Center developer account. Complete any necessary publisher identity verification. Microsoft determines available enrollment paths and fees.
2. Reserve **LakaPDF** as an app name (if available). Find its assigned Package Identity Name and exact Package Identity Publisher string in the app's Product identity details. The display name is NOT the package publisher identity.
3. Open https://github.com/larxvo/lakapdf/actions/workflows/store-msix.yml and choose **Run workflow**.
4. Paste the exact values from Partner Center into Package Identity, Publisher (X.500 Distinguished Name), Publisher display and a four-number package version. No credentials or identity documents should be posted in GitHub issues.
5. When the build is successful, download the MSIX **artifact**, not the legacy unsigned EXE. This package is specifically for submission, not for sideloading.
6. In Partner Center select the supported packaged desktop app submission path. Confirm your app type supports the generated full-trust MSIX, then upload the package and complete Store listing details, privacy policy, screenshots, market availability, and content declarations.
7. Submit for Microsoft certification. Only provide a Microsoft Store download link after approval and publication.

## What GitHub Actions does
- Builds the local-first Python application and bundles the runtime.
- Runs PDF engine and packaging metadata tests.
- Prepares a Store manifest using real Partner Center identifiers, plus placeholder design assets that must be reviewed before submission.
- Uses the Windows SDK MakeAppx tool to package and unpack the MSIX, verifying the structure.
- Uploads an **unsigned** .msix file and SHA256 only as a workflow artifact, never auto-publishes it as a Store listing.

## Technical prerequisites and limitations
- The app is a packaged full-trust Windows desktop application.
- Microsoft may require additional verification or package changes; successful MSIX packing is not equivalent to Store certification.
- Our current app is Alpha 0.3.1; it lacks native editing of PDF text operators, OCR, digital certificate signatures and guaranteed compatibility with all Adobe/Canva/PdfCraft documents.
- Real Windows screenshots and official app branding must be submitted; do not substitute generated mockups as screenshot evidence.
- Ensure third-party licensing and AGPL source distribution requirements are met before final submission.

## Do not bypass Windows security
Do not tell people to disable Defender or click Run anyway on the unsigned legacy EXE. A Microsoft Store listing with a verified publisher is preferable, but approval is subject to Microsoft's review.
