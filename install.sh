#/bin/sh
$iwlistbin=$(which iwlist)
$wpabin=$(which wpa_supplicant)
$dhclientbin=$(which dhclient)
$pkillbin=$(which pkill)
if [ -z "$iwlistbin" ] || [ -z "$wpabin" ] || [ -z "$dhclientbin" ] || [ -z "$pkillbin" ]
then
	echo "One of these program are not founded in your system:"
	echo "	- iwlist"
	echo "	- wpa_supplicant"
	echo "	- dhclient"
	echo "	- pkill"
else
	user=$1
	sudo pip install colorama terminaltables pbkdf2 netifaces python-wifi
	sudo echo "ALL ALL=(ALL) NOPASSWD: $(which iwlist)" >> /etc/sudoers
	sudo echo "ALL ALL=(ALL) NOPASSWD: $(which wpa_supplicant)" >> /etc/sudoers
	sudo echo "ALL ALL=(ALL) NOPASSWD: $(which dhclient)" >> /etc/sudoers
	sudo echo "ALL ALL=(ALL) NOPASSWD: $(which pkill)" >> /etc/sudoers
	sudo mkdir /usr/share/dcm
	sudo cp -R * /usr/share/dcm/
	sudo ln -s /usr/share/dcm/dcm.py /bin/dcm
fi
