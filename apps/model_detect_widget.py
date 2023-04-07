from .UI.Ui_local_weight_view_frame import Ui_local_weight_ViewFrame
from .UI.Ui_view_frame import Ui_ViewFrame
from .YOLOv5.window_detect import RunDetect
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap, QImage
from typing import List, Tuple
import typing
import os
import sys
import cv2
from numpy import ndarray


class DetectWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._run()

    def _run(self):
        self.view_ui = Ui_ViewFrame()
        self.view_ui.setupUi(self)
        self.detect_thread = QtCore.QThread()  # 初始化一个QT线程管理器
        self.ready_model()

    def ready_model(self):
        self.view_ui.pushButton_statr_detect.clicked.connect(self.startDetect)
        self.start_detect = RunDetect()  # 初始化模型推理对象
        # 为self.detect_thread.start()信号绑定槽函数
        self.detect_thread.started.connect(self.start_detect.run)
        self.start_detect.moveToThread(self.detect_thread)  # 将模型推理对象挂载到QT线程管理器上
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

    def exitDetect(self):
        self.start_detect.run_thread_statue = False
        self.detect_thread.quit()
        self.detect_thread.wait()
        self.view_ui.pushButton_statr_detect.setText("启动推理")
        self.view_ui.pushButton_statr_detect.clicked.disconnect(self.exitDetect)
        self.view_ui.pushButton_statr_detect.clicked.connect(self.startDetect)
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


class LocalWeightDetectWidget(DetectWidget):
    def _run(self):
        self.view_ui = Ui_local_weight_ViewFrame()
        self.view_ui.setupUi(self)
        self.detect_thread = QtCore.QThread()  # 初始化一个QT线程管理器
        self.setCombox_select()
        self.ready_model()
    # 读取模型权重文件名
    def setCombox_select(self):
        for root, dirs, files in os.walk("apps/YOLOv5/weights/"):
            if len(files) == 0:
                self.view_ui.combox_select_weights.addItem("--未找到模型权重--")
                break
            self.view_ui.combox_select_weights.addItems(files)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainapp = DetectWidget()
    mainapp.show()
    app.exec()
