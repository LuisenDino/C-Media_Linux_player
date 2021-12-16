from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {
    'packages': ["App"], 
    'excludes': [],
    'include_files': ["App/Media"]
    }

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('App/App.py', base=base, target_name = 'C-Media')
]

setup(name='C-Media Player Linux',
      version = '1.0',
      description = 'None',
      options = {'build_exe': build_options},
      executables = executables)
