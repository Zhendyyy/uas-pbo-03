import sqlite3

class Lingkaran:
    PathDB = 'C:/uas/databases/dbrumus.db'
    
    def __init__(self, jari):
        self.jari = jari
        self.luas = None
        self.keliling = None
        
    def tampil_Lingkaran(self):
        try:
            conn = sqlite3.connect(Lingkaran.PathDB)
            curr = conn.cursor()
            query = "SELECT * FROM lingkaran"
            curr.execute(query)
            data_Lingkaran= curr.fetchall()
            return data_Lingkaran
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()
        
    def hitung(self):
        self.luas = 3.14 * self.jari**2
        self.keliling = 2 * 3.14 * self.jari
        