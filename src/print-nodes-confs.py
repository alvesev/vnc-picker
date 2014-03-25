#!/usr/bin/python3

#
#   Copyright 2014 Alex Vesev
#
#   This application name is VNC-Picker, which may be wraped as
#   "VNCP".
#
#   This file is a part of VNC-Picker.
#
#   This application is free software: you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This application is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this script. If not, see <http://www.gnu.org/licenses/>.
#
##


import sys
import configparser
import os
from os.path import expanduser
import re

def selectFirstFoundConfFileNameFromPool(fileNamesPool):
    for singleFileName in fileNamesPool :
        if os.path.isfile(singleFileName):
            return singleFileName
    raise Exception("No configuration files found among the listed ones: "
            + str(fileNamesPool))

def isSectionNodeDescription(sectionName):
    if re.search('^(\s)*node', sectionName):
        return True
    return False

def printOrderedValuesFromSection(configSection):

    orderedKeys = (
            'user-name',
            'vnc-host-name',
            'ssh-port-number',
            'tun-host-name',
            'local-tun-port-number',
            'vnc-host-port-number',
            'display-identifier',
            'screen-size',
            'screen-dpi',
            'vnc-password-file'
        )

    for key in orderedKeys:
        try:
            value = configSection[key]
            if value:
                sys.stdout.write(configSection[key] + "\n")
            else:
                raise Exception("Got from configuration file's section "
                            + str(configSection)
                            + " false value '" + value
                            + "' for key '" + key + "'.")
        except:
            sys.stderr.write("\nFrom configuration file's section '"
                    + str(configSection)
                    + "' got unexpected value for key '" + key + "'.\n\n")
            raise

  #
 # #
# # #
 # #
  #


defaultInstallDirectory = '/opt/vnc-picker/'
currentUserHomeDir = expanduser('~')
thisDir = os.path.dirname(os.path.abspath(__file__))

confShortFileName = 'vnc-picker.conf'
confFullFileNamesPool = (
        currentUserHomeDir + '/.vnc-picker/' + confShortFileName,
        defaultInstallDirectory + confShortFileName,
        thisDir + '/' + confShortFileName
    )

fileNameConfWanted = selectFirstFoundConfFileNameFromPool(confFullFileNamesPool)
configInstance = configparser.ConfigParser()
configInstance.read(fileNameConfWanted)

for sectionName in configInstance.sections() :
    if isSectionNodeDescription(sectionName):
        sys.stdout.write('[node description start]' + '\n')
        printOrderedValuesFromSection(configInstance[sectionName])
        sys.stdout.write('[node description stop]' + '\n')
