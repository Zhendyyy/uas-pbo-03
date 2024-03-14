import sqlite3

class Layanglayang:
    PathDB = 'C:/uas/databases/dbrumus.db'
    
    def __init__(self, d1,d2,panjang,lebar):
        self.d1 = d1
        self.d2 = d2
        self.panjang = panjang
        self.lebar = lebar
        self.luas = None
        self.keliling = None
        
    def tampil_Layanglayang(self):
        try:
            conn = sqlite3.connect(Layanglayang.PathDB)
            curr = conn.cursor()
            query = "SELECT * FROM layanglayang"
            curr.execute(query)
            data_Layanglayang= curr.fetchall()
            return data_Layanglayang
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()
        
    def hitung(self):
        self.luas = 0.5 * self.d1 * self.d2
        self.keliling = 2 * (self.panjang + self.lebar)
        