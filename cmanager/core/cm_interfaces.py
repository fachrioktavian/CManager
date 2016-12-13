# Copyright 2016 Fachrizal Oktavian
# This file is part of DracOS Connection Manager.
#
# DracOS Connection Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DracOS Connection Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DracOS Connection Manager.  If not, see <http://www.gnu.org/licenses/>.

"""
cm_interfaces
"""

import netifaces
from pythonwifi.iwlibs import Wireless
from terminaltables import AsciiTable
from colorama import Fore, Back, Style, init


class Cm_interfaces(object):

    init(autoreset=True)

    def __init__(self):
        self.ifaces = netifaces.interfaces()
        self.ifaces_wireless = []
        self.ifaces_ethernet = []
        self.ifaces_localhost = []
        self.dict_type = {}
        self.dict_status = {}
        self.dict_ssid = {}
        self.dict_mode = {}
        self.dict_wname = {}
        self.dict_apaddr = {}
        self.dict_ipaddr = {}
        self.dict_mask = {}

    def resolve_Interfaces(self):
        for data in self.ifaces:
            try:
                Wireless(data).getWirelessName()
                self.dict_type[data] = 'wireless'
            except IOError:
                self.dict_type[data] = 'non-wireless'
        for data in self.ifaces:
            try:
                info = netifaces.ifaddresses(data)[netifaces.AF_INET][0]
                self.dict_ipaddr[data] = info['addr']
                self.dict_mask[data] = info['netmask']
                if info.has_key('peer'):
                    self.dict_type[data] = 'localhost'
                    self.dict_status[data] = 'connected'
                elif self.dict_type[data] != 'wireless':
                    self.dict_type[data] = 'ethernet'
                    self.dict_status[data] = 'connected'
                else:
                    self.dict_status[data] = 'connected'
            except KeyError:
                self.dict_status[data] = 'not-connected'
                self.dict_ipaddr[data] = self.dict_mask[data] = '-'
        for data in self.ifaces:
            self.dict_ssid[data] = self.dict_mode[data] = self.dict_wname[
                data] = self.dict_apaddr[data] = '-'
            try:
                if self.dict_type[data] == 'wireless' and self.dict_status[data] == 'connected':
                    self.dict_ssid[data] = Wireless(data).getEssid()
                    self.dict_apaddr[data] = Wireless(data).getAPaddr()
                self.dict_mode[data] = Wireless(data).getMode()
                self.dict_wname[data] = Wireless(data).getWirelessName()
            except IOError:
                pass

        for data in self.dict_type:
            if self.dict_type[data] == 'wireless':
                self.ifaces_wireless.append(data)
            elif self.dict_type[data] == 'ethernet':
                self.ifaces_ethernet.append(data)
            elif self.dict_type[data] == 'localhost':
                self.ifaces_localhost.append(data)
        return True

    def get_ifaces_wireless(self):
        return self.ifaces_wireless

    def get_ifaces_ethernet(self):
        return self.ifaces_ethernet

    def get_ifaces_localhost(self):
        return self.ifaces_localhost

    def print_ifaces_wireless_table(self):
        indent = ' ' * 1
        header = indent + 'Wireless interfaces information:\n'
        self.wireless_table = [['Interface', 'Status', 'IP Address',
                                'Mask', 'Mode', 'SSID', 'AP Address', 'Wireless Type']]
        for data in self.ifaces_wireless:
            self.wireless_table.append([
                data,
                self.dict_status[data],
                self.dict_ipaddr[data],
                self.dict_mask[data],
                self.dict_mode[data],
                self.dict_ssid[data],
                self.dict_apaddr[data],
                self.dict_wname[data]
            ])
        table = AsciiTable(self.wireless_table)
        print (Fore.YELLOW + Style.DIM + header + table.table)

    def print_ifaces_ethernet_table(self):
        indent = ' ' * 1
        header = indent + 'Ethernet interfaces information:\n'
        self.ethernet_table = [['Interface', 'Status', 'IP Address', 'Mask']]
        for data in self.ifaces_ethernet:
            self.ethernet_table.append([
                data,
                self.dict_status[data],
                self.dict_ipaddr[data],
                self.dict_mask[data]
            ])
        table = AsciiTable(self.ethernet_table)
        print (Fore.YELLOW + Style.DIM + header + table.table)

    def print_ifaces_localhost_table(self):
        indent = ' ' * 1
        header = indent + 'Localhost interfaces information:\n'
        self.localhost_table = [['Interface', 'Status', 'IP Address', 'Mask']]
        for data in self.ifaces_localhost:
            self.localhost_table.append([
                data,
                self.dict_status[data],
                self.dict_ipaddr[data],
                self.dict_mask[data]
            ])
        table = AsciiTable(self.localhost_table)
        print (Fore.YELLOW + Style.DIM + header + table.table)
