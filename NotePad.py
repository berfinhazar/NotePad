import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog,
    QMessageBox, QFontDialog
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Not Defteri (Windows)")
        self.setGeometry(200, 100, 900, 600)

        self.text_area = QTextEdit()
        self.setCentralWidget(self.text_area)

        self._create_menu_bar()

    def _create_menu_bar(self):
        menu_bar = self.menuBar()

        # --- DOSYA ---
        file_menu = menu_bar.addMenu("Dosya")

        new_action = QAction("Yeni", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction("Aç", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Kaydet", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)


        edit_menu = menu_bar.addMenu("Düzen")

        cut_action = QAction("Kes", self)
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(self.text_area.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction("Kopyala", self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.text_area.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Yapıştır", self)
        paste_action.setShortcut("Ctrl+V")
        paste_action.triggered.connect(self.text_area.paste)
        edit_menu.addAction(paste_action)

        # --- BİÇİM ---
        format_menu = menu_bar.addMenu("Biçim")

        font_action = QAction("Yazı Tipini Değiştir", self)
        font_action.triggered.connect(self.change_font)
        format_menu.addAction(font_action)


        help_menu = menu_bar.addMenu("Yardım")

        about_action = QAction("Hakkında", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)



    def new_file(self):
        self.text_area.clear()

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Metin Dosyaları (*.txt)")
        if path:
            with open(path, 'r', encoding='utf-8') as file:
                self.text_area.setText(file.read())

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Dosya Kaydet", "", "Metin Dosyaları (*.txt)")
        if path:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(self.text_area.toPlainText())
            QMessageBox.information(self, "Kaydedildi", "Dosya başarıyla kaydedildi!")

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_area.setFont(font)

    def show_about(self):
        QMessageBox.about(self, "Hakkında", "Bu basit bir Notepad uygulamasıdır.\nGeliştirici: Berfin 😊")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Notepad()
    window.show()
    sys.exit(app.exec_())
