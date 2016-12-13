#/bin/sh

iwlistbin=$(which iwlist)
wpabin=$(which wpa_supplicant)
dhclientbin=$(which dhclient)
pkillbin=$(which pkill)

if [ -z "$iwlistbin" ] || [ -z "$wpabin" ] || [ -z "$dhclientbin" ] || [ -z "$pkillbin" ]
then
	echo "One of these program are not founded in your system:"
	echo "	- iwlist"
	echo "	- wpa_supplicant"
	echo "	- dhclient"
	echo "	- pkill"
else
	sudoersiwlist=$(sudo cat /etc/sudoers | grep "ALL ALL=(ALL) NOPASSWD: $iwlistbin")
	sudoerswpa=$(sudo cat /etc/sudoers | grep "ALL ALL=(ALL) NOPASSWD: $wpabin")
	sudoersdhclient=$(sudo cat /etc/sudoers | grep "ALL ALL=(ALL) NOPASSWD: $dhclientbin")
	sudoerspkill=$(sudo cat /etc/sudoers | grep "ALL ALL=(ALL) NOPASSWD: $pkillbin")

	if [[ $sudoersiwlist ]]
	then
		echo "[INSTALL] iwlist has been in sudoers whitelist"
	else
		sudo echo "ALL ALL=(ALL) NOPASSWD: $iwlistbin" >> /etc/sudoers
	fi

	if [[ $sudoerswpa ]]
	then
		echo "[INSTALL] wpa_supplicant has been in sudoers whitelist"
	else
		sudo echo "ALL ALL=(ALL) NOPASSWD: $wpabin" >> /etc/sudoers
	fi

	if [[ $sudoersdhclient ]]
	then
		echo "[INSTALL] dhclient has been in sudoers whitelist"
	else
		sudo echo "ALL ALL=(ALL) NOPASSWD: $dhclientbin" >> /etc/sudoers
	fi

	if [[ $sudoerspkill ]]
	then
		echo "[INSTALL] pkill has been in sudoers whitelist"
	else
		sudo echo "ALL ALL=(ALL) NOPASSWD: $pkillbin" >> /etc/sudoers
	fi
fi
