import PyInstaller.__main__

PyInstaller.__main__.run([
    'bfm/__main__.py',
    '--name', 'bfm',
    '--onedir',
    '--windowed',
    '--clean',
    '--specpath', "build/spec",
    '--distpath', "build/dist",
    '--workpath', "build/temp",
    '--contents-directory', "resources",
])
    