if status is-interactive
    set fish_greeting ""

    # Aliases
    alias grep "grep --color=auto"
    alias cat "bat --style=plain --paging=never"
    alias ls "exa --group-directories-first"
    alias tree "exa -T"
    alias dotfiles="git --git-dir $HOME/.dotfiles/.git --work-tree $HOME"

    # Prompt
    # starship init fish | source
    set -gx LESS_TERMCAP_mb \e'[1;32m'
    set -gx LESS_TERMCAP_md \e'[1;32m'
    set -gx LESS_TERMCAP_me \e'[0m'
    set -gx LESS_TERMCAP_se \e'[0m'
    set -gx LESS_TERMCAP_so \e'[01;33m'
    set -gx LESS_TERMCAP_ue \e'[0m'
    set -gx LESS_TERMCAP_us \e'[1;4;31m'
    

    # Git
    set -g theme_display_git yes
    set theme_display_git_default_branch yes

    # Theme
    set theme_color_scheme gruvbox
    set -g theme_nerd_fonts yes
end
