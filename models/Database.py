import sqlite3


class Database:
    db_name = 'game_leaderboard_v2.db' # Andmebaasinimi
    tabel = 'ranking' # vajalik tabelinimi, mis muutub
    def __init__(self):
        """konstruktor"""
        self.conn = None # Kas andmebaasiga on ühendus või ei ole
        self.cursor = None #Andmed, mis saab andmebaasist
        self.connect()  # Loo ühendus

    def connect(self):
        """Loob ühenduse andmebaasiga"""
        try:
            if self.conn:
                self.conn.close()
                print('Varasem andmebaasi ühendus suletud')
            self.conn = sqlite3.connect(self.db_name) #Loo ühendus
            self.cursor = self.conn.cursor()
            print(f'Uus ühendus andmebaasiga {self.db_name} loodud')
        except sqlite3.Error as error:
            print(f'Tõrge andmebaasi ühenduse loomisel: {error}')
            self.conn = None
            self.cursor = None

    def close_connection(self):
        """Sulgeb andmebaasiga ühenduse"""
        try:
            if self.conn:
                self.conn.close()
                print(f'Ühendus andmebaasiga {self.db_name} suletud')
        except sqlite3.Error as error:
            print(f'Tõrge ühenduse sulgemisel: {error}')

    def read_records(self):
        """Loeme andmebaasist kogu edetabeli"""
        if self.cursor:
            try:
                sql = f'SELECT * FROM {self.tabel};' # Päring andmebaasi
                self.cursor.execute(sql) # Käivita see päring
                data = self.cursor.fetchall() #Kõik kirjed muutujasse data
                return data #Tagastab kõik andmebaasi kirjed
            except sqlite3.Error as error:
                print(f'Kirjete lugemisel ilmnes tõrge: {error}')
                return [] #tagastab tühja listi
            finally:
                self.close_connection()  #Katkesta ühendus
        else:
            print('Ühenduse andmebaasiga puudub. Palun loo ühendus andmebaasiga')
