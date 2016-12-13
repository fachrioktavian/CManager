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
cm_help
"""

from colorama import Fore, Back, Style, init


class Cm_help(object):

    init(autoreset=True)

    def show_help(self):
        help = 'dashboard section:\n'
        help += ' show interfaces          : Print all interfaces found by cmanager\n'
        help += ' wizard wifi              : Go to wifi wizard section\n'
        help += ' exit                     : Exit cmanager\n\n'
        help += 'wifi-wizard section:\n'
        help += ' show profile             : List profile that saved by cmanager\n'
        help += ' show options             : List available options used to create a profile\n'
        help += ' set [options] [value]    : Set value to available options before save the profile\n'
        help += ' save profile             : Save profile after options data\'s been filled\n'
        help += ' del profile [profile]    : Del profile by profile\'s name\n'
        help += ' use [wireless_intarface] : Use this command BEFORE scanning available network or connecting a profile\n'
        help += ' scan                     : Scanning available networks\n'
        help += ' connect [profile]        : Connecting wireless interface to a wifi network using specified profile\'s name\n'
        help += ' back                     : Back to dashboard section'

        print (Fore.GREEN + Style.BRIGHT + help)
