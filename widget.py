# This Python file uses the following encoding: utf-8
import sys, os

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QFileDialog
from PIL import Image

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setFixedSize(1300, 750)
        self.setStyleSheet("background-color: #d9e8e6")
        self.ui.tableWidget.setStyleSheet("background-color: #ffffff")
        self.prevDir = ""
        self.prevFile = ""
        self.row = 0;

    def onButton2Clicked(self):
        fileName = QFileDialog.getOpenFileName(self, 'Choose the file: ')
        if fileName[0].lower().endswith(('.png', '.jpg', '.gif', '.tiff', '.pcx', '.bmp')):
            self.ui.label_2.setText(fileName[0])
            img = Image.open(fileName[0])
            name = QTableWidgetItem(os.path.split(fileName[0])[1])
            format = QTableWidgetItem(img.format)
            dpi = QTableWidgetItem(str(img.info.get('dpi')))
            size = QTableWidgetItem(str(img.size))
            depth = 0
            depthType = img.mode
            if depthType == "L" or depthType == "P":
                depth = 8
            elif depthType == "1":
                depth = 1
            elif depthType == "RGB" or depthType == "YCbCr" or depthType == "LAB" or depthType == "HSV":
                depth = 24
            elif depthType == "RGBA" or depthType == "CMYK" or depthType == "I" or depthType == "F":
                depth = 32
            depthItem = QTableWidgetItem(str(depth))
            compression = QTableWidgetItem(str(img.info.get('compression')))
            self.ui.tableWidget.insertRow(self.row)
            self.ui.tableWidget.setItem(self.row, 0, name)
            self.ui.tableWidget.setItem(self.row, 1, format)
            self.ui.tableWidget.setItem(self.row, 2, size)
            self.ui.tableWidget.setItem(self.row, 3, dpi)
            self.ui.tableWidget.setItem(self.row, 4, depthItem)
            self.ui.tableWidget.setItem(self.row, 5, compression)
            self.row += 1
            img.close()

    def onButtonClicked(self):
        directoryName = QFileDialog.getExistingDirectory(self, 'Enter the directory: ')
        self.ui.label_2.setText(directoryName)
        filesList = os.listdir(directoryName)
        for file in filesList:
            if file.lower().endswith(('.png', '.jpg', '.gif', '.tiff', '.pcx', '.bmp')):
                img = Image.open(directoryName + '/' + file)
                name = QTableWidgetItem(file)
                format = QTableWidgetItem(img.format)
                dpi = QTableWidgetItem(str(img.info.get('dpi')))
                size = QTableWidgetItem(str(img.size))
                depth = 0
                depthType = img.mode
                if depthType == "L" or depthType == "P":
                    depth = 8
                elif depthType == "1":
                    depth = 1
                elif depthType == "RGB" or depthType == "YCbCr" or depthType == "LAB" or depthType == "HSV":
                    depth = 24
                elif depthType == "RGBA" or depthType == "CMYK" or depthType == "I" or depthType == "F":
                    depth = 32
                depthItem = QTableWidgetItem(str(depth))
                compression = QTableWidgetItem(str(img.info.get('compression')))
                self.ui.tableWidget.insertRow(self.row)
                self.ui.tableWidget.setItem(self.row, 0, name)
                self.ui.tableWidget.setItem(self.row, 1, format)
                self.ui.tableWidget.setItem(self.row, 2, size)
                self.ui.tableWidget.setItem(self.row, 3, dpi)
                self.ui.tableWidget.setItem(self.row, 4, depthItem)
                self.ui.tableWidget.setItem(self.row, 5, compression)
                self.row += 1
                img.close()

    def onButton3Clicked(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        self.ui.label_2.setText("File/Directory Not Chosen")
        self.row = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.setWindowTitle("Images Information")
    widget.show()
    sys.exit(app.exec())
