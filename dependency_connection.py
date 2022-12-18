import subprocess
import sys

if sys.platform == 'darwin' or sys.platform == 'linux':
    lib = (
     '/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"',
     'brew doctor',
     'brew install blueutil',
     'brew install brightness'
    )
    for j in lib:
        subprocess.getoutput(j)
else:    
    pass
