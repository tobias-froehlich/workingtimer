# workingtimer
Tracks when the screen is not locked and allows to sum working hours

Install the gnome-screensaver:
sudo apt-get install gnome-screensaver

Put this into the file ~/.config/autostart/timer.desktop :

[Desktop Entry]
Type=Application
Name=Timer
Exec=python3 /home/.../timer.py
Icon=system-run
X-GNOME-Autostart-enabled=true

Generate a settings file:
python3 generateEmptySettings.py

Configure the file settings.json that was generated.

