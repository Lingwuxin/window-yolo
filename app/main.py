from re import S
import sys
import os
from typing import List, Tuple
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap, QImage
from numpy import ndarray
from UI.Ui_main import Ui_MainWindow
from YOLOv5.garbage_detect import RunthreadSatrtDetect
import time
import cv2


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.start_detect_thread = None
        # app_window = QtWidgets.QMainWindow()
        self.setupUi(self)
        self.setWindowTitle("YOLO可视化窗口")
        self.pushButton_statr_detect.clicked.connect(self.startDetect)

    # 在子线程中启动推理模型
    def startDetect(self):
        self.label_player.setText("加载中")
        if self.start_detect_thread == None:
            self.start_detect_thread = RunthreadSatrtDetect()
            self.start_detect_thread.detect_img.connect(self.show_label_img)
            self.start_detect_thread.msg.connect(self.setTextEdit)
        self.start_detect_thread.run_thread_statue = True
        self.start_detect_thread.start()
        self.pushButton_statr_detect.clicked.connect(self.exitDetect)
        self.pushButton_statr_detect.clicked.disconnect(self.startDetect)
        self.textEdit_res_msg.setText('加载模型中')
        self.pushButton_statr_detect.setText("退出推理")

    def exitDetect(self):
        self.start_detect_thread.run_thread_statue = False
        self.start_detect_thread.quit()
        self.start_detect_thread.wait()
        self.start_detect_thread = None
        self.pushButton_statr_detect.setText("启动推理")
        self.pushButton_statr_detect.clicked.connect(self.startDetect)
        self.pushButton_statr_detect.clicked.disconnect(self.exitDetect)
        self.label_player.setText("加载中")

    def stopDetect(self):
        return

    def continueDetect(self):
        return

    # def getLabelmsg(self):
    #     self.label_res_msg.setText("输出推理目标信息")
    #     self.get_label_thread = RunthreadGetLabelMsg()
    #     self.get_label_thread.msg.connect(self.setTextEdit)
    #     self.get_label_thread.start()

    def setTextEdit(self, msg: str):
        self.textEdit_res_msg.append(msg)
        textCursor = self.textEdit_res_msg.textCursor()
        self.textEdit_res_msg.moveCursor(textCursor.End)

    def show_label_img(self, img: ndarray):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = QImage(
            img[:],
            img.shape[1],
            img.shape[0],
            img.shape[1] * 3,
            QtGui.QImage.Format_RGB888,
        )
        self.label_player.setPixmap(QPixmap.fromImage(img))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainapp = MainApp()
    mainapp.show()
    app.exec()
