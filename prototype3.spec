# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
import glob, os
rasterio_imports_paths = glob.glob(r"C:\Users\User\Desktop\reduceTIF\venv\Lib\site-packages\rasterio\*.py")
rasterio_imports = ['rasterio.sample']

for item in rasterio_imports_paths:
    current_module_filename = os.path.split(item)[-1]
    current_module_filename = 'rasterio.'+current_module_filename.replace('.py', '')
    rasterio_imports.append(current_module_filename)

a = Analysis(
    ['prototype3.py'],
    pathex=['C:\\Users\\User\\Desktop\\reduceTIF\\venv\\Lib\\site-packages'],
    binaries=[],
    datas=[('data','data')],
    hiddenimports=rasterio_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
splash = Splash(
    'splashscreenn.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    splash,
    splash.binaries,
    [],
    name='prototype3',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
