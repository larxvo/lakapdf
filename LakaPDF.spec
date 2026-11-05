a=Analysis(['lakapdf_alpha/app.py'],pathex=['lakapdf_alpha'],binaries=[],datas=[],hiddenimports=['fitz','pymupdf','native_engine'],hookspath=[],hooksconfig={},runtime_hooks=[],excludes=[],noarchive=False)
pyz=PYZ(a.pure)
exe=EXE(pyz,a.scripts,[],exclude_binaries=True,name='LakaPDF',debug=False,strip=False,upx=False,console=False)
coll=COLLECT(exe,a.binaries,a.datas,strip=False,upx=False,name='LakaPDF')
