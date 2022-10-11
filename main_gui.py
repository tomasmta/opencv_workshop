from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
import utils


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1697, 600)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox_img_processing = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_img_processing.setGeometry(QtCore.QRect(440, 50, 481, 501))
        self.groupBox_img_processing.setObjectName("groupBox_img_processing")

        self.button_color_separation = QtWidgets.QPushButton(self.groupBox_img_processing)
        self.button_color_separation.setGeometry(QtCore.QRect(30, 40, 421, 91))
        self.button_color_separation.setObjectName("button_color_separation")

        self.button_color_transformation = QtWidgets.QPushButton(self.groupBox_img_processing)
        self.button_color_transformation.setGeometry(QtCore.QRect(30, 150, 421, 91))
        self.button_color_transformation.setObjectName("button_color_transformation")

        self.button_color_detection = QtWidgets.QPushButton(self.groupBox_img_processing)
        self.button_color_detection.setGeometry(QtCore.QRect(30, 260, 421, 91))
        self.button_color_detection.setObjectName("button_color_detection")

        self.button_blending = QtWidgets.QPushButton(self.groupBox_img_processing)
        self.button_blending.setGeometry(QtCore.QRect(30, 370, 421, 91))
        self.button_blending.setObjectName("button_blending")


        self.groupBox_img_smoothing = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_img_smoothing.setGeometry(QtCore.QRect(1040, 50, 481, 501))
        self.groupBox_img_smoothing.setObjectName("groupBox_img_smoothing")

        self.button_median_filter = QtWidgets.QPushButton(self.groupBox_img_smoothing)
        self.button_median_filter.setGeometry(QtCore.QRect(30, 300, 421, 91))
        self.button_median_filter.setObjectName("button_median_filter")

        self.button_gauss_blur = QtWidgets.QPushButton(self.groupBox_img_smoothing)
        self.button_gauss_blur.setGeometry(QtCore.QRect(30, 80, 421, 91))
        self.button_gauss_blur.setObjectName("button_gauss_blur")

        self.button_bilateral_filter = QtWidgets.QPushButton(self.groupBox_img_smoothing)
        self.button_bilateral_filter.setGeometry(QtCore.QRect(30, 190, 421, 91))
        self.button_bilateral_filter.setObjectName("button_bilateral_filter")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_img_processing.setTitle(_translate("MainWindow", "Image Processing"))
        self.button_color_separation.setText(_translate("MainWindow", "Color Separation"))
        self.button_color_transformation.setText(_translate("MainWindow", "Color Transformation"))
        self.button_color_detection.setText(_translate("MainWindow", "Color Detection"))
        self.button_blending.setText(_translate("MainWindow", "Blending"))
        self.groupBox_img_smoothing.setTitle(_translate("MainWindow", "Image Smoothing"))
        self.button_median_filter.setText(_translate("MainWindow", "Median Filter"))
        self.button_gauss_blur.setText(_translate("MainWindow", "Gaussian Blur"))
        self.button_bilateral_filter.setText(_translate("MainWindow", "Bilateral Filter"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.button_color_separation.clicked.connect(self.color_separation)

        self.button_color_transformation.clicked.connect(self.color_transformation)

        self.button_color_detection.clicked.connect(self.color_detection)

        self.button_blending.clicked.connect(self.blend_pictures)

        self.button_gauss_blur.clicked.connect(self.gaussian_blur)

        self.button_bilateral_filter.clicked.connect(self.bilateral_filter)

        self.button_median_filter.clicked.connect(self.median_filter)


    

    @QtCore.pyqtSlot()
    def browse_img(self):
        image = QtWidgets.QFileDialog.getOpenFileName(None, 'OpenFile' ,'', "Image file(*.png *.jpg *.bmp)")
        path = image[0]
        return path

    def color_separation(self):
        path = self.browse_img()
        utils.split_colors(path)
    
    def  color_transformation(self):
        path = self.browse_img()
        utils.transform_colors(path)

    def color_detection(self):
        path = self.browse_img()
        utils.detect_color(path)

    def blend_pictures(self):
        path1 = self.browse_img()
        path2 = self.browse_img()
        utils.blend(path1, path2)

    def gaussian_blur(self):
        path = self.browse_img()
        filter_type = utils.Filters(path)
        filter_type.gaussian()

    def bilateral_filter(self):
        path = self.browse_img()
        filter_type = utils.Filters(path)
        filter_type.bilateral()
    
    def median_filter(self):
        path = self.browse_img()
        filter_type = utils.Filters(path)
        filter_type.median()

 


if __name__ == "__main__":
    import sys
    app =QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
    

