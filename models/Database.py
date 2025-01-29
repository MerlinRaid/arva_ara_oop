import sqlite3

from models.Stopwatch import Stopwatch


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

    def no_cheater(self):
        """Loeme andmebaasist infot, kus on kuvatud ainult ausad mängijad, sorteeritult ja piiratud 10 mängijaga"""
        if self.cursor:
            try:
                sql = f'''
                    SELECT name, quess, steps, game_length 
                    FROM {self.tabel} 
                    WHERE cheater = ? 
                    ORDER BY steps ASC, game_length ASC, name ASC 
                    LIMIT 10;
                '''  # Sorteeri ja piirdu 10 mängijaga
                self.cursor.execute(sql, (0,))  # Käivita see päring
                data = self.cursor.fetchall()  # Kõik kirjed muutujasse data
                return data  # Tagastab kõik andmebaasi kirjed
            except sqlite3.Error as error:
                print(f'Kirjete lugemisel ilmnes tõrge: {error}')
                return []  # Tagastab tühja listi
            finally:
                self.close_connection()  # Katkesta ühendus
        else:
            print('Ühenduse andmebaasiga puudub. Palun loo ühendus andmebaasiga')

    def for_export(self):
        """Tagastab kogu andmebaasi sisu (kõik veerud), sorteeritult sama moodi nagu no_cheater()"""
        if self.cursor:
            try:
                sql = f'''
                    SELECT * 
                    FROM {self.tabel} 
                    ORDER BY steps ASC, game_length ASC, name ASC;
                '''  # Kogu tabel, sama sorteerimine
                self.cursor.execute(sql)  # Käivita see päring
                data = self.cursor.fetchall()  # Kõik kirjed muutujasse data
                return data  # Tagastab kõik andmebaasi kirjed
            except sqlite3.Error as error:
                print(f'Kirjete lugemisel ilmnes tõrge: {error}')
                return []  # Tagastab tühja listi
            finally:
                self.close_connection()  # Katkesta ühendus
        else:
            print('Ühenduse andmebaasiga puudub. Palun loo ühendus andmebaasiga')

    def add_record(self, name, steps, pc_nr, cheater, seconds):
        """Lisab mängija andmed tabelisse"""
        if self.cursor:
            try:
                sql = f'INSERT INTO {self.tabel} (name, steps, quess, cheater, game_length) VALUES (?, ?, ?, ?, ?);'
                self.cursor.execute(sql, (name, steps, pc_nr, cheater, seconds)) #Nende kahe rejaga üritab phyton lisada anmeid andmebaasi
                self.conn.commit() #See lisab reaalselt tabelisse (save)
                print('Mängija on listaud tabelisse!')
            except sqlite3.Error as error:
                print(f'Mängija lisamisel tekkis tõrge {error}')
            finally:
                self.close_connection()
        else:
            print('Ühendus puudub! Palun loo ühendus andmebaasiga.')

"""def read_records(self):
        Loeme andmebaasist kogu edetabeli
        if self.cursor:
            try:
                sql = f'SELECT * FROM {self.tabel};'  # Päring andmebaasi
                self.cursor.execute(sql)  # Käivita see päring
                data = self.cursor.fetchall()  # Kõik kirjed muutujasse data
                return data  # Tagastab kõik andmebaasi kirjed
            except sqlite3.Error as error:
                print(f'Kirjete lugemisel ilmnes tõrge: {error}')
                return []  # tagastab tühja listi
            finally:
                self.close_connection()  # Katkesta ühendus
        else:
            print('Ühenduse andmebaasiga puudub. Palun loo ühendus andmebaasiga')"""