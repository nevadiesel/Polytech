'''import os
import sys
import pandas as pd
import Ui_text_edit
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class MainApplication(QtWidgets.QMainWindow, YOUR_UI_FILE.YOUR_UI_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.data = None

    def save(self):
        QFileDialog.getSaveFileName()
        
    def exit(self):
       exit()




def main():
  app = QtWidgets.QApplication(sys.argv)
  window = MainApplication()
  window.show()
  app.exec_()


if __name__ == '__main__':
  main()
'''