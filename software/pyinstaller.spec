# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['/script/chameleon_cli_main.py'],
    pathex=['/script'],
    binaries=[
        # Include compiled binaries from the correct location
        ("software/bin/*", "bin/"),
        # Alternative paths depending on your build configuration
        # ("software/bin/Debug/*", "bin/"),
        # ("software/bin/Release/*", "bin/"),
    ],
    datas=[
        # Include any data files if needed
        # ("software/script/data/*", "data/"),
    ],
    hiddenimports=[
        # Add any hidden imports that PyInstaller might miss
        'serial',
        'serial.tools',
        'serial.tools.list_ports',
        # Add other imports from requirements.txt as needed
    ],
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

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='chameleon_cli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None  # Add path to icon file if you have one
)