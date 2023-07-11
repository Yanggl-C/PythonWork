# -*- coding: utf-8 -*-
import os.path

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout,QDialog,QPushButton,QLabel,QLineEdit,QMessageBox,QTextEdit,QHBoxLayout
import sys
import os
import xml.etree.ElementTree as ET
from PyQt5.QtCore import Qt, pyqtSignal

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
class Ui_AdapterThresholdWindow(QDialog):

    Signal_AdapterThreshold_Parameter = pyqtSignal(int,int,int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filed_dict = {}
        self.init_ui()

    def init_ui(self):
        """
        初始化对话框
        :return:
        """
        self.setWindowTitle("AdapterThresholdSetting")
        self.resize(300,200)
        layout = QVBoxLayout()
        #读取文件中的标志

        self.combox_Method = QtWidgets.QComboBox()
        self.combox_Type = QtWidgets.QComboBox()
        self.combox_blocksize = QtWidgets.QComboBox()
        self.threshold_flag = {}

        file_xml = ET.parse(os.path.join(BASE_DIR,'db',"AdapterThreshold.xml"))
        if file_xml:
            root = list(file_xml.getroot())
        for tag in root:
            if tag.tag == 'ADAPTIVE_THRESH':
                for info in tag:
                    strN = str(info.tag)
                    self.threshold_flag[strN] = int(info.text)
                    self.combox_Method.addItem(strN)
            if tag.tag == 'THRESH_BINARY':
                for info in tag:
                    strN = str(info.tag)
                    self.threshold_flag[strN] = int(info.text)
                    self.combox_Type.addItem(strN)
            if tag.tag == 'BLOCK_SIZE':
                for info in tag:
                    strN = str(info.get('Index'))
                    self.combox_blocksize.addItem(strN)
        #标签
        lbl = QLabel()
        lbl.setText('阈值算法:')
        layout.addWidget(lbl)

        layout.addWidget(self.combox_Method)
        #标签
        lbl = QLabel()
        lbl.setText('阈值类型:')
        layout.addWidget(lbl)

        layout.addWidget(self.combox_Type)

        #标签
        lbl = QLabel()
        lbl.setText('邻域:')
        layout.addWidget(lbl)

        layout.addWidget(self.combox_blocksize)

        layout.addStretch()
        btn_ok = QPushButton()
        btn_ok.setText("OK")
        btn_ok.clicked.connect(self.ok_clicked)
        layout.addWidget(btn_ok)
        self.setLayout(layout)
    def ok_clicked(self):
        print(self.threshold_flag[str(self.combox_Method.currentText())])
        print(self.threshold_flag[str(self.combox_Type.currentText())])
        self.Signal_AdapterThreshold_Parameter.emit(self.threshold_flag[str(self.combox_Method.currentText())],self.threshold_flag[str(self.combox_Type.currentText())],int(self.combox_blocksize.currentText()))


