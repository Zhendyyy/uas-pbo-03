from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from rumus.lingkaran import Lingkaran

class LingkaranForm(QDialog):
    def __init__(self,parent=None):
        super(LingkaranForm,self).__init__(parent)
        loadUi('C:/uas/view/lingkaran.ui',self)
        self.btnHitung.clicked.connect(self.hitungdata)
        self.btnKeluar.clicked.connect(self.keluar)
    
    
    def hitungdata(self):
        try:
            jari = float(self.txtJ1.text())
          
            lingkaran = Lingkaran(jari)
            lingkaran.hitung()
            
            self.txtLuas.setText(f'{lingkaran.luas}')
            self.txtKeliling.setText(f'{lingkaran.keliling}')
            
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Masukkan nilai')
    
    def keluar(self):
        self.close()