# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\python_tring\deep_learning\新建文件夹\window-yolo\apps\UI\add_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(433, 178)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(settings)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(settings)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(settings)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Form"))
        self.radioButton_2.setText(_translate("settings", "使用摄像头"))
        self.radioButton.setText(_translate("settings", "使用rtmp传输"))
