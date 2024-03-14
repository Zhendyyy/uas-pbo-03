import sqlite3

class Persegi:
    PathDB = 'C:/uas/databases/dbrumus.db'
    
    def __init__(self, sisi):
        self.sisi = sisi
        self.luas = None
        self.keliling = None
        
    def tampil_Persegi(self):
        try:
            conn = sqlite3.connect(Persegi.PathDB)
            curr = conn.cursor()
            query = "SELECT * FROM persegi"
            curr.execute(query)
            data_Persegi= curr.fetchall()
            return data_Persegi
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()
        
    def hitung(self):
        self.luas = self.sisi * self.sisi
        self.keliling = 4 * (self.sisi)
        