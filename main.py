from UI.Ui_view_frame import Ui_ViewFrame
from UI.Ui_window import Ui_MainWindow
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap, QImage
from typing import List, Tuple
import os
import sys
import cv2
from numpy import ndarray
from YOLOv5.window_detect import RunDetect
class MainApp(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        # app_window = QtWidgets.QMainWindow()
        self.main_ui = Ui_MainWindow()
        self.view_ui=Ui_ViewFrame()
        self.main_ui.setupUi(self)
        self.add_view_frame()
        self.ready_model()
        
    def add_view_frame(self):
        widget=QWidget()
        self.view_ui.setupUi(widget)
        self.main_ui.view_frame_gridLayout.addWidget(widget)

    def ready_model(self):
        self.view_ui.pushButton_statr_detect.clicked.connect(self.startDetect)
        self.setCombox_select()  # 加载模型列表
        self.detect_thread = QtCore.QThread()  # 初始化一个QT线程管理器
        self.start_detect = RunDetect()  # 初始化模型推理对象

        # 为self.detect_thread.start()信号绑定槽函数
        self.detect_thread.started.connect(self.start_detect.run)
        self.start_detect.moveToThread(self.detect_thread)# 将模型推理对象挂载到QT线程管理器上
        # 处理推理过程中发出的信号并绑定槽函数
        self.start_detect.detect_img.connect(self.show_label_img)
        self.start_detect.msg.connect(self.setTextEdit)
        self.start_detect.label.connect(self.setDetectLabels)

    def startDetect(self):
        self.view_ui.label_player.setText("加载中")
        self.start_detect.run_thread_statue = True
        self.start_detect.weight_file = (
            self.view_ui.combox_select_weights.currentText()  # 选中模型
        )
        self.detect_thread.start()
        self.view_ui.pushButton_statr_detect.clicked.disconnect(self.startDetect)
        self.view_ui.pushButton_statr_detect.clicked.connect(self.exitDetect)
        self.view_ui.textEdit_res_msg.setText("加载模型中")
        self.view_ui.pushButton_statr_detect.setText("退出推理")

    # 读取模型权重文件名
    def setCombox_select(self):
        for root, dirs, files in os.walk("YOLOv5/weights/"):
            if len(files) == 0:
                self.view_ui.combox_select_weights.addItem("--未找到模型权重--")
                break
            self.view_ui.combox_select_weights.addItems(files)

    def exitDetect(self):
        self.start_detect.run_thread_statue = False
        self.detect_thread.quit()
        self.detect_thread.wait()
        self.view_ui.pushButton_statr_detect.setText("启动推理")
        self.view_ui.pushButton_statr_detect.clicked.connect(self.startDetect)
        self.view_ui.pushButton_statr_detect.clicked.disconnect(self.exitDetect)
        self.view_ui.label_player.setText("加载中")

    def stopDetect(self):
        pass

    def continueDetect(self):
        pass

    def setTextEdit(self, msg: List[str]):
        self.view_ui.textEdit_res_msg.append("\n".join(msg))
        textCursor = self.view_ui.textEdit_res_msg.textCursor()
        self.view_ui.textEdit_res_msg.moveCursor(textCursor.End)

    def show_label_img(self, img: ndarray):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = QImage(
            img[:],
            img.shape[1],
            img.shape[0],
            img.shape[1] * 3,
            QtGui.QImage.Format_RGB888,
        )
        self.view_ui.label_player.setPixmap(QPixmap.fromImage(img))

    def setDetectLabels(self, labels: List[str]):
        self.view_ui.label_detect_labels.setText(",".join(labels))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainapp = MainApp()
    mainapp.show()
    app.exec()