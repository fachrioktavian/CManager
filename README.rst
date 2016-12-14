DCM or Connection Manager
============================

.. image:: https://img.shields.io/pypi/v/cmanager.svg?style=flat-square&label=version
   :target: https://pypi.python.org/pypi/cmanager

.. image:: https://img.shields.io/badge/license-GNUGPLv3-blue.svg?style=flat-square
   :target: https://raw.githubusercontent.com/fachrioktavian/DracOS-Connection-Manager/master/LICENSE.txt

.. image:: https://img.shields.io/pypi/pyversions/cmanager.svg?style=flat-square
   :target: https://github.com/fachrioktavian/DracOS-Connection-Manager

.. image:: https://img.shields.io/pypi/dm/cmanager.svg?style=flat-square
   :target: https://pypi.python.org/pypi/cmanager

**DracOS Connection Manager** is a CLI (Command Line Interface) based program written in Python.
This program help DracOS Linux's users to manage their connection ex: wifi connection.

Installation
------------------------

    DCM require the user as sudoers.

You can install DCM directly from `PyPI`_:

::

    $ sudo pip install cmanager
    $ sudo cmanager configure

Or download from github repository, then:

::

    $ sudo python setup.py install
    $ sudo cmanager configure
    # Or
    $ sudo ./install.sh


**DCM** needs some python module below, `(this modules already included at pypi installed requires)`.

- colorama: ``sudo pip install colorama``
- terminaltables: ``sudo pip install terminaltables``
- pbkdf2: ``sudo pip install pbkdf2``
- netifaces: ``sudo pip install netifaces``
- python-wifi: ``sudo pip install python-wifi``

DCM needs some program/binary in sudoers file's whitelist so it won't ask for password while executing those program:

- iwlist
- wpa_supplicant
- dhclient
- pkill

To make you easier in installing DCM, just use install.sh script. You just need to run it with ``./install.sh``

Usage
------------------------

::

    $ sudo cmanager


Documentation
------------------------

Don't forget to run cmanager as with ``sudo cmanager``, type ``help`` inside DCM to get information about available commands

.. image:: https://raw.githubusercontent.com/fachrioktavian/DracOS-Connection-Manager/master/screenshots/help.jpeg

Dashboard section
------------------------

**See available interfaces**

DCM will detect interfaces on your system, categorize them into three types of interface (wireless, ethernet, localhost).
Use ``show interface`` to print those interface

.. image:: https://raw.githubusercontent.com/fachrioktavian/DracOS-Connection-Manager/master/screenshots/show_interfaces.jpeg

Wifi-wizard section
-------------------------

**Specifying wireless interface to used by DCM**

Before you can ask DCM to scan available networks and connecting to one of them using profile that you've been created (see profile explanation),
you should specify wireless interface that DCM will use to do those activity, type ``use [wireless_interface]``.

.. image:: https://raw.githubusercontent.com/fachrioktavian/DracOS-Connection-Manager/master/screenshots/use_interface.jpeg

----------------------------

**Scan available wifi networks**

To scan available network, simply type ``scan``.

.. image:: https://raw.githubusercontent.com/fachrioktavian/DracOS-Connection-Manager/master/screenshots/scan_networks.jpeg

----------------------------

**Creating profile**

Profile in DCM is a configuration file that has information about wifi connection like SSID, type of connection (Open/WPA), and passphrase if the connection is WPA type.
To create a profile, simply input value to available option (name, ssid, type, passphrase) using ``set name [value]``,
``set ssid [value]``, ``set type [value]``, ``set passphrase [value]``. ``show options`` to see available options. For Open type connection,
you just need to input name, ssid, and type, no need to supply passphrase information.

After all informations needed to create a profile have been provided, simply ``save profile`` and your profile will be saved.
To see all information about all profiles that have been saved, type ``show profile``.

.. image:: https://raw.githubusercontent.com/fachrioktavian/DracOS-Connection-Manager/master/screenshots/create_profile.jpeg

----------------------------

**Connecting to a network**

To connecting DCM to a network use a specified profile name, type ``connect [profile]``. To disconnect it, simply type ``CTRL+C``.

.. image:: https://raw.githubusercontent.com/fachrioktavian/DracOS-Connection-Manager/master/screenshots/connect_wifi.jpeg

Contributing to DCM
----------------------------

The easiest way to contribute to DCM is to file issues.

License
----------------------------

See `LICENSE`_

Changelog
----------------------------

See `CHANGELOG.md`_


.. _PyPI: https://pypi.python.org/pypi/cmanager
.. _LICENSE: https://github.com/fachrioktavian/DracOS-Connection-Manager/blob/master/LICENSE.txt
.. _CHANGELOG.md: https://github.com/fachrioktavian/DracOS-Connection-Manager/blob/master/CHANGELOG.md
