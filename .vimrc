set nocompatible
syntax on
set backspace=2

set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
autocmd BufWritePre * :%s/\s\+$//e

filetype plugin on
set visualbell
set background=dark
set showmatch
set showcmd
set autowrite
set pastetoggle=<F2>
