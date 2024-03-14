import sqlite3

class Jajargenjang:
    PathDB = 'C:/uas/databases/dbrumus.db'
    
    def __init__(self, a,b,alas,tinggi):
        self.a = a 
        self.b = b 
        self.alas = alas
        self.tinggi = tinggi
        self.luas = None
        self.keliling = None
        
    def tampil_Jajargenjang(self):
        try:
            conn = sqlite3.connect(Jajargenjang.PathDB)
            curr = conn.cursor()
            query = "SELECT * FROM jajargenjang"
            curr.execute(query)
            data_Jajargenjang= curr.fetchall()
            return data_Jajargenjang
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()
        
    def hitung(self):
        self.luas = self.alas * self.tinggi
        self.keliling = 2 * (self.a + self.b)
        