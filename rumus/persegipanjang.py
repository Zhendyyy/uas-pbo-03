import sqlite3

class Persegipanjang:
    PathDB = 'C:/uas/databases/dbrumus.db'
    
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        self.luas = None
        self.keliling = None
        
    def tampil_Persegipanjang(self):
        try:
            conn = sqlite3.connect(Persegipanjang.PathDB)
            curr = conn.cursor()
            query = "SELECT * FROM persegipanjang"
            curr.execute(query)
            data_Persegipanjang= curr.fetchall()
            return data_Persegipanjang
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()
        
    def hitung(self):
        self.luas = self.panjang * self.lebar
        self.keliling = 2 * (self.panjang + self.lebar)
        