import sys
import googletrans
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMessageBox, QMainWindow

class TranslateForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TranslateForm, self).__init__(parent)
        loadUi('C:/uas/view/translate.ui', self)
        self.add_languages()
        self.txt1.clear()
        self.btnClear.clicked.connect(self.clear)
        self.btnTranslate.clicked.connect(self.translate)
        
        
    def add_languages(self):
        for x in googletrans.LANGUAGES.values():
            self.cmbL1.addItem(x.capitalize())
            self.cmbL2.addItem(x.capitalize())
            
    def translate(self):
        try:
            text_1 = self.txt1.toPlainText()
            lang_1 = self.cmbL1.currentText()
            lang_2 = self.cmbL2.currentText()
            
            translator = googletrans.Translator()
            translate = translator.translate(text_1, src=lang_1, dest=lang_2)
            self.txt2.setText(translate.text)
            
        except Exception as e:
            self.error_message(e)
    
    def error_message(self, text):
        msg = QMessageBox()
        msg.setWindowTitle('Error')
        msg.setText(str(text))
        msg.exec_()
    
    def clear(self):
        self.txt1.clear()
        self.txt2.clear()