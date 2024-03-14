import sqlite3

class Toner():
    pathDB = 'C:/uas/databases/database.db'

    def __init__(self,nama,kode,harga,fungsi, brand):
        self.nama = nama
        self.kode = kode
        self.harga = harga
        self.fungsi = fungsi
        self.brand = brand

    def tampil_toner(self):
        try:
            conn = sqlite3.connect(Toner.pathDB)
            curr = conn.cursor()
            query = "SELECT * FROM toner"
            curr.execute(query)
            data_toner= curr.fetchall()
            return data_toner
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()

    def save(self):
        try:
            conn =  sqlite3.connect(Toner.pathDB)
            curr = conn.cursor()
            query = "INSERT INTO toner (nama,kode,harga,fungsi,brand) VALUES (?,?,?,?,?)"
            curr.execute(query,(self.nama,self.kode,self.harga,self.fungsi, self.brand))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close()

    def update(self,kode_lama):
        try:
            conn =  sqlite3.connect(Toner.pathDB)
            curr = conn.cursor()
            query = "UPDATE toner SET kode = ?, nama = ?, harga = ?, fungsi = ?, brand = ? WHERE kode = ?"
            curr.execute(query,(self.nama, self.kode, self.harga, self.fungsi, self.brand,kode_lama))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close() 

    @staticmethod
    def delete(kode):
        try:
            conn =  sqlite3.connect(Toner.pathDB)
            curr = conn.cursor()
            query = "DELETE FROM toner WHERE kode = ?"
            curr.execute(query,(kode,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close() 