# Girv's Dotfiles

My current Arch-i3 configuration. Colours based on [Everforest](https://github.com/sainnhe/everforest) theme for Vim.


## Information

<img src="rice.png" align="right" width="400px">

- **OS:** [Arch Linux](https://archlinux.org)
- **WM:** [i3-gaps (Now merged with i3)](https://github.com/Airblader/i3)
- **Terminal:** [kitty](https://github.com/kovidgoyal/kitty)
- **Bar:** [polybar](https://github.com/polybar/polybar)
- **Shell:** [zsh](https://www.zsh.org/)
- **Compositor:** [picom](https://github.com/yshui/picom)
- **Application Launcher:** [rofi](https://github.com/davatorium/rofi)
- **Notification Deamon:** [dunst](https://github.com/dunst-project/dunst)


## Installation
*TODO: Install script*

### Target Structure
```
~/
├── .config/
│   ├── i3/
│   │   └── config
│   ├── kitty/
│   │   └── kitty.conf
│   ├── nvim/
│   │   └── init.lua
│   │   └── lazy-lock.json 
│   ├── picom/
│   │   └── TODO 
│   ├── polybar/
│   │   ├── config.ini
│   │   └── launch.sh
│   ├── rofi/
│   │   ├── themes
│   │   │   └── squared-everforest.rasi
│   │   └── config.rasi
│   └── zsh/
│       ├── aliases.txt
│   	└── (zsh-syntax-highlighting)
├── .local
│   └── bin
│       └── powermenu
├── .bashrc
└── .zshrc
```

### Programs/Packages Needed 

- feh
- i3
- kitty
- nvim
- picom
- polybar
- rofi
- zsh
    - zsh-syntax-highlighting

### Fonts Needed

- JetBrainsMono Nerd Font
- Iosevka 
- Sarasa Mono