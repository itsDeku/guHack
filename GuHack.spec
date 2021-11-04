# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Game/eel/GuHack.py'],
             pathex=['C:\\Game\\eel'],
             binaries=[],
             datas=[('C:/Game/eel/data', 'data/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='GuHack',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Game\\eel\\galgotias.ico')
