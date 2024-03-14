from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from rumus.belahketupat import Belahketupat

class BelahketupatForm(QDialog):
    def __init__(self,parent=None):
        super(BelahketupatForm,self).__init__(parent)
        loadUi('C:/uas/view/belahketupat.ui',self)
        self.btnHitung.clicked.connect(self.hitungdata)
        self.btnKeluar.clicked.connect(self.keluar)
    
    
    def hitungdata(self):
        try:
            d1 = float(self.txtd1.text())
            d2 = float(self.txtd2.text())
            sisi = float(self.txtSisi.text())
           
            belahketupat = Belahketupat(d1,d2,sisi)
            belahketupat.hitung()
            
            self.txtLuas.setText(f'{belahketupat.luas}')
            self.txtKeliling.setText(f'{belahketupat.keliling}')
            
        except ValueError:
            QMessageBox.warning(self, 'Error', 'masukkan nilai')
    
    def keluar(self):
        self.close()