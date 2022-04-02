# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instaloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 344)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 130, 181, 106))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_download_post = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rb_download_post.setObjectName("rb_download_post")
        self.verticalLayout.addWidget(self.rb_download_post)
        self.rb_download_profile = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rb_download_profile.setObjectName("rb_download_profile")
        self.verticalLayout.addWidget(self.rb_download_profile)
        self.rb_update_profile = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rb_update_profile.setObjectName("rb_update_profile")
        self.verticalLayout.addWidget(self.rb_update_profile)
        self.rb_download_top_x_posts = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rb_download_top_x_posts.setObjectName("rb_download_top_x_posts")
        self.verticalLayout.addWidget(self.rb_download_top_x_posts)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 130, 192, 146))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_save_metadata = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_save_metadata.setObjectName("cb_save_metadata")
        self.verticalLayout_2.addWidget(self.cb_save_metadata)
        self.cb_post_metadata_txt_patternx = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_post_metadata_txt_patternx.setObjectName("cb_post_metadata_txt_patternx")
        self.verticalLayout_2.addWidget(self.cb_post_metadata_txt_patternx)
        self.cb_download_geotags = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_download_geotags.setObjectName("cb_download_geotags")
        self.verticalLayout_2.addWidget(self.cb_download_geotags)
        self.cb_download_comments = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_download_comments.setObjectName("cb_download_comments")
        self.verticalLayout_2.addWidget(self.cb_download_comments)
        self.cb_no_pics = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_no_pics.setObjectName("cb_no_pics")
        self.verticalLayout_2.addWidget(self.cb_no_pics)
        self.cb_no_videos = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_no_videos.setObjectName("cb_no_videos")
        self.verticalLayout_2.addWidget(self.cb_no_videos)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 471, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.past_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.past_btn.setObjectName("past_btn")
        self.horizontalLayout.addWidget(self.past_btn)
        self.le_go_btn = QtWidgets.QPushButton(self.centralwidget)
        self.le_go_btn.setGeometry(QtCore.QRect(70, 290, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.le_go_btn.setFont(font)
        self.le_go_btn.setCheckable(False)
        self.le_go_btn.setChecked(False)
        self.le_go_btn.setObjectName("le_go_btn")
        self.set_dir_btn = QtWidgets.QPushButton(self.centralwidget)
        self.set_dir_btn.setGeometry(QtCore.QRect(10, 60, 101, 32))
        self.set_dir_btn.setObjectName("set_dir_btn")
        self.label_dir = QtWidgets.QLabel(self.centralwidget)
        self.label_dir.setGeometry(QtCore.QRect(20, 90, 469, 30))
        self.label_dir.setText("")
        self.label_dir.setObjectName("label_dir")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(5, 110, 500, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(5, 0, 471, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_login.setFont(font)
        self.label_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_login.setStyleSheet("color: rgb(0, 209, 0)")
        self.label_login.setText("")
        self.label_login.setObjectName("label_login")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rb_download_post.setText(_translate("MainWindow", "download_post"))
        self.rb_download_profile.setText(_translate("MainWindow", "download_profile"))
        self.rb_update_profile.setText(_translate("MainWindow", "update_profile"))
        self.rb_download_top_x_posts.setText(_translate("MainWindow", "download_top_x_posts"))
        self.cb_save_metadata.setText(_translate("MainWindow", "save_metadata"))
        self.cb_post_metadata_txt_patternx.setText(_translate("MainWindow", "post_metadata_txt_pattern"))
        self.cb_download_geotags.setText(_translate("MainWindow", "download_geotags"))
        self.cb_download_comments.setText(_translate("MainWindow", "download_comments"))
        self.cb_no_pics.setText(_translate("MainWindow", "no_pics"))
        self.cb_no_videos.setText(_translate("MainWindow", "no_videos"))
        self.label.setText(_translate("MainWindow", "URL: "))
        self.past_btn.setText(_translate("MainWindow", "past"))
        self.le_go_btn.setText(_translate("MainWindow", "LE  GO"))
        self.set_dir_btn.setText(_translate("MainWindow", "set_dir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
