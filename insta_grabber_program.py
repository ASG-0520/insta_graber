from set_log import s_log, s_pas
import sys
import insta_graber
import design
import instaloader
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog
from pathlib import Path
import webbrowser


class InstaGrabber(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clipboard = QApplication.clipboard()
        self.le_go_btn.clicked.connect(lambda: self.menu())
        self.set_dir_btn.clicked.connect(self.browse_folder)
        self.past_btn.clicked.connect(self.paste_func)
        self.login_btn.clicked.connect(self.login)
        self.open_dir_btn.clicked.connect(self.open_folder)
        self.login_from_file_btn.clicked.connect(self.login_from_file)

        self.label_dir.setText(str(insta_graber.d_path))
        self.label_dir.setToolTip(str(insta_graber.d_path))

    def login_from_file(self):
        if s_log and s_pas:
            try:
                print(s_log, s_pas)
                insta_graber.login(s_log, s_pas)
            except instaloader.exceptions.ConnectionException:
                print('нет подключения, проверь инет')
                self.show_popup_connection_error()
            except Exception as exception_error:
                self.show_popup(title='Error', text=str(exception_error))
            else:
                self.label_login.setText("You loged in like: " + s_log)
        else:
            self.show_popup(title="File error", text='File error', info="Check the file set_log.py",
                            ico=QMessageBox.Critical)

    def paste_func(self):
        self.lineEdit.setText(self.clipboard.text())

    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.label_dir.setText(directory)
        self.label_dir.setToolTip(directory)
        insta_graber.L.dirname_pattern = directory + '/{target}'
        print('browse_folder: ' + directory)

    def open_folder(self):
        filename = Path(self.label_dir.text())
        webbrowser.open(filename.absolute().as_uri())
        print('open_folder::  ' + str(filename))

    def menu(self):
        # ================================================================================ #
        # #################################  CheckBox:  ################################## #
        # ================================================================================ #

        # post_metadata_txt_patternx:
        if self.cb_post_metadata_txt_patternx.isChecked():
            insta_graber.L.post_metadata_txt_pattern = '{caption}'
        else:
            insta_graber.L.post_metadata_txt_pattern = ''

        # save_metadata:
        if self.cb_save_metadata.isChecked():
            insta_graber.L.save_metadata = True
        else:
            insta_graber.L.save_metadata = False

        # download_geotags:
        if self.cb_download_geotags.isChecked():
            insta_graber.L.download_geotags = True
        else:
            insta_graber.L.download_geotags = False

        # download_comments:
        if self.cb_download_comments.isChecked():
            insta_graber.L.download_comments = True
        else:
            insta_graber.L.download_comments = False

        # # download_pics:
        if self.cb_no_pics.isChecked():
            insta_graber.L.download_pictures = False
        else:
            insta_graber.L.download_pictures = True

        # download_videos:
        if self.cb_no_videos.isChecked():
            insta_graber.L.download_videos = False
        else:
            insta_graber.L.download_videos = True

        # ================================================================================ #
        # ################################  RadioButtons: ################################ #
        # ================================================================================ #

        # ================================================================================ #
        # download_post:
        # ================================================================================ #
        if self.rb_download_post.isChecked():
            try:
                insta_graber.download_post_shortcode(self.lineEdit.text())  #

            except instaloader.exceptions.LoginRequiredException:
                print('Это закрытый пост, нужно ЗАЛОГИНИТЬСЯ')
                self.show_popup_login_error()
                self.login()

            except instaloader.exceptions.ConnectionException:
                print('нет подключения, проверь инет')
                self.show_popup_connection_error()

            except IndexError:
                print("не верный адрес")
                self.show_popup_index_error()
            else:
                self.show_popup(title='Done', text='DONE ', ico=QMessageBox.Warning)

        # ================================================================================ #
        # download_profile:
        # ================================================================================ #
        elif self.rb_download_profile.isChecked():

            try:
                insta_graber.download_profile(self.lineEdit.text())

            except instaloader.exceptions.LoginRequiredException:
                print('Это закрытый пост, нужно ЗАЛОГИНИТЬСЯ')
                self.show_popup_login_error()
                self.login()

            except instaloader.exceptions.ConnectionException:
                print('нет подключения, проверь инет')
                self.show_popup_connection_error()

            except IndexError:
                print("не верный адрес")
                self.show_popup_index_error()
            else:
                self.show_popup(title='Done', text='DONE ', ico=QMessageBox.Warning)
        # ================================================================================ #
        # update_profile:
        # ================================================================================ #
        elif self.rb_update_profile.isChecked():

            try:
                insta_graber.update_profile(self.lineEdit.text())

            except instaloader.exceptions.LoginRequiredException:
                print('Это закрытый пост, нужно ЗАЛОГИНИТЬСЯ')
                self.show_popup_login_error()
                self.login()

            except instaloader.exceptions.ConnectionException:
                print('нет подключения, проверь инет')
                self.show_popup_connection_error()

            except IndexError:
                print("не верный адрес")
                self.show_popup_index_error()
            else:
                self.show_popup(title='Done', text='DONE ', ico=QMessageBox.Warning)
        # ================================================================================ #
        # download_top_x_posts
        # ================================================================================ #
        elif self.rb_download_top_x_posts.isChecked():

            try:
                insta_graber.update_profile(self.lineEdit.text())

            except instaloader.exceptions.LoginRequiredException:
                print('Это закрытый пост, нужно ЗАЛОГИНИТЬСЯ')
                self.show_popup_login_error()
                self.login()

            except instaloader.exceptions.ConnectionException:
                print('нет подключения, проверь инет')
                self.show_popup_connection_error()

            except IndexError:
                print("не верный адрес")
                self.show_popup_index_error()
            else:
                self.show_popup(title='Done', text='DONE ', ico=QMessageBox.Warning)
        # ================================================================================ #

    def show_popup_login_error(self):
        msg = QMessageBox()
        msg.setWindowTitle('login_error')
        msg.setText('This is a private post, you need to log in')
        msg.setInformativeText('Login and try again.')
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()

    def show_popup_connection_error(self):
        msg = QMessageBox()
        msg.setWindowTitle('connection_error')
        msg.setText('Connection error')
        msg.setIcon(QMessageBox.Critical)
        msg.setInformativeText('Connection aborted, check the Internet')
        x = msg.exec_()

    def show_popup_index_error(self):
        msg = QMessageBox()
        msg.setWindowTitle('index_error')
        msg.setText("URL error: ")
        msg.setIcon(QMessageBox.Critical)
        msg.setInformativeText('Requested URL is incorrect or page has been removed')
        x = msg.exec_()

    def show_popup(self, title="", text="", info="", ico=QMessageBox.Critical):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(ico)
        msg.setInformativeText(info)
        x = msg.exec_()

    def login(self):
        input_login, res_log = QInputDialog.getText(self, 'Login', 'Login')
        if res_log is True:
            input_password, res_pass = QInputDialog.getText(self, 'Password', 'Password')

        try:
            insta_graber.login(input_login, input_password)
        except instaloader.exceptions.ConnectionException:
            print('нет подключения, проверь инет')
            self.show_popup_connection_error()
        except Exception as exception_error:
            self.show_popup(title='Error', text=str(exception_error))
        else:
            self.label_login.setText("You loged in like: " + input_login[0])


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = InstaGrabber()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
