# Security and code signing — LakaPDF

© 2026 Larx Vo · https://vovinhlac.com

## Current state

The installer from v0.3.1-alpha is **unsigned**. It passed automated Windows installation tests, but Windows SmartScreen can block it because the publisher is unrecognized. Passing build tests, a SHA256 checksum or a Defender scan does not guarantee the file is safe. **Do not turn off Windows Defender or bypass SmartScreen merely to install it.**

The regular Windows workflow now generates unsigned test artifacts without publishing them automatically.

## Trusted public releases

To distribute a genuinely publisher-verified Windows installer:

1. Obtain a trusted Authenticode code-signing certificate issued to the legitimate publisher; confirm its subject matches the actual verified developer name.
2. Keep the private signing key in an appropriate secure signing service or hardware-backed certificate store; never commit it.
3. Sign the standalone app EXE **before** creating the installer; then sign the finished installer EXE with RFC3161 timestamp.
4. Validate Authenticode signatures and chain, test installer and uninstaller, run antivirus and dependency checks, and publish an SHA256 checksum.
5. Distribute via GitHub Releases or consider Microsoft Store distribution. SmartScreen reputation is not guaranteed immediately even with valid signing.

## Example verification

Open Windows PowerShell and inspect:
```powershell
Get-AuthenticodeSignature .\LakaPDF_0.3.1_Windows_x64_Setup.exe | Format-List *
Get-FileHash .\LakaPDF_0.3.1_Windows_x64_Setup.exe -Algorithm SHA256
```

Only release after checking the signer and trust chain. A self-signed certificate cannot establish global publisher trust.

## Unfinished

A trusted signing certificate and signed release do not yet exist. The old unsigned GitHub release should not be represented as a trusted installer. This documentation is not a workaround for SmartScreen.
