# -*- coding: utf-8 -*-
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

import os
import sys
from core.cm_app import Cm_app


def main():
    if os.getuid() != 0:
        print ("[-] Please Access as root..!")
        sys.exit()

    if len(sys.argv) > 1:
        configure = sys.argv[1]
        if configure.lower() == 'configure':
            os.system('./cmanager/configure.sh')
            sys.exit()

    cm_app_handler = Cm_app()
    cm_app_handler.standby()


if __name__ == '__main__':
    main()
