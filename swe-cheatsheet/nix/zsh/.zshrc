eval "$(pyenv init -)"

[[ -r "/usr/local/etc/profile.d/bash_completion.sh" ]] && . "/usr/local/etc/profile.d/bash_completion.sh"


#############

# Find and set branch name var if in git repository.
function git_branch_name()
{
  branch=$(git symbolic-ref HEAD 2> /dev/null | awk 'BEGIN{FS="/"} {print $NF}')
  if [[ $branch == "" ]];
  then
    :
  else
    echo '('$branch')'
  fi
}

# Enable substitution in the prompt.
setopt prompt_subst

# Config for prompt. PS1 synonym.
NEWLINE=$'\n'
prompt='${PWD/#$HOME/~} $(git_branch_name) ${NEWLINE}> '

export PS2="> "

###############


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
alias pip="pip3"
alias python="python3"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/home/bin/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/home/bin/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/home/bin/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/home/bin/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

