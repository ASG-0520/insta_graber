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
        MainWindow.resize(608, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(12, -1, -1, -1)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)
        self.label_login = QtWidgets.QLabel(self.centralwidget)
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
        self.horizontalLayout.addWidget(self.label_login)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.login_from_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_from_file_btn.setObjectName("login_from_file_btn")
        self.horizontalLayout.addWidget(self.login_from_file_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(12, -1, 0, -1)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.past_btn = QtWidgets.QPushButton(self.centralwidget)
        self.past_btn.setObjectName("past_btn")
        self.horizontalLayout_4.addWidget(self.past_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.set_dir_btn = QtWidgets.QPushButton(self.centralwidget)
        self.set_dir_btn.setObjectName("set_dir_btn")
        self.horizontalLayout_2.addWidget(self.set_dir_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(12, 0, -1, -1)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_dir = QtWidgets.QLabel(self.centralwidget)
        self.label_dir.setText("")
        self.label_dir.setObjectName("label_dir")
        self.horizontalLayout_5.addWidget(self.label_dir)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.open_dir_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_dir_btn.setObjectName("open_dir_btn")
        self.horizontalLayout_5.addWidget(self.open_dir_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(50, 12, 50, 20)
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(12, 0, -1, 40)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_download_post = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_download_post.setCheckable(True)
        self.rb_download_post.setChecked(False)
        self.rb_download_post.setObjectName("rb_download_post")
        self.verticalLayout.addWidget(self.rb_download_post)
        self.rb_download_profile = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_download_profile.setObjectName("rb_download_profile")
        self.verticalLayout.addWidget(self.rb_download_profile)
        self.rb_update_profile = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_update_profile.setObjectName("rb_update_profile")
        self.verticalLayout.addWidget(self.rb_update_profile)
        self.rb_download_top_x_posts = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_download_top_x_posts.setEnabled(False)
        self.rb_download_top_x_posts.setObjectName("rb_download_top_x_posts")
        self.verticalLayout.addWidget(self.rb_download_top_x_posts)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_save_metadata = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_save_metadata.setObjectName("cb_save_metadata")
        self.verticalLayout_2.addWidget(self.cb_save_metadata)
        self.cb_post_metadata_txt_patternx = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_post_metadata_txt_patternx.setObjectName("cb_post_metadata_txt_patternx")
        self.verticalLayout_2.addWidget(self.cb_post_metadata_txt_patternx)
        self.cb_download_geotags = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_download_geotags.setObjectName("cb_download_geotags")
        self.verticalLayout_2.addWidget(self.cb_download_geotags)
        self.cb_download_comments = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_download_comments.setObjectName("cb_download_comments")
        self.verticalLayout_2.addWidget(self.cb_download_comments)
        self.cb_no_pics = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_no_pics.setObjectName("cb_no_pics")
        self.verticalLayout_2.addWidget(self.cb_no_pics)
        self.cb_no_videos = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_no_videos.setObjectName("cb_no_videos")
        self.verticalLayout_2.addWidget(self.cb_no_videos)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(12, -1, 12, 0)
        self.gridLayout.setHorizontalSpacing(18)
        self.gridLayout.setVerticalSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        self.exit_bn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.exit_bn.setFont(font)
        self.exit_bn.setObjectName("exit_bn")
        self.gridLayout.addWidget(self.exit_bn, 0, 2, 1, 1)
        self.le_go_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.le_go_btn.setFont(font)
        self.le_go_btn.setCheckable(False)
        self.le_go_btn.setChecked(False)
        self.le_go_btn.setObjectName("le_go_btn")
        self.gridLayout.addWidget(self.le_go_btn, 0, 0, 1, 2)
        self.verticalLayout_10.addLayout(self.gridLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.verticalLayout_10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "InstaGrabber"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.login_from_file_btn.setText(_translate("MainWindow", "Login from file"))
        self.label.setText(_translate("MainWindow", "URL: "))
        self.past_btn.setText(_translate("MainWindow", "past"))
        self.set_dir_btn.setText(_translate("MainWindow", "set directory"))
        self.open_dir_btn.setText(_translate("MainWindow", "open dir"))
        self.rb_download_post.setText(_translate("MainWindow", "download post"))
        self.rb_download_profile.setText(_translate("MainWindow", "download profile"))
        self.rb_update_profile.setText(_translate("MainWindow", "update profile"))
        self.rb_download_top_x_posts.setText(_translate("MainWindow", "download_top_x_posts"))
        self.cb_save_metadata.setText(_translate("MainWindow", "save metadata"))
        self.cb_post_metadata_txt_patternx.setText(_translate("MainWindow", "post metadata txt pattern"))
        self.cb_download_geotags.setText(_translate("MainWindow", "download geotags"))
        self.cb_download_comments.setText(_translate("MainWindow", "download comments"))
        self.cb_no_pics.setText(_translate("MainWindow", "no pics"))
        self.cb_no_videos.setText(_translate("MainWindow", "no videos"))
        self.exit_bn.setText(_translate("MainWindow", "Exit"))
        self.le_go_btn.setText(_translate("MainWindow", "LE  GO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
