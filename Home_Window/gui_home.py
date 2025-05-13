import sys
from PIL import Image

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from PySide6.QtWidgets import QFileDialog

from Home_Window.UI.home_window import Ui_MainWindow
from Home_Window.utils import pil2pixmap

class GuiHome(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.input_image_path = ""
        self.pb_browse_image.clicked.connect(self.browse_image)

    @qtc.Slot()
    def browse_image(self):

        self.input_image_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select an Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.tif)"
        )

        if self.input_image_path:
            try:
                pil_image = Image.open(self.input_image_path)
                pixmap = pil2pixmap(pil_image)

                self.lb_input_image.setPixmap(
                    pixmap.scaled(
                        self.lb_input_image.size()
                    )
                )
            except Exception as e:
                self.lb_input_image.setText("Unable to load image.")



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = GuiHome()
    window.show()
    sys.exit(app.exec())