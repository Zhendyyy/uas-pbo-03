from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from CRUD.serum import Serum

class SerumForm(QDialog):
    def __init__(self,parent=None):
        super(SerumForm,self).__init__(parent)
        loadUi('C:/uas/view/serum.ui',self)
        self.TampilData()
        self.btnSimpan.clicked.connect(self.simpanData)
        self.btnEdit.clicked.connect(self.updateData)
        # self.tblSerum.itemDoubleClicked.connect(self.handle_item_double_click)
        self.btnKeluar.clicked.connect(self.keluar)

    def TampilData(self):
        data_serum = Serum.tampil_serum(self)
        if data_serum:
            self.tblSerum.setRowCount(0)
            for row_number,row_data in enumerate(data_serum):
                self.tblSerum.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tblSerum.setItem(row_number,column_number,
                                           QTableWidgetItem(str(data)))
                    for row in range(self.tblSerum.rowCount()):
                        for col in range(self.tblSerum.columnCount()):
                            item = self.tblSerum.item(row, col)
                            if item:
                                item.setFlags(item.flags() & Qt.ItemIsEnabled)
                    
    def simpanData(self):
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        serum = Serum(nama,kode,harga,fungsi, brand)
        serum.save()
        QMessageBox.information(self,'Success','Data Serum berhasil disimpan..!!!')
        self.TampilData()
        
    def updateData(self):
        kode_lama = self.txtKode.text()
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        serum = Serum(nama,kode,harga,fungsi, brand)
        serum.update(kode_lama)
        QMessageBox.information(self,'Success','Data Serum berhasil diubah..!!!')
        self.TampilData()

    def deleteData(self):
        nama = self.txtNama.text()
        kode = self.txtKode.text()
        harga = self.txtHarga.text()
        fungsi = self.txtFungsi.text()
        brand = self.txtBrand.text()
        serum = Serum(nama,kode,harga,fungsi, brand)
        serum.delete(kode)
        QMessageBox.information(self,'Success','Data Serum berhasil dihapus..!!!')
        self.TampilData()
    
    def keluar(self):
        self.close()