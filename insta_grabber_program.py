import insta_graber
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clipboard = QApplication.clipboard()

        self.le_go_btn.clicked.connect(lambda: self.menu())
        self.set_dir_btn.clicked.connect(self.browse_folder)
        self.past_btn.clicked.connect(self.paste_func)

    def paste_func(self):
        self.lineEdit.setText(self.clipboard.text())

    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.label_dir.setText(directory)
        insta_graber.L.dirname_pattern = directory

    def menu(self):
        # ____________________________________CheckBox:______________________________________

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

        # ____________________________________RadioButton____________________________________

        # download_post:
        if self.rb_download_post.isChecked():
            insta_graber.download_post_shortcode(self.lineEdit.text())  #
            self.label_done.setText('Done!')

        # download_profile
        elif self.rb_download_profile.isChecked():
            insta_graber.download_profile(self.lineEdit.text())  #

        # update_profile
        elif self.rb_update_profile.isChecked():
            insta_graber.download_profile(self.lineEdit.text())  #
        # ____________________________________________________________________________________


def main():
    # insta_graber.login()
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
