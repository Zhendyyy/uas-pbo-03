import sqlite3

class Belahketupat:
    PathDB = 'C:/uas/databases/dbrumus.db'
    
    def __init__(self, d1, d2, sisi):
        self.d1 = d1
        self.d2 = d2
        self.sisi = sisi
        self.luas = None
        self.keliling = None
        
    def tampil_Belahketupat(self):
        try:
            conn = sqlite3.connect(Belahketupat.PathDB)
            curr = conn.cursor()
            query = "SELECT * FROM belahketupat"
            curr.execute(query)
            data_belahketupat= curr.fetchall()
            return data_belahketupat
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()
        
    def hitung(self):
        self.luas = (self.d1 * self.d2)/2
        self.keliling = 4 * (self.sisi)
        