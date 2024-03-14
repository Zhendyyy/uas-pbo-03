import sqlite3

class Trapesium:
    PathDB = 'C:/uas/databases/dbrumus.db'
    
    def __init__(self, sisi1, sisi2, sisi3,sisi4, tinggi):
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.sisi3 = sisi3
        self.sisi4 = sisi4
        self.tinggi = tinggi
        self.luas = None
        self.keliling = None
        
    def tampil_Trapesium(self):
        try:
            conn = sqlite3.connect(Trapesium.PathDB)
            curr = conn.cursor()
            query = "SELECT * FROM trapesium"
            curr.execute(query)
            data_Trapesium= curr.fetchall()
            return data_Trapesium
        except sqlite3.Error as e:
            print('Error : ',e)
        finally:
            curr.close()
            conn.close()
        
    def hitung(self):
        self.luas = 0.5 * (self.sisi1 * self.sisi2)*self.tinggi
        self.keliling = self.sisi1 + self.sisi2 + self.sisi3 + self.sisi4
        