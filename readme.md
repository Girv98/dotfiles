# Girv's Dotfiles

My current (work in progress) Arch-i3 configuration. Colours based on [Everforest](https://github.com/sainnhe/everforest) theme for Vim.


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
│   ├── dunst/
│   │   └── dunstrc
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
├── .xinitrc
└── .zshrc
```

### Programs/Packages Needed 

- Dunst
- Feh
- i3
- Kitty
- Network Manager
- Nvim
- Picom
- Polybar
- Rofi
- Zsh
    - zsh-syntax-highlighting

### Fonts Needed

- JetBrainsMono Nerd Font
- Iosevka
- Sarasa Mono (for CJK)