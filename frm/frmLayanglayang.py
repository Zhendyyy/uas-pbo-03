from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from rumus.layanglayang import Layanglayang

class LayanglayangForm(QDialog):
    def __init__(self,parent=None):
        super(LayanglayangForm,self).__init__(parent)
        loadUi('C:/uas/view/layanglayang.ui',self)
        self.btnHitung.clicked.connect(self.hitungdata)
        self.btnKeluar.clicked.connect(self.keluar)
    
    
    def hitungdata(self):
        try:
            d1 = float(self.txtd1.text())
            d2 = float(self.txtd2.text())
            panjang = float(self.txtPanjang.text())
            lebar = float(self.txtLebar.text())
           
            layanglayang = Layanglayang(d1,d2,panjang,lebar)
            layanglayang.hitung()
            
            self.txtLuas.setText(f'{ layanglayang.luas}')
            self.txtKeliling.setText(f'{ layanglayang.keliling}')
            
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Masukkan nilai')
    
    def keluar(self):
        self.close()