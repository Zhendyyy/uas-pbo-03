from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from CRUD.moisturizer import Moisturizer

class MoisturizerForm(QDialog):
    def __init__(self,parent=None):
        super(MoisturizerForm,self).__init__(parent)
        loadUi('C:/uas/view/moisturizer.ui',self)
        self.TampilData()
        self.btnSimpan.clicked.connect(self.simpanData)
        self.btnEdit.clicked.connect(self.updateData)
        # self.tblMoisturizer.itemDoubleClicked.connect(self.handle_item_double_click)
        self.btnKeluar.clicked.connect(self.keluar)

    def TampilData(self):
        data_moisturizer = Moisturizer.tampil_moisturizer(self)
        if data_moisturizer:
            self.tblMoisturizer.setRowCount(0)
            for row_number,row_data in enumerate(data_moisturizer):
                self.tblMoisturizer.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tblMoisturizer.setItem(row_number,column_number,
                                           QTableWidgetItem(str(data)))
                    for row in range(self.tblMoisturizer.rowCount()):
                        for col in range(self.tblMoisturizer.columnCount()):
                            item = self.tblMoisturizer.item(row, col)
                            if item:
                                item.setFlags(item.flags() & Qt.ItemIsEnabled)
                    
    def simpanData(self):
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        moisturizer = Moisturizer(nama,kode,harga,fungsi, brand)
        moisturizer.save()
        QMessageBox.information(self,'Success','Data Moisturizer berhasil disimpan..!!!')
        self.TampilData()
        
    def updateData(self):
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        kode_lama = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        moisturizer = Moisturizer(nama,kode,harga,fungsi, brand)
        moisturizer.update(kode_lama)
        QMessageBox.information(self,'Success','Data Moisturizer berhasil diubah..!!!')
        self.TampilData()

    def deleteData(self):
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        moisturizer = Moisturizer(nama,kode,harga,fungsi, brand)
        moisturizer.delete(kode)
        QMessageBox.information(self,'Success','Data Moisturizer berhasil dihapus..!!!')
        self.TampilData()
        
    def keluar(self):
        self.close()