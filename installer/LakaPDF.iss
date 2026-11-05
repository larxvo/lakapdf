#define AppVersion "0.3.1"
[Setup]
AppId={{A5BC6D32-ED07-4843-A164-1D3436F2FD71}
AppName=LakaPDF
AppVersion={#AppVersion}
AppPublisher=Larx Vo
AppPublisherURL=https://vovinhlac.com
DefaultDirName={localappdata}\Programs\LakaPDF
DefaultGroupName=LakaPDF
OutputDir=..\release
OutputBaseFilename=LakaPDF_0.3.1_Windows_x64_Setup
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
UninstallDisplayIcon={app}\LakaPDF.exe
[Files]
Source: "..\dist\LakaPDF\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
[Icons]
Name: "{autoprograms}\LakaPDF"; Filename: "{app}\LakaPDF.exe"
[Run]
Filename: "{app}\LakaPDF.exe"; Description: "Launch LakaPDF"; Flags: nowait postinstall skipifsilent
