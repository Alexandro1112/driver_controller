/usr/bin/sh
$ response=' '

GREEN='\033[0;32m'
YELLOW='\033[0;33m'

plt=$(uname)
if [[ "$plt" == 'Linux' ]]; then
    $ response='Your Platform:Ubuntu(Linux): Wait installation..'
    cd ~
    # ܿܿܿܿܿܿܿܿܿܿܿܿܿܿܿܿReplace '~' to working path to directory
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install ffmpeg
    brew install blueutil
    brew install brightness
    brew install terminal-notifier && echo -e "${GREEN} Successful!"
elif [[ "$plt" == 'Darwin' ]]; then
    $ responses= 'Your Platform:Mac-os: Wait installation..'
    cd /Users/admin/PycharmProjects/~
    # ܿܿܿܿܿܿܿܿܿܿܿܿܿܿܿܿReplace '~' to working path to directory
    brew install ffmpeg
    brew install blueutil
    brew install brightness
    brew install terminal-notifier && echo -e "${GREEN} Successful!"


else
    echo "${YELLOW} For windows no dependencies. Run Code."
    exit 1;
 fi
