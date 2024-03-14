from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from CRUD.facialwash import Facialwash

class FacialwashForm(QDialog):
    def __init__(self,parent=None):
        super(FacialwashForm,self).__init__(parent)
        loadUi('C:/uas/view/facialwash.ui',self)
        self.TampilData()
        self.btnSimpan.clicked.connect(self.simpanData)
        self.btnEdit.clicked.connect(self.updateData)
        # self.tblFacialwash.itemDoubleClicked.connect(self.handle_item_double_click)
        self.btnKeluar.clicked.connect(self.keluar)

    def TampilData(self):
        data_facialwash = Facialwash.tampil_facialwash(self)
        if data_facialwash:
            self.tblFacialwash.setRowCount(0)
            for row_number,row_data in enumerate(data_facialwash):
                self.tblFacialwash.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tblFacialwash.setItem(row_number,column_number,
                                           QTableWidgetItem(str(data)))
                    for row in range(self.tblFacialwash.rowCount()):
                        for col in range(self.tblFacialwash.columnCount()):
                            item = self.tblFacialwash.item(row, col)
                            if item:
                                item.setFlags(item.flags() & Qt.ItemIsEnabled)
                    
    def simpanData(self):
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        facialwash = Facialwash(nama,kode,harga,fungsi, brand)
        facialwash.save()
        QMessageBox.information(self,'Success','Data Facialwash berhasil disimpan..!!!')
        self.TampilData()
        
    def updateData(self):
        kode_lama = self.txtKode.text()
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        facialwash = Facialwash(nama,kode,harga,fungsi, brand)
        facialwash.update(kode_lama)
        QMessageBox.information(self,'Success','Data Facialwash berhasil diubah..!!!')
        self.TampilData()

    def deleteData(self):
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        facialwash = Facialwash(nama,kode,harga,fungsi, brand)
        facialwash.delete(kode)
        QMessageBox.information(self,'Success','Data Facialwash berhasil dihapus..!!!')
        self.TampilData()
    
    def keluar(self):
        self.close()