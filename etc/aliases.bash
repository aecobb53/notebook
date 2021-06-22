################
# BASIC SYSTEM #
################

alias q='exit'
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias ~='cd ~'
alias ..='cd ..'
alias lsr='ls -lrth'
alias lsa='ls -larth'
#alias lsd='ls -larthd'
alias ssh='ssh -X '
alias be='sudo su -'

###################
# ADVANCED SYSTEM #
###################

alias revert='bash'
alias sauce='source ~/.zshrc'
alias vial='vi $NOTEBOOK/etc/aliases.zsh'
alias cdg='cd $GITDIR'
alias grep='grep --color=auto'
alias ggrep='grep -G'
alias rgrep='grep -R'
alias grgrep='grep -GR'
alias grigrep='grep -GRi'
alias less='less -R'
alias psme='ps -ejf | grep "^$USER" | grep -v grep'
alias py='$PYPATH'
alias grepal='grep $NOTEBOOK/etc/aliases.zsh -e '

