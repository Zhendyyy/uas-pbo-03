import sqlite3

class Moisturizer():
    pathDB = 'C:/uas/databases/database.db'

    def __init__(self,nama,kode,harga,fungsi, brand):
        self.nama = nama
        self.kode = kode
        self.harga = harga
        self.fungsi = fungsi
        self.brand = brand

    def tampil_moisturizer(self):
        try:
            conn = sqlite3.connect(Moisturizer.pathDB)
            curr = conn.cursor()
            query = "SELECT * FROM moisturizer"
            curr.execute(query)
            data_moisturizer= curr.fetchall()
            return data_moisturizer
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()

    def save(self):
        try:
            conn =  sqlite3.connect(Moisturizer.pathDB)
            curr = conn.cursor()
            query = "INSERT INTO moisturizer (nama,kode,harga,fungsi,brand) VALUES (?,?,?,?,?)"
            curr.execute(query,(self.nama,self.kode,self.harga,self.fungsi, self.brand))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close()

    def update(self,kode_lama):
        try:
            conn =  sqlite3.connect(Moisturizer.pathDB)
            curr = conn.cursor()
            query = "UPDATE moisturizer SET nama = ?, kode = ?, harga = ?, fungsi = ?, brand = ? WHERE kode = ?"
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
            conn =  sqlite3.connect(Moisturizer.pathDB)
            curr = conn.cursor()
            query = "DELETE FROM moisturizer WHERE kode = ?"
            curr.execute(query,(kode,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error e:",e)
        finally:
            curr.close()
            conn.close() 