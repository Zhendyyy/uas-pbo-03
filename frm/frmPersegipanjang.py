from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from rumus.persegipanjang import Persegipanjang

class PersegipanjangForm(QDialog):
    def __init__(self,parent=None):
        super(PersegipanjangForm,self).__init__(parent)
        loadUi('C:/uas/view/persegipanjang.ui',self)
        self.btnHitung.clicked.connect(self.hitungdata)
        self.btnKeluar.clicked.connect(self.keluar)
    
    
    def hitungdata(self):
        try:
            panjang = float(self.txtPanjang.text())
            lebar = float(self.txtLebar.text())
            
            persegipanjang = Persegipanjang(panjang, lebar)
            persegipanjang.hitung()
            
            self.txtLuas.setText(f'{persegipanjang.luas}')
            self.txtKeliling.setText(f'{persegipanjang.keliling}')
            # self.TampilData()
            
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Masukkan nilai untuk panjang dan lebar')
    
    def keluar(self):
        self.close()