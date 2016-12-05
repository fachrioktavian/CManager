#/bin/sh
if [ -z "$1" ]
then
	echo "Please specify active user as parameter"
else
	user=$1
	sudo pip install colorama terminaltables pbkdf2 netifaces python-wifi
	sudo echo "$user ALL=(ALL) NOPASSWD: $(which iwlist)" >> /etc/sudoers
	sudo echo "$user ALL=(ALL) NOPASSWD: $(which wpa_supplicant)" >> /etc/sudoers
	sudo echo "$user ALL=(ALL) NOPASSWD: $(which dhclient)" >> /etc/sudoers
	sudo echo "$user ALL=(ALL) NOPASSWD: $(which pkill)" >> /etc/sudoers
	sudo mkdir /usr/share/dcm
	sudo cp -R * /usr/share/dcm/
	sudo ln -s /usr/share/dcm/dcm.py /bin/dcm
fi
