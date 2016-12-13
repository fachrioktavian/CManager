# Copyright 2016 Fachrizal Oktavian
# This file is part of CManager.
#
# CManager is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CManager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CManager.  If not, see <http://www.gnu.org/licenses/>.

"""
cm_connection
"""

import pbkdf2
from terminaltables import AsciiTable
import os
import subprocess
import time
from colorama import Fore, Back, Style, init


class Cm_connection(object):

    init(autoreset=True)
    profile_path = '/usr/share/cmanager/profile/'

    ACT_SYSTEM = 'system'
    ACT_POS = '+'
    ACT_NEG = '-'

    WPA_CONNECTED = 'CTRL-EVENT-CONNECTED'
    WPA_DISCONNECTED = 'CTRL-EVENT-DISCONNECTED'
    WPA_SCAN_FAILED = 'CTRL-EVENT-SCAN-FAILED'

    def debug(self, indent, actor, deb_type, msg):
        """
        deb_type -> 0:info, 1:succeed, 2:failed
        """
        list_type = [Fore.YELLOW, Fore.GREEN, Fore.RED]
        deb_style = Style.DIM
        deb_color = list_type[deb_type]
        spaces = ' ' * indent
        print (deb_color + deb_style + spaces + '[' + actor + '] ' + msg)

    def __init__(self):
        self.dict_profile = {'NAME': '', 'SSID': '', 'TYPE': '', 'PASSPHRASE': ''}

    def get_compute_pmk(self, passphrase):
        pmk = pbkdf2.PBKDF2(passphrase, self.dict_profile['SSID'], 4096).read(32).encode("hex")
        return pmk

    def set_profile_name(self, name):
        self.dict_profile['NAME'] = name

    def set_profile_ssid(self, ssid):
        self.dict_profile['SSID'] = ssid

    def set_profile_type(self, enc_type):
        self.dict_profile['TYPE'] = enc_type

    def set_profile_passphrase(self, passphrase):
        self.dict_profile['PASSPHRASE'] = passphrase

    def save_profile(self):
        if self.dict_profile['TYPE'] == 'Open':
            output = open(self.profile_path + self.dict_profile['NAME'] + '.conf', 'w')
            config = '#Open\nnetwork={\n\tssid="' + \
                self.dict_profile['SSID'] + '"\n\tkey_mgmt=NONE\n\tpriority=100\n}\n'
            output.write(config)
            output.close()
            return True
        elif self.dict_profile['TYPE'] == 'WPA':
            output = open(self.profile_path + self.dict_profile['NAME'] + '.conf', 'w')
            config = '#WPA\nnetwork={\n\tssid="' + self.dict_profile['SSID'] + '"\n\t#psk="' + self.dict_profile[
                'PASSPHRASE'] + '"\n\tpsk=' + self.get_compute_pmk(self.dict_profile['PASSPHRASE']) + '\n}\n'
            output.write(config)
            output.close()
            return True
        return False

    def show_options(self):
        indent = ' '
        header = indent + 'Available Options for creating profile:\n'
        info = 'name       -> ' + self.dict_profile['NAME'] + '\n'
        info += 'ssid       -> ' + self.dict_profile['SSID'] + '\n'
        info += 'type       -> ' + self.dict_profile['TYPE'] + '\n'
        info += 'passphrase -> ' + self.dict_profile['PASSPHRASE']
        print (Fore.YELLOW + Style.DIM + header + info)

    def show_profile(self):
        indent = ' '
        header = indent + 'List of profiles saved by system:\n'
        table = [['Profile name', 'Connection type', 'SSID', 'Passphrase']]
        list_profile = os.listdir(self.profile_path)
        for fileconf in list_profile:
            of_file = open(self.profile_path + fileconf, 'r')
            of = of_file.read().split('\n')
            if of[0][1::] == 'Open':
                table.append([fileconf[:-5:], 'Open', of[2][7:-1:], '-'])
            elif of[0][1::] == 'WPA':
                table.append([fileconf[:-5:], 'WPA', of[2][7:-1:], of[3][7:-1:]])
            of_file.close()
        print (Fore.YELLOW + Style.DIM + header + AsciiTable(table).table)

    def delete_profile(self, profile):
        try:
            os.remove(self.profile_path + profile + '.conf')
            return True
        except:
            return False

    def exec_dhclient(self, iface):
        program = ['/sbin/dhclient']
        cmd_release = ('-r ' + iface).split(' ')
        cmd_request = [iface]
        try:
            p = subprocess.Popen(['sudo'] + program + cmd_release,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.wait()
            p = subprocess.Popen(['sudo'] + program + cmd_request,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.wait()
            return True
        except:
            return False

    def release_dhclient(self, iface):
        program = ['/sbin/dhclient']
        cmd_release = ('-r ' + iface).split(' ')
        try:
            p = subprocess.Popen(['sudo'] + program + cmd_release,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.wait()
            return True
        except:
            return False

    def kill_wpasupp(self, iface):
        try:
            cmd = '/bin/ps a'.split(' ')
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for line in iter(p.stdout.readline, b''):
                if 'sudo' in line and 'wpa_supplicant' in line and iface in line:
                    result = line.split(' ')
                    while '' in result:
                        result.remove('')
                    pid = result[0]
                    program = ['/usr/bin/pkill']
                    cmd_kill = ('-P ' + pid).split(' ')
                    p = subprocess.Popen(['sudo'] + program + cmd_kill,
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except:
            return False

    flagReconnect = True

    def connect_profile(self, iface, profile):
        program = ['/sbin/wpa_supplicant']
        cmd = ('-D nl80211 -i ' + iface + ' -c ' + self.profile_path + profile + '.conf').split(' ')
        try:
            p = subprocess.Popen(['sudo'] + program + cmd, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, bufsize=1)
            for line in iter(p.stdout.readline, b''):
                # print (line)
                if self.WPA_CONNECTED in line:
                    self.debug(2, self.ACT_POS, 1, 'Connected')
                    flagExecDhclient = self.exec_dhclient(iface)
                    if flagExecDhclient:
                        self.flagReconnect = True
                        self.debug(2, self.ACT_POS, 1, 'Got IP address from server')
                    else:
                        self.debug(2, self.ACT_NEG, 2, 'Couldn\'t got IP adrress from server')
                        p.stdout.close()
                        break
                if self.WPA_DISCONNECTED in line or self.WPA_SCAN_FAILED in line:
                    self.debug(2, self.ACT_NEG, 2, 'Disconnected')
                    flagKillWpasupp = self.kill_wpasupp(iface)
                    flagRelDhclient = self.release_dhclient(iface)
                    if flagKillWpasupp and flagRelDhclient and self.flagReconnect:
                        self.flagReconnect = False
                        self.debug(2, self.ACT_SYSTEM, 0, 'Reconnecting')
                        self.connect_profile(iface, profile)
                    else:
                        self.debug(2, self.ACT_NEG, 2,
                                   'Error\'s occured while reconnecting interface')
                        p.stdout.close()
                        break
        except KeyboardInterrupt:
            self.debug(1, self.ACT_SYSTEM, 1, 'Disconnecting')
            flagKillWpasupp = self.kill_wpasupp(iface)
            flagRelDhclient = self.release_dhclient(iface)
            if flagKillWpasupp and flagRelDhclient:
                self.debug(2, self.ACT_POS, 1, 'Disconnected')
            else:
                self.debug(2, self.ACT_POS, 1, 'Error\'s occured while disconnecting interface')
        except Exception as e:
            print (e)
            self.debug(2, self.ACT_NEG, 2, 'Error\'s occured while connecting interface')
