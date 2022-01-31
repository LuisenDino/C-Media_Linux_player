sudo cp C-Media_Player_config.desktop C-Media_Player.desktop /usr/share/applications
sudo cp C-Media_Player_config.desktop C-Media_Player.desktop "$HOME/Escritorio" || sudo cp C-Media_Player_config.desktop C-Media_Player.desktop "$HOME/Desktop"
sudo chown $USER:dialout "$HOME/Escritorio/C-Media_Player_config.desktop" 
sudo chown $USER:dialout "$HOME/Escritorio/C-Media_Player.desktop" 
sudo chmod 775 "$HOME/Escritorio/C-Media_Player_config.desktop" 
sudo chmod 775 "$HOME/Escritorio/C-Media_Player.desktop" 
sudo cp -r CMedia_Player /usr/share/C-Media_Player
sudo cp C-Media_Player /usr/bin
sudo cp logo/CmediaPlayer.png /usr/share/pixmaps/CmediaPlayer.png
sudo cp 50-CMediaPlayer.rules /lib/udev/rules.d/50-CMediaPlayer.rules

sudo udevadm control --reload
sudo udevadm trigger

CMEDIA_PATH="$HOME/.config/Ciel/C-Media_Player"
mkdir -p "$CMEDIA_PATH/configs"

sudo cp config.json "$CMEDIA_PATH/configs/config.json"
sudo chown $USER:dialout "$CMEDIA_PATH/configs/config.json" 
sudo cp -r Media "$CMEDIA_PATH"

sudo adduser $USER dialout 

echo "La aplicacion se ha instalado"