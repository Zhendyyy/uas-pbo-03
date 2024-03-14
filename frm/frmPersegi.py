from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from rumus.persegi import Persegi

class PersegiForm(QDialog):
    def __init__(self,parent=None):
        super(PersegiForm,self).__init__(parent)
        loadUi('C:/uas/view/persegi.ui',self)
        self.btnHitung.clicked.connect(self.hitungdata)
        self.btnKeluar.clicked.connect(self.keluar)
    
    
    def hitungdata(self):
        try:
            sisi = float(self.txtSisi.text())
            persegi = Persegi(sisi)
            persegi.hitung()
            
            self.txtLuas.setText(f'{persegi.luas}')
            self.txtKeliling.setText(f'{persegi.keliling}')
            
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Masukkan nilai untuk panjang dan lebar')
    
    def keluar(self):
        self.close()