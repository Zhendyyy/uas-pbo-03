from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from rumus.jajargenjang import Jajargenjang

class JajargenjangForm(QDialog):
    def __init__(self,parent=None):
        super(JajargenjangForm,self).__init__(parent)
        loadUi('C:/uas/view/jajargenjang.ui',self)
        self.btnHitung.clicked.connect(self.hitungdata)
        self.btnKeluar.clicked.connect(self.keluar)
    
    
    def hitungdata(self):
        try:
            a = float(self.txtA.text())
            b = float(self.txtB.text())
            alas = float(self.txtAlas.text())
            tinggi = float(self.txtTinggi.text())
            
           
            jajargenjang = Jajargenjang(a,b,alas,tinggi)
            jajargenjang.hitung()
            
            self.txtLuas.setText(f'{jajargenjang.luas}')
            self.txtKeliling.setText(f'{jajargenjang.keliling}')
            
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Masukkan nilai ')
    
    def keluar(self):
        self.close()