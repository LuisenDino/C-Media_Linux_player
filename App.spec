# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['App/App.py'],
             pathex=["/home/luis/.local/lib/python3.7/site-packages/cv2"],
             binaries=[("/home/luis/.local/lib/python3.7/site-packages/cefpython3/libcef.so", ".")],
             datas=[("/home/luis/Escritorio/C-Media_Linux_player/App/Media", "App/Media")],
             hiddenimports=[],
             hookspath=["."],
             hooksconfig={},
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
          [],
          exclude_binaries=True,
          name='C-Media Player Linux v1.0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon="/home/luis/Descargas/C-MediaRecursos/CmediaPlayer.ico"          
          )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='App')
