# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout, QMessageBox, \
    QGraphicsPixmapItem,QScrollArea
from PyQt5.QtWidgets import QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
import algorithm as alg
#弹出框
import Ui_ThresholdWindow
import Ui_AdapterThresholdWindow
import Ui_LUTWindow
import Ui_FlipWindow

import numpy as np
import copy
import cv2
# 资源管理器
import tkinter as tk
from tkinter import filedialog

from copy import deepcopy

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))


class Ui_MainWindow(object):
    def __init__(self):
        #super(Ui_MainWindow,self).__init__()
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1215, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 581, 111))
        self.groupBox.setObjectName("groupBox")
        self.cmb_algorithm = QtWidgets.QComboBox(self.groupBox)
        self.cmb_algorithm.setGeometry(QtCore.QRect(10, 70, 441, 31))
        self.cmb_algorithm.setObjectName("cmb_algorithm")
        self.txt_PathShow = QtWidgets.QTextEdit(self.groupBox)
        self.txt_PathShow.setGeometry(QtCore.QRect(10, 20, 441, 31))
        self.txt_PathShow.setObjectName("txt_PathShow")
        self.btn_ReadPath = QtWidgets.QPushButton(self.groupBox)
        self.btn_ReadPath.setGeometry(QtCore.QRect(460, 20, 111, 31))
        self.btn_ReadPath.setObjectName("btn_ReadPath")
        self.label1 = QtWidgets.QLabel(self.groupBox)
        self.label1.setGeometry(QtCore.QRect(10, 50, 121, 21))
        self.label1.setObjectName("label1")
        self.btn_procressimg = QtWidgets.QPushButton(self.groupBox)
        self.btn_procressimg.setGeometry(QtCore.QRect(460, 70, 111, 31))
        self.btn_procressimg.setObjectName("btn_procressimg")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(610, 0, 581, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cmb_algorithm_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.cmb_algorithm_2.setGeometry(QtCore.QRect(10, 70, 441, 31))
        self.cmb_algorithm_2.setObjectName("cmb_algorithm_2")
        self.txt_PathShow_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.txt_PathShow_2.setGeometry(QtCore.QRect(10, 20, 441, 31))
        self.txt_PathShow_2.setObjectName("txt_PathShow_2")
        self.btn_ReadPath_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_ReadPath_2.setGeometry(QtCore.QRect(460, 20, 111, 31))
        self.btn_ReadPath_2.setObjectName("btn_ReadPath_2")
        self.label1_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label1_2.setGeometry(QtCore.QRect(10, 50, 121, 21))
        self.label1_2.setObjectName("label1_2")
        self.btn_procressimg_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_procressimg_2.setGeometry(QtCore.QRect(460, 70, 111, 31))
        self.btn_procressimg_2.setObjectName("btn_procressimg_2")

        self.scrollArea2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea2.setGeometry(QtCore.QRect(610, 120, 581, 511))
        #self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setObjectName("scrollArea2")
        self.scrollAreaWidgetContents2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents2.setGeometry(QtCore.QRect(0, 0, 581, 511))
        self.scrollAreaWidgetContents2.setObjectName("scrollAreaWidgetContents2")
        self.lab_showImg_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents2)
        self.lab_showImg_2.setGeometry(QtCore.QRect(0, 0, 581, 511))
        self.lab_showImg_2.setObjectName("lab_showImg_2")
        self.scrollArea2.setWidget(self.scrollAreaWidgetContents2)


        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 120, 581, 511))
        #self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 581, 511))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lab_showImg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lab_showImg.setGeometry(QtCore.QRect(0, 0, 581, 511))
        self.lab_showImg.setObjectName("lab_showImg")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1215, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_PathShow, self.btn_ReadPath)
        MainWindow.setTabOrder(self.btn_ReadPath, self.cmb_algorithm)
        MainWindow.setTabOrder(self.cmb_algorithm, self.txt_PathShow_2)
        MainWindow.setTabOrder(self.txt_PathShow_2, self.btn_ReadPath_2)
        MainWindow.setTabOrder(self.btn_ReadPath_2, self.cmb_algorithm_2)

        self.algorithm = Algorithm()

        # 变量
        self.img = None
        self.img2 = None
        self.img_cp = None
        self.img_cp2 = None

        self.file_path = None
        self.file_path2 = None

        self.flag_thresholdVal = False
        self.flag_thresholdMax = False

        self.flag_AdapterThresholdVal = False
        # 添加事件
        self.btn_ReadPath.clicked.connect(self.btn_ReadPath_clicked)
        self.btn_ReadPath_2.clicked.connect(self.btn_ReadPath_2_clicked)

        self.btn_procressimg.clicked.connect(self.btn_procressimg_clicked)
        self.btn_procressimg_2.clicked.connect(self.btn_procressimg_2_clicked)
        # 读取算法
        import json
        file_json = os.path.join(BASE_DIR, 'db', 'algorithm1.json')
        with open(file_json, mode='r', encoding='utf-8') as f:
            data = f.read()
        self.data_list = json.loads(data)
        for idx, lista in enumerate(self.data_list.keys()):
            self.cmb_algorithm.addItem(lista)
            self.cmb_algorithm_2.addItem(lista)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "读取图片"))
        self.btn_ReadPath.setText(_translate("MainWindow", "加载图像"))
        self.label1.setText(_translate("MainWindow", "算法选择:"))
        self.btn_procressimg.setText(_translate("MainWindow", "处理"))
        self.groupBox_2.setTitle(_translate("MainWindow", "读取图片"))
        self.btn_ReadPath_2.setText(_translate("MainWindow", "加载图像"))
        self.label1_2.setText(_translate("MainWindow", "算法选择:"))
        self.btn_procressimg_2.setText(_translate("MainWindow", "处理"))
        self.lab_showImg_2.setText(_translate("MainWindow", "TextLabel"))
        self.lab_showImg.setText(_translate("MainWindow", "TextLabel"))
    def call_algorithm(self,cmd_type,params = None):
        if cmd_type  not in self.algorithm.cmd_algorithm:
            QMessageBox.warning(None,'错误','指令错误！')
            return
        return self.algorithm.cmd_algorithm[cmd_type](params)
    def btn_ReadPath_clicked(self):
        '''
        按钮事件
        读取图像文件路径
        :return:
        '''
        file_path = self.read_filepath()
        if file_path == "" or file_path is None:
            return
        if file_path.endswith('jpg') or file_path.endswith('png') or file_path.endswith('bmp'):
            if self.is_contains_chinese(file_path):
                QMessageBox.warning(None, '错误', "路径中含有中文字符")
                return
            self.txt_PathShow.setText('{}'.format(file_path))
            self.file_path = file_path
        else:
            QMessageBox.warning(None, "错误", "请选择图片文件")
            return
        # 读取图像
        self.img = cv2.imread(self.file_path)
        # 图片转化
        self.show_img(False, self.img, self.lab_showImg,self.scrollAreaWidgetContents)
    def btn_ReadPath_2_clicked(self):
        '''
        按钮事件
        读取图像文件路径
        :return:
        '''
        file_path = self.read_filepath()
        if file_path == "" or file_path is None:
            return
        if file_path.endswith('jpg') or file_path.endswith('png') or file_path.endswith('bmp'):
            if self.is_contains_chinese(file_path):
                QMessageBox.warning(None, '错误', "路径中含有中文字符")
                return
            self.txt_PathShow_2.setText('{}'.format(file_path))
            self.file_path2 = file_path
        else:
            QMessageBox.warning(None, "错误", "请选择图片文件")
            return
        # 读取图像
        self.img2 = cv2.imread(self.file_path2)
        # 图片转化
        self.show_img(False, self.img2, self.lab_showImg_2,self.scrollAreaWidgetContents2)

    def btn_procressimg_clicked(self):
        #获取当前选中算法
        str_algorithm = self.cmb_algorithm.currentText()
        if self.file_path == '' or self.img is None:
            return
        #深度复制图像
        self.img_cp = deepcopy(self.img)
        self.alg_num = self.data_list[str_algorithm]
        if self.alg_num in range(1,8):
            isgray,show_img  = self.call_algorithm(self.alg_num,self.img_cp)
            if show_img is not None:
                self.show_img(isgray, show_img, self.lab_showImg, self.scrollAreaWidgetContents)
        if self.alg_num in [8,9,10,11,12,17,18]:
            if self.file_path2 == '' or self.img2 is None:
                QMessageBox.warning(None,'错误','请加载另一个图像！')
                return
            isgray, show_img = self.call_algorithm(self.alg_num, (self.img_cp,self.img2))
            if show_img is not None:
                self.show_img(isgray, show_img, self.lab_showImg, self.scrollAreaWidgetContents)
        if self.alg_num in [14,15,16,20]:
            self.openDialog(str_algorithm)
    def btn_procressimg_2_clicked(self):
        pass

    def show_img(self,gray, img, console,consol_scrollarea):
        '''
        图片显示
        :param gray: 是否是灰度 是True否False
        :param img: 图片
        :param console: 显示图片控件
        :return:
        '''
        if gray:
            frame = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.strides[0],
                                 QtGui.QImage.Format_Indexed8)
        else:
            frame = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.strides[0],
                             QtGui.QImage.Format_BGR888)
        pix = QtGui.QPixmap.fromImage(frame)
        console.setPixmap(pix)
        console.setGeometry(0, 0, img.shape[1], img.shape[0])
        consol_scrollarea.setGeometry(0, 0, img.shape[1], img.shape[0])
        #console.setScaledContents(True)
        #console.update()
    def openDialog(self,algorithm):
        '''
        弹出对话框
        :param algorithm: 算法类别
        :return:
        '''
        if algorithm == 'Threshold':
            self.dialog = Ui_ThresholdWindow.Ui_ThresholdWindow()
            self.dialog.setWindowModality(Qt.ApplicationModal)
            self.dialog.Signal_OneParameter.connect(self.thresholdValchange)
            #dialog.exec_()
            self.dialog.show()
        if algorithm == "AdapterThreshold":
            self.dialog = Ui_AdapterThresholdWindow.Ui_AdapterThresholdWindow()
            self.dialog.setWindowModality(Qt.ApplicationModal)
            self.dialog.Signal_AdapterThreshold_Parameter.connect(self.AdapterthresholdValchange)
            # dialog.exec_()
            self.dialog.show()
        if algorithm =="LUT":
            self.widget = Ui_LUTWindow.Ui_LUTWindow()
            self.widget.setWindowModality(Qt.ApplicationModal)
            self.widget.Signal_LUT_Parameter.connect(self.LUTValchange)
            self.widget.show()
        if algorithm =='Flip':
            self.dialog = Ui_FlipWindow.Ui_FlipWindow()
            self.dialog.setWindowModality(Qt.ApplicationModal)
            self.dialog.Signal_flipcode.connect(self.FlipCodeValchange)
            # dialog.exec_()
            self.dialog.show()
    def thresholdValchange(self,val,max,flag):
        if self.flag_thresholdVal == False:
            self.flag_thresholdVal = True
            return
        algorithm = Algorithm()
        thre_img = algorithm.Threshold(self.img_cp,val,max,flag)
        if thre_img is not None:
            if flag == 8 or flag ==16:
                self.show_img(True,thre_img,self.lab_showImg,self.scrollAreaWidgetContents)
            else:
                self.show_img(False,thre_img,self.lab_showImg,self.scrollAreaWidgetContents)
    def AdapterthresholdValchange(self,method,type,blocksize):
        # if self.flag_AdapterThresholdVal == False:
        #     self.flag_AdapterThresholdVal = True
        #     return
        algorithm = Algorithm()
        thre_img = algorithm.AdapterThreshold(self.img_cp,method,type,blocksize)
        if thre_img is not None:
            self.show_img(True, thre_img, self.lab_showImg,self.scrollAreaWidgetContents)
    def LUTValchange(self,limit1,limit2,LUTNUM1,LUTNUM2,LUTNUM3):
        algorithm = Algorithm()
        thre_img = algorithm.LUT(self.img_cp,limit1,limit2,LUTNUM1,LUTNUM2,LUTNUM3)
        if thre_img is not None:
            self.show_img(True, thre_img, self.lab_showImg,self.scrollAreaWidgetContents)
    def FlipCodeValchange(self,code):
        if code == 2:
            self.show_img(False, self.img_cp, self.lab_showImg,self.scrollAreaWidgetContents)
            return
        algorithm = Algorithm()
        thre_img = algorithm.Flip(self.img_cp,code)
        if thre_img is not None:
            self.show_img(False, thre_img, self.lab_showImg,self.scrollAreaWidgetContents)
    def is_contains_chinese(self, strs):
        '''
        是否有中文字符
        :param strs:路径字符串
        :return:
        '''
        for _char in strs:
            if '\u4e00' <= _char <= '\u9fa5':
                return True
        return False
    def read_filepath(self):
        '''
        读取文件
        :return:文件路径
        '''
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            filetypes=[('png', '*.png'), ('jpg', '*.jpg'), ('bmp', '*.bmp'), ('所有文件', '*.*')])
        if file_path == '' or file_path == None:
            QMessageBox.warning(None, "错误", "请选择图片文件")
            return
        return file_path

