import sys
from  PyQt5 import QtCore,QtGui,QtWidgets
import QtTest

if __name__ == '__main__':
    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    #调用自定义的界面
    ui = QtTest.Ui_MainWindow()
    ui.setupUi(MainWindow)

    #显示窗体并释放资源
    MainWindow.show()
    sys.exit(app.exec_())