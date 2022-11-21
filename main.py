import sys
from typing import List, Tuple
import os
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap, QImage
from numpy import ndarray
from UI.Ui_main import Ui_MainWindow
from YOLOv5.window_detect import RunDetect
import cv2
import time


class MainApp(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        # app_window = QtWidgets.QMainWindow()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.setWindowTitle("YOLO可视化窗口")
        self.ready_model()

    def ready_model(self):
        self.main_ui.pushButton_statr_detect.clicked.connect(self.startDetect)
        self.setCombox_select()
        self.detect_thread = QtCore.QThread()
        self.start_detect_thread = RunDetect()
        self.detect_thread.started.connect(self.start_detect_thread.run)
        self.start_detect_thread.moveToThread(self.detect_thread)
        self.start_detect_thread.detect_img.connect(self.show_label_img)
        self.start_detect_thread.msg.connect(self.setTextEdit)
        self.start_detect_thread.label.connect(self.setDetectLabels)

    def startDetect(self):
        self.main_ui.label_player.setText("加载中")
        self.start_detect_thread.run_thread_statue = True
        self.start_detect_thread.weight_file = (
            self.main_ui.combox_select_weights.currentText()  # 选中模型
        )
        self.detect_thread.start()
        self.main_ui.pushButton_statr_detect.clicked.disconnect(self.startDetect)
        self.main_ui.pushButton_statr_detect.clicked.connect(self.exitDetect)
        self.main_ui.textEdit_res_msg.setText("加载模型中")
        self.main_ui.pushButton_statr_detect.setText("退出推理")

    # 读取模型权重文件名
    def setCombox_select(self):
        for root, dirs, files in os.walk("YOLOv5/weights/"):
            if len(files) == 0:
                self.main_ui.combox_select_weights.addItem("--未找到模型权重--")
                break
            self.main_ui.combox_select_weights.addItems(files)

    def exitDetect(self):
        self.start_detect_thread.run_thread_statue = False
        self.detect_thread.quit()
        self.detect_thread.wait()
        self.main_ui.pushButton_statr_detect.setText("启动推理")
        self.main_ui.pushButton_statr_detect.clicked.connect(self.startDetect)
        self.main_ui.pushButton_statr_detect.clicked.disconnect(self.exitDetect)
        self.main_ui.label_player.setText("加载中")

    def stopDetect(self):
        pass

    def continueDetect(self):
        pass

    def setTextEdit(self, msg: List[str]):
        self.main_ui.textEdit_res_msg.append("\n".join(msg))
        textCursor = self.main_ui.textEdit_res_msg.textCursor()
        self.main_ui.textEdit_res_msg.moveCursor(textCursor.End)

    def show_label_img(self, img: ndarray):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = QImage(
            img[:],
            img.shape[1],
            img.shape[0],
            img.shape[1] * 3,
            QtGui.QImage.Format_RGB888,
        )
        self.main_ui.label_player.setPixmap(QPixmap.fromImage(img))

    def setDetectLabels(self, labels: List[str]):
        self.main_ui.label_detect_labels.setText(",".join(labels))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainapp = MainApp()
    mainapp.show()
    app.exec()
