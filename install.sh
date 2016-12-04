#/bin/sh
user=$1
sudo pip install colorama terminaltables pbkdf2
sudo echo "$user ALL=(ALL) NOPASSWD: $(which iwlist)" >> /etc/sudoers
sudo echo "$user ALL=(ALL) NOPASSWD: $(which wpa_supplicant)" >> /etc/sudoers
sudo echo "$user ALL=(ALL) NOPASSWD: $(which dhclient)" >> /etc/sudoers
sudo echo "$user ALL=(ALL) NOPASSWD: $(which pkill)" >> /etc/sudoers
sudo ln -s $(pwd)/dcm.py /bin/dcm
