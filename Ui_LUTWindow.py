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
class Ui_LUTWindow(QDialog):

    Signal_LUT_Parameter = pyqtSignal(int,int,int,int,int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filed_dict = {}
        self.init_ui()

    def init_ui(self):
        """
        初始化对话框
        :return:
        """
        self.setWindowTitle("LUTSetting")
        self.resize(300,200)
        layout = QVBoxLayout()
        #读取文件中的标志

        self.spinbox_low = QtWidgets.QSpinBox()
        self.spinbox_high = QtWidgets.QSpinBox()
        self.spinbox_lut1 = QtWidgets.QSpinBox()
        self.spinbox_lut2 = QtWidgets.QSpinBox()
        self.spinbox_lut3 = QtWidgets.QSpinBox()
        self.num_LUT = {}

        file_xml = ET.parse(os.path.join(BASE_DIR,'db',"LUT.xml"))
        if file_xml:
            root = list(file_xml.getroot())
        for tag in root:
            if tag.tag == "LUT":
                for tag in tag:
                    strN = str(tag.get('Name'))
                    self.num_LUT[strN] = int(tag.get('Index'))
        #标签
        lbl = QLabel()
        lbl.setText('映射范围：')
        layout.addWidget(lbl)
        #映射范围
        map_layout = QHBoxLayout()
        lbl = QLabel()
        lbl.setText('0')
        map_layout.addWidget(lbl)

        map_layout.addStretch()

        self.spinbox_low.setMaximum(255)
        self.spinbox_low.setValue(self.num_LUT['Limit1'])
        self.spinbox_low.valueChanged.connect(self.spinbox_low_changed)
        map_layout.addWidget(self.spinbox_low)

        map_layout.addStretch()

        self.spinbox_high.setMaximum(255)
        self.spinbox_high.setValue(self.num_LUT['Limit2'])
        self.spinbox_high.valueChanged.connect( self.spinbox_high_changed)
        map_layout.addWidget(self.spinbox_high)

        map_layout.addStretch()

        lbl  =QLabel()
        lbl.setText('255')
        map_layout.addWidget(lbl)

        layout.addLayout(map_layout)

        #标签
        lbl = QLabel()
        lbl.setText('映射阈值:')
        layout.addWidget(lbl)
        #映射值
        map_layout = QHBoxLayout()
        map_layout.addStretch()
        self.spinbox_lut1.setMaximum(255)
        self.spinbox_lut1.setValue(self.num_LUT['LUTNUM1'])
        map_layout.addWidget(self.spinbox_lut1)
        map_layout.addStretch()
        self.spinbox_lut2.setMaximum(255)
        self.spinbox_lut2.setValue(self.num_LUT['LUTNUM2'])
        map_layout.addWidget(self.spinbox_lut2)
        map_layout.addStretch()
        self.spinbox_lut3.setMaximum(255)
        self.spinbox_lut3.setValue(self.num_LUT['LUTNUM3'])
        map_layout.addWidget(self.spinbox_lut3)
        map_layout.addStretch()
        layout.addLayout(map_layout)
        #OK按钮
        map_layout = QHBoxLayout()
        map_layout.addStretch()
        btn_ok = QPushButton()
        btn_ok.setText("OK")
        btn_ok.clicked.connect(self.ok_clicked)
        map_layout.addWidget(btn_ok)
        map_layout.addStretch()

        layout.addWidget(btn_ok)
        self.setLayout(layout)
    def spinbox_low_changed(self):
        if self.spinbox_low.value() > self.spinbox_high.value():
            self.spinbox_low.setValue(self.spinbox_high.value())
        self.spinbox_high.setMinimum(self.spinbox_low.value())
    def spinbox_high_changed(self):
        self.spinbox_low.setMaximum(self.spinbox_high.value())
        if self.spinbox_high.value() < self.spinbox_low.value():
            self.spinbox_high.setValue(self.spinbox_low.value())
    def ok_clicked(self):
        file_xml = ET.parse(os.path.join(BASE_DIR,'db',"LUT.xml"))
        if file_xml:
            for tag in file_xml.findall('LUT'):
                tag.set('Limit1',str(self.spinbox_low.value()))
                tag.set('Limit2',str(self.spinbox_high.value()))
                tag.set('LUTNUM1',str(self.spinbox_lut1.value()))
                tag.set('LUTNUM2',str(self.spinbox_lut2.value()))
                tag.set('LUTNUM3',str(self.spinbox_lut3.value()))
        self.Signal_LUT_Parameter.emit(self.spinbox_low.value(),self.spinbox_high.value(),self.spinbox_lut1.value(),self.spinbox_lut2.value(),self.spinbox_lut3.value())

