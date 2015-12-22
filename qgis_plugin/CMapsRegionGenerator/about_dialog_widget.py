# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dialog_widget.ui'
#
# Created: Tue Dec 22 12:24:05 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(529, 237)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cmapsregiongenerator/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.centigonIconLabel = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centigonIconLabel.sizePolicy().hasHeightForWidth())
        self.centigonIconLabel.setSizePolicy(sizePolicy)
        self.centigonIconLabel.setMinimumSize(QtCore.QSize(128, 128))
        self.centigonIconLabel.setText(_fromUtf8(""))
        self.centigonIconLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cmapsregiongenerator/centigonsolutions_logo.png")))
        self.centigonIconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.centigonIconLabel.setObjectName(_fromUtf8("centigonIconLabel"))
        self.verticalLayout.addWidget(self.centigonIconLabel)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lutraLogoLabel = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lutraLogoLabel.sizePolicy().hasHeightForWidth())
        self.lutraLogoLabel.setSizePolicy(sizePolicy)
        self.lutraLogoLabel.setMinimumSize(QtCore.QSize(128, 46))
        self.lutraLogoLabel.setText(_fromUtf8(""))
        self.lutraLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cmapsregiongenerator/lutra_logo.png")))
        self.lutraLogoLabel.setObjectName(_fromUtf8("lutraLogoLabel"))
        self.verticalLayout.addWidget(self.lutraLogoLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.aboutBrowser = QtGui.QTextBrowser(Dialog)
        self.aboutBrowser.setAcceptRichText(False)
        self.aboutBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.aboutBrowser.setOpenExternalLinks(True)
        self.aboutBrowser.setOpenLinks(True)
        self.aboutBrowser.setObjectName(_fromUtf8("aboutBrowser"))
        self.horizontalLayout.addWidget(self.aboutBrowser)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About CMAPS Region Generator", None))
        self.aboutBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#efe1bb\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))

import resources_rc
