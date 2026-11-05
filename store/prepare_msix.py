"""Stage a Microsoft Store MSIX package with the exact Partner Center identity.
Unsigned MSIX is for Partner Center submission, NOT sideloading.
© 2026 Larx Vo — vovinhlac.com
"""
import argparse
import pathlib
import re
import shutil
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

def validate(name,publisher,version):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{2,49}",name):
        raise ValueError("Invalid Store package identity name")
    if any(v in name.lower() for v in ("placeholder","replace","example","todo")):
        raise ValueError("Use exact identity from Partner Center, not a placeholder")
    if not publisher.startswith("CN=") or any(v in publisher.lower() for v in ("placeholder","replace","example","cn=larx vo")):
        raise ValueError("Publisher must match the actual Partner Center Publisher field")
    parts=version.split(".")
    if len(parts)!=4 or any(not v.isdigit() or int(v)>65535 for v in parts):
        raise ValueError("Version must have four integer components, each 0..65535")

def manifest(name,publisher,publisher_display,version):
    name,publisher,publisher_display=map(escape,(name,publisher,publisher_display))
    return f'''<?xml version="1.0" encoding="utf-8"?>
<Package xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
         xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10"
         xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities"
         IgnorableNamespaces="uap rescap">
 <Identity Name="{name}" Publisher="{publisher}" Version="{version}" ProcessorArchitecture="x64"/>
 <Properties><DisplayName>LakaPDF</DisplayName><PublisherDisplayName>{publisher_display}</PublisherDisplayName>
 <Description>Free local-first PDF desktop editor</Description><Logo>Assets\\StoreLogo.png</Logo></Properties>
 <Resources><Resource Language="en-us"/></Resources>
 <Dependencies><TargetDeviceFamily Name="Windows.Desktop" MinVersion="10.0.17763.0" MaxVersionTested="10.0.22621.0"/></Dependencies>
 <Applications><Application Id="LakaPDF" Executable="LakaPDF\\LakaPDF.exe" EntryPoint="Windows.FullTrustApplication">
  <uap:VisualElements DisplayName="LakaPDF" Description="Local PDF tools by Larx Vo"
   BackgroundColor="#2764DD" Square150x150Logo="Assets\\Square150x150Logo.png"
   Square44x44Logo="Assets\\Square44x44Logo.png"/>
 </Application></Applications>
 <Capabilities><rescap:Capability Name="runFullTrust"/></Capabilities>
</Package>'''

def icons(out):
    from PIL import Image, ImageDraw
    out.mkdir(parents=True,exist_ok=True)
    for filename,n in (("StoreLogo.png",50),("Square44x44Logo.png",44),
                       ("Square150x150Logo.png",150)):
        scale=4
        s=n*scale
        im=Image.new("RGBA",(s,s),(0,0,0,0))
        d=ImageDraw.Draw(im)
        d.rounded_rectangle((s//14,s//14,s-s//14,s-s//14),radius=s//5,fill="#2764DD")
        d.rounded_rectangle((int(s*.27),int(s*.18),int(s*.72),int(s*.82)),
                            radius=s//25,fill="#FFFFFF")
        d.line([(int(s*.39),int(s*.39)),(int(s*.39),int(s*.66)),
                (int(s*.61),int(s*.66))],fill="#2764DD",width=max(2,s//18))
        im.resize((n,n),Image.Resampling.LANCZOS).save(out/filename)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--dist",required=True,type=pathlib.Path)
    p.add_argument("--stage",required=True,type=pathlib.Path)
    p.add_argument("--identity",required=True)
    p.add_argument("--publisher",required=True)
    p.add_argument("--publisher-display",default="Larx Vo")
    p.add_argument("--version",default="0.3.1.0")
    a=p.parse_args()
    validate(a.identity,a.publisher,a.version)
    if not (a.dist/"LakaPDF.exe").is_file():
        raise ValueError("Missing compiled Windows desktop EXE")
    if a.stage.exists(): shutil.rmtree(a.stage)
    a.stage.mkdir(parents=True)
    shutil.copytree(a.dist,a.stage/"LakaPDF")
    icons(a.stage/"Assets")
    xml=manifest(a.identity,a.publisher,a.publisher_display,a.version)
    ET.fromstring(xml)
    (a.stage/"AppxManifest.xml").write_text(xml,encoding="utf-8")
    print("MSIX layout staged for Partner Center identity:",a.identity)

if __name__=="__main__": main()
