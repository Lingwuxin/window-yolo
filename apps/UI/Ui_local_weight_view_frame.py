# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\python_tring\deep_learning\garbage\apps\UI\local_weight_view_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_local_weight_ViewFrame(object):
    def setupUi(self, local_weight_ViewFrame):
        local_weight_ViewFrame.setObjectName("local_weight_ViewFrame")
        local_weight_ViewFrame.resize(600, 596)
        local_weight_ViewFrame.setMaximumSize(QtCore.QSize(600, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(local_weight_ViewFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(local_weight_ViewFrame)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_detect_labels = QtWidgets.QLabel(self.splitter_2)
        self.label_detect_labels.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_detect_labels.setObjectName("label_detect_labels")
        self.label_player = QtWidgets.QLabel(self.splitter_2)
        self.label_player.setStyleSheet("font: 36pt \"Agency FB\";\n"
"background-color:rgb(229, 229, 229);")
        self.label_player.setAlignment(QtCore.Qt.AlignCenter)
        self.label_player.setObjectName("label_player")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.combox_select_weights = QtWidgets.QComboBox(self.splitter)
        self.combox_select_weights.setMaximumSize(QtCore.QSize(16777215, 30))
        self.combox_select_weights.setCurrentText("")
        self.combox_select_weights.setObjectName("combox_select_weights")
        self.pushButton_statr_detect = QtWidgets.QPushButton(self.splitter)
        self.pushButton_statr_detect.setObjectName("pushButton_statr_detect")
        self.label_res_msg = QtWidgets.QLabel(self.splitter_2)
        self.label_res_msg.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_res_msg.setObjectName("label_res_msg")
        self.textEdit_res_msg = QtWidgets.QTextEdit(self.splitter_2)
        self.textEdit_res_msg.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit_res_msg.setObjectName("textEdit_res_msg")
        self.verticalLayout.addWidget(self.splitter_2)

        self.retranslateUi(local_weight_ViewFrame)
        QtCore.QMetaObject.connectSlotsByName(local_weight_ViewFrame)

    def retranslateUi(self, local_weight_ViewFrame):
        _translate = QtCore.QCoreApplication.translate
        local_weight_ViewFrame.setWindowTitle(_translate("local_weight_ViewFrame", "Frame"))
        self.label_detect_labels.setText(_translate("local_weight_ViewFrame", "检测目标"))
        self.label_player.setText(_translate("local_weight_ViewFrame", "无信号"))
        self.pushButton_statr_detect.setText(_translate("local_weight_ViewFrame", "启动模型"))
        self.label_res_msg.setText(_translate("local_weight_ViewFrame", "信息栏"))
        self.textEdit_res_msg.setHtml(_translate("local_weight_ViewFrame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">尚未开始推理</p></body></html>"))