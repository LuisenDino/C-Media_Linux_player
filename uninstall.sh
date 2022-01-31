sudo rm /usr/share/applications/C-Media_Player_config.desktop 
sudo rm /usr/share/applications/C-Media_Player.desktop 
sudo rm "$HOME/Escritorio/C-Media_Player_config.desktop" ||sudo rm "$HOME/Desktop/C-Media_Player_config.desktop" 
sudo rm "$HOME/Escritorio/C-Media_Player.desktop" || sudo rm "$HOME/Desktop/C-Media_Player.desktop"
sudo rm -r /usr/share/C-Media_Player
sudo rm /usr/bin/C-Media_Player 
sudo rm /usr/share/pixmaps/CmediaPlayer.png
sudo rm /lib/udev/rules.d/50-CMediaPlayer.rules

sudo udevadm control --reload
sudo udevadm trigger

CMEDIA_PATH="$HOME/.config/Ciel/"
sudo rm -r $CMEDIA_PATH

sudo gpasswd -d $USER dialout

echo "La aplicacion se ha desinstalado"