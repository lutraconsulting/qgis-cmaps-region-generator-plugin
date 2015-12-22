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

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from about_dialog_widget import Ui_Dialog
from version import pythonPluginVersion

class AboutDialog(QDialog, Ui_Dialog):
    
    def __init__(self, iface):
        
        QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        
        self.setupUi(self)
        self.iface = iface
        
        self.aboutBrowser.setHtml( self.source() )
        
        QObject.connect(self.aboutBrowser, SIGNAL("anchorClicked(QUrl)"), self.linkClicked)
        
        
    def __del__(self):
        QObject.disconnect(self.aboutBrowser, SIGNAL("anchorClicked(QUrl)"), self.linkClicked)
        
        
    def linkClicked(self, url):
        
        QDesktopServices.openUrl(url)

    def source(self):
        return """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:'IstokWeb,IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:9pt; font-weight:400; font-style:normal;"><p style=" margin-top:6px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'IstokWeb,IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; font-weight:600; color:#505050;">CMAPS Region Generator</span></p><p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; color:#505050;">Version """ + pythonPluginVersion() + """</span></p><p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; color:#505050;">CMaps Analytics Region Creator is a utility designed for&nbsp;typical business intelligence practitioners or dashboard developers to transform typical geographic administrative areas like zip, state, and country into custom business regions and territories.</span></p><p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; color:#505050;">Check out the </span><a href="http://centigonknowledge.com/cmaps-analytics-region-creator/"><span style=" font-family:'IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; text-decoration: none; color:#13AA49;">project page</span></a><span style=" font-family:'IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; color:#505050;"> for more information.</span></p><p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; color:#505050;">Developed for </span><a href="http://centigonsolutions.com/"><span style=" font-family:'IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; text-decoration: none; color:#13AA49;">Centigon Solutions, Inc.</span></a><span style=" font-family:'IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; color:#505050;"> by </span><a href="http://www.lutraconsulting.co.uk/"><span style=" font-family:'IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; text-decoration: none; color:#13AA49;">Lutra Consulting</span></a><span style=" font-family:'IstokWeb,FreeSans,Geneva,Arial,sans-serif'; font-size:8pt; color:#505050;">.</span></p></body></html>"""
        
