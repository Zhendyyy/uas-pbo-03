from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from rumus.trapesium import Trapesium

class TrapesiumForm(QDialog):
    def __init__(self,parent=None):
        super(TrapesiumForm,self).__init__(parent)
        loadUi('C:/uas/view/trapesium.ui',self)
        self.btnHitung.clicked.connect(self.hitungdata)
        self.btnKeluar.clicked.connect(self.keluar)
    
    
    def hitungdata(self):
        try:
            sisi1 = float(self.txtS1.text())
            sisi2 = float(self.txtS2.text())
            sisi3 = float(self.txtS3.text())
            sisi4 = float(self.txtS4.text())
            tinggi = float(self.txtTinggi.text())
           
            trapesium = Trapesium(sisi1,sisi2,sisi3,sisi4,tinggi)
            trapesium.hitung()
            
            self.txtLuas.setText(f'{trapesium.luas}')
            self.txtKeliling.setText(f'{trapesium.keliling}')
            
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Masukkan nilai')
    
    def keluar(self):
        self.close()