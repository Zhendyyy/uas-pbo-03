from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from rumus.segitiga import Segitiga

class SegitigaForm(QDialog):
    def __init__(self,parent=None):
        super(SegitigaForm,self).__init__(parent)
        loadUi('C:/uas/view/segitiga.ui',self)
        self.btnHitung.clicked.connect(self.hitungdata)
        self.btnKeluar.clicked.connect(self.keluar)
    
    
    def hitungdata(self):
        try:
            alas = float(self.txtAlas.text())
            tinggi = float(self.txtTinggi.text())
            lebar = float(self.txtLebar.text())
           
            segitiga = Segitiga(alas,tinggi,lebar)
            segitiga.hitung()
            
            self.txtLuas.setText(f'{segitiga.luas}')
            self.txtKeliling.setText(f'{segitiga.keliling}')
            
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Masukkan nilai untuk panjang dan lebar')
    
    def keluar(self):
        self.close()