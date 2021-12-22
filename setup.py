from cx_Freeze import setup, Executable
from distutils.sysconfig import get_python_lib
from glob import glob
from os.path import join

# Dependencies are automatically detected, but it might need
# fine tuning.
cefPath = join(get_python_lib(), "cefpython3")
CEF_INCLUDES = glob(join(cefPath, "*"))
CEF_INCLUDES.remove(join(cefPath, "examples"))

build_options = {
    'packages': ["cefpython3","tkinter", "App"], 
    'excludes': [],
    'include_files': ["App/Media/"]+CEF_INCLUDES,
    'includes':["tkinter", "cefpython3"]
    }

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [Executable('App/App.py',base=base, 
    target_name = 'C-Media Player Linux v1.0', 
    icon="/home/luis/Escritorio/C-Media_Linux_player/App/Media/CmediaPlayer.ico",
    shortcutName="C-Media Player Linux v1.0",
    shortcutDir="C-MediaPlayerLinuxv1.0"
    )]


setup(name='C-Media Player Linux',
      version = '1.0',
      description = 'None',
      options = {'build_exe': build_options},
      executables = executables)
