import sqlite3

class Segitiga:
    PathDB = 'C:/uas/databases/dbrumus.db'
    
    def __init__(self, alas, tinggi, lebar):
        self.alas = alas
        self.tinggi = tinggi
        self.lebar = lebar
        self.luas = None
        self.keliling = None
        
    def tampil_Segitiga(self):
        try:
            conn = sqlite3.connect(Segitiga.PathDB)
            curr = conn.cursor()
            query = "SELECT * FROM segitiga"
            curr.execute(query)
            data_segitiga= curr.fetchall()
            return data_segitiga
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()
        
    def hitung(self):
        self.luas = (self.alas * self.tinggi) /2
        self.keliling = self.alas + self.lebar + self.tinggi
        