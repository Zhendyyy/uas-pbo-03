import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
from translate.translate import TranslateForm
from controllers.frmToner import TonerForm
from controllers.frmSerum import SerumForm
from controllers.frmMoisturizer import MoisturizerForm
from controllers.frmFacialwash import FacialwashForm
from frm.frmPersegipanjang import PersegipanjangForm
from frm.frmPersegi import PersegiForm
from frm.frmSegitiga import SegitigaForm
from frm.frmTrapesium import TrapesiumForm
from frm.frmLingkaran import LingkaranForm
from frm.frmLayanglayang import LayanglayangForm
from frm.frmBelahketupat import BelahketupatForm
from frm.frmJajargenjang import JajargenjangForm

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('C:/uas/view/mainwindows.ui',self)
        self.showMaximized()
        
        self.actionTranslate.triggered.connect(self.showTranslateForm)
        self.actiontoner.triggered.connect(self.showTonerForm)
        self.actionserum.triggered.connect(self.showSerumForm)
        self.actionfacialwash.triggered.connect(self.showFacialwashForm)
        self.actionmoisturizer.triggered.connect(self.showMoisturizerForm)
        self.actionPersegi_Panjang.triggered.connect(self.showPersegipanjangForm)
        self.actionPersegi.triggered.connect(self.showPersegiForm)
        self.actionSegitiga.triggered.connect(self.showSegitigaForm)
        self.actionTrapesium.triggered.connect(self.showTrapesiumForm)
        self.actionLingkaran.triggered.connect(self.showLingkaranForm)
        self.actionLayang_layang.triggered.connect(self.showLayanglayangForm)
        self.actionBelah_Ketupat.triggered.connect(self.showBelahketupatForm)
        self.actionJajar_Genjang.triggered.connect(self.showJajargenjangForm)
      
    def showTranslateForm(self):
        self.formTranslate = TranslateForm()
        # self.formTranslate.setModal(True)
        self.formTranslate.show()
        
    def showTonerForm(self):
        self.formToner = TonerForm()
        self.formToner.setModal(True)
        self.formToner.show()
        
    def showSerumForm(self):
        self.formSerum = SerumForm()
        self.formSerum.setModal(True)
        self.formSerum.show()
        
    def showFacialwashForm(self):
        self.formFacialwash = FacialwashForm()
        self.formFacialwash.setModal(True)
        self.formFacialwash.show()
        
    def showMoisturizerForm(self):
        self.formMoisturizer = MoisturizerForm()
        self.formMoisturizer.setModal(True)
        self.formMoisturizer.show()
    
    def showPersegipanjangForm(self):
        self.formPersegipanjang = PersegipanjangForm()
        self.formPersegipanjang.setModal(True)
        self.formPersegipanjang.show()
    
    def showPersegiForm(self):
        self.formPersegi = PersegiForm()
        self.formPersegi.setModal(True)
        self.formPersegi.show()
    
    def showSegitigaForm(self):
        self.formSegitiga = SegitigaForm()
        self.formSegitiga.setModal(True)
        self.formSegitiga.show()
        
    def showBelahketupatForm(self):
        self.formBelahketupat = BelahketupatForm()
        self.formBelahketupat.setModal(True)
        self.formBelahketupat.show()
    
    def showLingkaranForm(self):
        self.formLingkaran = LingkaranForm()
        self.formLingkaran.setModal(True)
        self.formLingkaran.show()
        
    def showTrapesiumForm(self):
        self.formTrapesium = TrapesiumForm()
        self.formTrapesium.setModal(True)
        self.formTrapesium.show()
        
    def showLayanglayangForm(self):
        self.formLayanglayang = LayanglayangForm()
        self.formLayanglayang.setModal(True)
        self.formLayanglayang.show()
        
    def showJajargenjangForm(self):
        self.formJajargenjang = JajargenjangForm()
        self.formJajargenjang.setModal(True)
        self.formJajargenjang.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = MainMenu() 
    mainMenu.show()
    sys.exit(app.exec_())

