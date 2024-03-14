from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from CRUD.toner import Toner

class TonerForm(QDialog):
    def __init__(self,parent=None):
        super(TonerForm,self).__init__(parent)
        loadUi('C:/uas/view/toner.ui',self)
        self.TampilData()
        self.btnSimpan.clicked.connect(self.simpanData)
        self.btnEdit.clicked.connect(self.updateData)
        # self.tblToner.itemDoubleClicked.connect(self.handle_item_double_click)
        self.btnKeluar.clicked.connect(self.keluar)

    def TampilData(self):
        data_toner = Toner.tampil_toner(self)
        if data_toner:
            self.tblToner.setRowCount(0)
            for row_number,row_data in enumerate(data_toner):
                self.tblToner.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tblToner.setItem(row_number,column_number,
                                           QTableWidgetItem(str(data)))
                    for row in range(self.tblToner.rowCount()):
                        for col in range(self.tblToner.columnCount()):
                            item = self.tblToner.item(row, col)
                            if item:
                                item.setFlags(item.flags() & Qt.ItemIsEnabled)
                    
    def simpanData(self):
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        toner = Toner(nama,kode,harga,fungsi, brand)
        toner.save()
        QMessageBox.information(self,'Success','Data Toner berhasil disimpan..!!!')
        self.TampilData()
        
    def updateData(self):
        kode_lama = self.txtKode.text()
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        toner = Toner(nama,kode,harga,fungsi, brand)
        toner.update(kode_lama)
        QMessageBox.information(self,'Success','Data Toner berhasil diubah..!!!')
        self.TampilData()

    def deleteData(self):
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        toner = Toner(nama,kode,harga,fungsi, brand)
        toner.delete(kode)
        QMessageBox.information(self,'Success','Data Toner berhasil dihapus..!!!')
        self.TampilData()
    
    def keluar(self):
        self.close()