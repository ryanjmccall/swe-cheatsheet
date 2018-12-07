eval "$(pyenv init -)"

[ -f /usr/local/etc/bash_completion ] && . /usr/local/etc/bash_completion

# Prompt
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\nin \w \$(parse_git_branch)\n> "
export PS2="> "

# Python
#export PIP_DISABLE_PIP_VERSION_CHECK=1

# Java Path
export CLASSPATH=.:/usr/local/bin


export ARCHFLAGS="-arch x86_64"
export ICLOUD_DIR="/Users/home/Library/Mobile Documents/com~apple~CloudDocs"

# shortcuts
alias lsd="ls -lrt -d -1 $PWD/{*,.*}"

alias pycharm="open /Applications/PyCharm\ CE.app/"
alias pull_nta="pushd $HOME/nta && find . -mindepth 1 -maxdepth 1 -type d -print -exec git -C {} pull \; && popd"
alias jnb="jupyter notebook"
