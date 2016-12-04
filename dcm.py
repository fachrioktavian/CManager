#!/usr/bin/python
# Copyright 2016 Fachrizal Oktavian
#   This file is part of DracOS Connection Manager.
#
#   DracOS Connection Manager is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   DracOS Connection Manager is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with DracOS Connection Manager.  If not, see <http://www.gnu.org/licenses/>.

from classes.dcm_app import Dcm_app

if __name__=='__main__':
	dcm_app_handler = Dcm_app()
	dcm_app_handler.standby()