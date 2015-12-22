# -*- coding: utf-8 -*-

# CMAPS Region Generator - Automate merging features using a CSV file definition.
# Copyright (C) 2013 Centigon Solutions Inc.

# sales at centigonsolutions dot com
# 1333 Camino Del Rio S #300
# San Diego 
# CA 92108
# USA

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from version import pythonPluginVersion

def name():
    return "CMaps Region Generator"


def description():
    return "Automate merging features using a CSV file definition."


def version():
    return "Version " + pythonPluginVersion()


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Lutra Consulting for Centigon Solutions"

def email():
    return "sales@centigonsolutions.com"

def classFactory(iface):
    # load CMapsRegionGenerator class from file CMapsRegionGenerator
    from cmapsregiongenerator import CMapsRegionGenerator
    return CMapsRegionGenerator(iface)