class Algorithm(object):
    def __init__(self):
        self.cmd_algorithm = {alg.Bgr2Gray: self.Bgr2Gray,
                              alg.Bgr2YUV: self.Bgr2YUV,
                              alg.Bgr2HSV: self.Bgr2HSV,
                              alg.Bgr2Lab: self.Bgr2Lab,
                              alg.MinMaxLoc: self.MinMaxLoc,
                              alg.Mean: self.Mean,
                              alg.MeanstdDev: self.MeanstdDev,
                              alg.Max: self.Max,
                              alg.Min: self.Min,
                              alg.bitwise_and: self.bitwise_and,
                              alg.bitwise_or: self.bitwise_or,
                              alg.bitwise_xor: self.bitwise_xor,
                              alg.bitwise_not: self.bitwise_not,
                              alg.Threshold: self.Threshold,
                              alg.AdapterThreshold: self.AdapterThreshold,
                              alg.LUT: self.LUT,
                              alg.Vconcat:self.Vconcat,
                              alg.Hconcat:self.Hconcat,
                              alg.Flip: self.Flip,

                              }
    def Bgr2Gray(self, rec_img):
        '''
        彩色图转化为灰度图
        :param rec_img: 图像
        :return: 处理后的图像
        '''
        try:
            if len(rec_img.shape) == 2:
                return
            gray =  cv2.cvtColor(rec_img, cv2.COLOR_BGR2GRAY)
            return True,gray
        except Exception as e:
            QMessageBox.warning(None, "错误", "{e}".format(str(e)))
            return
    def Bgr2YUV(self, rec_img):
        '''
        彩色图转化为YUV
        :param rec_img: 图像
        :return: 处理后的图像
        '''
        try:
            yuv = cv2.cvtColor(rec_img,cv2.COLOR_RGB2YUV)
            y,u,v = cv2.split(yuv)
            cv2.imshow('y',y)
            cv2.imshow('u',u)
            cv2.imshow('v',v)
            return False,yuv
        except Exception as e:
            QMessageBox.warning(None, "错误", "{e}".format(str(e)))
            return
    def Bgr2HSV(self, rec_img):
        '''
        彩色图转化为HSV
        :param rec_img: 图像
        :return: 处理后的图像
        '''
        try:
            hsv =  cv2.cvtColor(rec_img, cv2.COLOR_BGR2HSV)
            h,s,v = cv2.split(hsv)
            cv2.imshow('h',h)
            cv2.imshow('s',s)
            cv2.imshow('v',v)
            return False,hsv
        except Exception as e:
            QMessageBox.warning(None, "错误", "{e}".format(str(e)))
            return
    def Bgr2Lab(self, rec_img):
        '''
        彩色图转化为Lab
        :param rec_img: 图像
        :return: 处理后的图像
        '''
        try:
            lab = cv2.cvtColor(rec_img, cv2.COLOR_BGR2LAB)
            l,a,b = cv2.split(lab)
            cv2.imshow('l',l)
            cv2.imshow('a',a)
            cv2.imshow('b',b)
            return False,lab
        except Exception as e:
            QMessageBox.warning(None, "错误", "{e}".format(str(e)))
            return
    def MinMaxLoc(self,rec_img):
        '''
        获取最大最小値
        :param rec_img: 图像
        :return:处理后的图像
        '''
        try:
            img = rec_img.reshape((1,-1))
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img)
            cv2.putText(rec_img,'minVal{}'.format(min_val,3),(0,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(rec_img,'maxVal{}'.format(max_val,3),(0,60),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(rec_img,'minVallLoc{}'.format(min_loc,3),(0,90),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(rec_img,'maxValLoc{}'.format(max_loc,3),(0,120),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            return False,rec_img
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def Mean(self,rec_img):
        '''
        图像平均值
        :param rec_img: 图像
        :return: 处理后的图像
        '''
        try:
            mean = cv2.mean(rec_img)
            mean1 = mean[0]
            mean2 = mean[1]
            mean3 = mean[2]
            cv2.putText(rec_img,'Channel1Mean{}'.format(round(mean1,3)),(0,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(rec_img,'Channel2Mean{}'.format(round(mean2,3)),(0,60),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(rec_img,'Channel3Mean{}'.format(round(mean3,3)),(0,90),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            return False, rec_img
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def MeanstdDev(self,rec_img):
        '''
        图像均值标准差
        :param rec_img: 图像
        :return: 处理后的图像
        '''
        try:
            mean, stddev = cv2.meanStdDev(rec_img)
            mean1 = mean[0]
            mean2 = mean[1]
            mean3 = mean[2]
            stddev1 = stddev[0]
            stddev2 = stddev[1]
            stddev3 = stddev[2]
            cv2.putText(rec_img,'Channel1Mean{}'.format(round(float(mean1),3)),(0,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(rec_img,'Channel2Mean{}'.format(round(float(mean2),3)),(0,60),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(rec_img,'Channel3Mean{}'.format(round(float(mean3),3)),(0,90),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(rec_img,'Channel1StdDev{}'.format(stddev1),(0,120),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(rec_img,'Channel2StdDev{}'.format(stddev2),(0,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(rec_img,'Channel3StdDev{}'.format(stddev3),(0,180),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            return False,rec_img
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def Max(self,params):
        '''
        两图像最大值
        :param rec_img1:图像1
        :param rec_img2:图像2
        :return:返回最大图像
        '''
        try:
            rec_img1, rec_img2 = params
            if rec_img1.shape != rec_img2.shape:
                if rec_img1.shape > rec_img2.shape:
                    rec_img1 = cv2.resize(rec_img1, (rec_img2.shape[1], rec_img2.shape[0]), cv2.INTER_AREA)
                else:
                    rec_img2 = cv2.resize(rec_img2, (rec_img1.shape[1], rec_img1.shape[0]), cv2.INTER_AREA)
            max = cv2.max(rec_img1, rec_img2)
            return False,max
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def Min(self,params):
        '''
        两图像最小値
        :param rec_img1:图像1
        :param rec_img2:图像2
        :return:返回最小图像
        '''
        try:
            rec_img1, rec_img2 = params
            if rec_img1.shape != rec_img2.shape:
                if rec_img1.shape > rec_img2.shape:
                    rec_img1 = cv2.resize(rec_img1, (rec_img2.shape[1], rec_img2.shape[0]), cv2.INTER_AREA)
                else:
                    rec_img2 = cv2.resize(rec_img2, (rec_img1.shape[1], rec_img1.shape[0]), cv2.INTER_AREA)
            min =  cv2.min(rec_img1, rec_img2)
            return False,min
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def bitwise_and(self,params):
        '''
        两图像位进进行与操位
        :param rec_img1:图像1
        :param rec_img2:图像2
        :return:返回两图像位与操作结果
        '''
        try:
            rec_img1,rec_img2 = params
            if rec_img1.shape != rec_img2.shape:
                if rec_img1.shape > rec_img2.shape:
                    rec_img1 = cv2.resize(rec_img1, (rec_img2.shape[1], rec_img2.shape[0]), cv2.INTER_AREA)
                else:
                    rec_img2 = cv2.resize(rec_img2, (rec_img1.shape[1], rec_img1.shape[0]), cv2.INTER_AREA)
            bit_and =  cv2.bitwise_and(rec_img1, rec_img2)
            return False,bit_and
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def bitwise_or(self,params):
        '''
        两图像位进进行或操位params
        :param rec_img1:图像1
        :param rec_img2:图像2
        :return:返回两图像位或操�结果
        '''
        try:
            rec_img1, rec_img2 = params
            if rec_img1.shape != rec_img2.shape:
                if rec_img1.shape > rec_img2.shape:
                    rec_img1 = cv2.resize(rec_img1, (rec_img2.shape[1], rec_img2.shape[0]), cv2.INTER_AREA)
                else:
                    rec_img2 = cv2.resize(rec_img2, (rec_img1.shape[1], rec_img1.shape[0]), cv2.INTER_AREA)
            bit_or =  cv2.bitwise_or(rec_img1, rec_img2)
            return False,bit_or
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def bitwise_xor(self,params):
        '''
        两图像位进进行差操位
        :param rec_img1:图像1
        :param rec_img2:图像2
        :return:返回两图像位差操�结果
        '''
        try:
            rec_img1, rec_img2 = params
            if rec_img1.shape != rec_img2.shape:
                if rec_img1.shape > rec_img2.shape:
                    rec_img1 = cv2.resize(rec_img1, (rec_img2.shape[1], rec_img2.shape[0]), cv2.INTER_AREA)
                else:
                    rec_img2 = cv2.resize(rec_img2, (rec_img1.shape[1], rec_img1.shape[0]), cv2.INTER_AREA)
            bit_xor =cv2.bitwise_xor(rec_img1, rec_img2)
            return False,bit_xor
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def bitwise_not(self,rec_img):
        '''
        两图像位进进行取反操位
        :param rec_img:图像
        :return:返回图像取反结果
        '''
        try:
            bit_not =cv2.bitwise_not(rec_img)
            return False,bit_not
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def Threshold(self,rec_img,thresh,maxval,type = 0):
        '''
        两图像位进进行阈値操位
        :param rec_img:图像
        :param thresh:阈値
        :param maxval:最大値
        :param type:二值化可选标志
        :return:返回图像阈値操位结果
        '''
        try:
            if type == 8 :
                rec_img = cv2.cvtColor(rec_img, cv2.COLOR_BGR2GRAY)
                num, thre_img = cv2.threshold(rec_img, thresh, maxval, 0|8)
            elif type ==16 :
                rec_img = cv2.cvtColor(rec_img, cv2.COLOR_BGR2GRAY)
                num, thre_img = cv2.threshold(rec_img, thresh, maxval, 0|16)
            else:
                _,thre_img  = cv2.threshold(rec_img, thresh, maxval,type)
            return thre_img
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def AdapterThreshold(self,rec_img,thresholdmethod,thresholdtype,blockSize):
        try:
            if len(rec_img.shape) == 3:
                rec_img = cv2.cvtColor(rec_img, cv2.COLOR_BGR2GRAY)
            #thre_img = cv2.adaptiveThreshold(rec_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,thresholdtype,c)
            thre_img = cv2.adaptiveThreshold(rec_img,255,thresholdmethod,thresholdtype,blockSize,0)
            return thre_img
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def LUT(self,rec_img,limit1,limit2,lutnum1,lutnum2,lutnum3):
        '''
        LUT功能，将图像根据表格映射
        :param rec_img: 需要映射的图像
        :param limit1: 映射范围一的值,范围一 = {0 : limit1}
        :param limit2: 映射范围二的值,范围二 = {limit2 : limit1}
        :param lutnum1: 映射值一,在范围一内的灰度值变为lutnum1
        :param lutnum2: 映射值二,在范围二内的灰度值变为lutnum2
        :param lutnum3: 映射值三,在{limit2:255}范围内的灰度值变为lutnum3
        :return:返回映射后的图像
        '''
        try:
            if len(rec_img.shape) == 3:
                rec_img = cv2.cvtColor(rec_img, cv2.COLOR_BGR2GRAY)
            LUT_img = np.zeros(256,np.uint8)
            LUT_img[0:limit1] = lutnum1
            LUT_img[limit1:limit2] = lutnum2
            LUT_img[limit2:] = lutnum3
            lut_img = cv2.LUT(rec_img,LUT_img)
            return lut_img
        except Exception as e:
            QMessageBox.warning(None, "错误", "{}".format(str(e)))
            return
    def Vconcat(self,params):
        '''
        垂直拼接
        :param rec_img1: 图像1
        :param rec_img2: 图像2
        :return: 拼接后的图像
        '''
        try:
            rec_img1,rec_img2 = params
            if len(rec_img1.shape) == 3 and len(rec_img2.shape) == 3:
                vconcat = cv2.vconcat([rec_img1, cv2.resize(rec_img2, (rec_img1.shape[1], rec_img2.shape[0]))])
                return False, vconcat
            else:
                if len(rec_img1.shape) == 3:
                    rec_img1 = cv2.cvtColor(rec_img1,cv2.COLOR_BGR2GRAY)
                elif len(rec_img2.shape) == 3:
                    rec_img2 = cv2.cvtColor(rec_img2,cv2.COLOR_BGR2GRAY)
                vconcat =  cv2.vconcat([rec_img1,cv2.resize(rec_img2,(rec_img1.shape[1],rec_img2.shape[0]))])
                return False,vconcat
        except Exception as ex:
            QMessageBox.warning(None,"错误",'{}'.format(str(ex)))
    def Hconcat(self,params):
        '''
        水平拼接
        :param rec_img1: 图像1
        :param rec_img2: 图像2
        :return: 拼接后的图像
        '''
        try:
            rec_img1,rec_img2 = params
            if len(rec_img1.shape) == 3 and len(rec_img2.shape) == 3:
                hconcat = cv2.hconcat([rec_img1, cv2.resize(rec_img2, (rec_img2.shape[1], rec_img1.shape[0]))])
                return False, hconcat
            else:
                if len(rec_img1.shape) == 3:
                    rec_img1 = cv2.cvtColor(rec_img1,cv2.COLOR_BGR2GRAY)
                elif len(rec_img2.shape) == 3:
                    rec_img2 = cv2.cvtColor(rec_img2,cv2.COLOR_BGR2GRAY)
                hconcat =  cv2.hconcat([rec_img1,cv2.resize(rec_img2,(rec_img2.shape[1],rec_img1.shape[0]))])
                return False,hconcat
        except Exception as ex:
            QMessageBox.warning(None,"错误",'{}'.format(str(ex)))
    def Flip(self,rec_img,flipCode):
        '''
        图像翻转
        :param rec_img: 需要翻转的图像
        :param flipCode: 翻过标志 >0:绕Y旋转   =0:绕X旋转 <0:两条轴都翻转
        :return: 翻过气后的图像
        '''
        try:
            return cv2.flip(rec_img,flipCode)
        except Exception as ex:
            QMessageBox.warning(None,"错误",'{}'.format(str(ex)))