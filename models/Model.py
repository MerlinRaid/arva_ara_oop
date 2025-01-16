from random import randint

from models.Database import Database
from models.Stopwatch import Stopwatch

from tabulate import tabulate
from datetime import datetime


class Model:
    #Defineerime kalssi muutujad
    pc_nr = randint(1, 100)
    steps = 0 # Käikude arv
    game_over = False #Mäng ei ole läbi
    cheater = False # Mängija ei ole petja
    stopwatch = Stopwatch() # Loome stopperi objekti

    def __init__(self):
        """Konstruktor"""
        self.rest_game()

    def rest_game(self):
        """Teeb uue mängu"""
        self.pc_nr = randint(1, 100)
        self.steps = 0  # Käikude arv
        self.game_over = False  # Mäng ei ole läbi
        self.cheater = False  # Mängija ei ole petja
        self.stopwatch.reset() # Nullib stopperi
        #self.stopwatch.start() #Käivitab stopperi

    def ask(self):
        """Küsib numbrit ja kontrollib"""
        user_nr = int(input('Sisesta number: ')) # Küsi mängijalt numbrit
        self.steps += 1 # Käikude arv kasvab

        if user_nr == 1000: #Tagauks
            self.cheater = True  # Sa oled petja
            self.game_over = True # Mäng sai läbi
            self.stopwatch.stop() # Peata aeg
            print(f'Leidsid mu nõrg koha. Õige number oli {self.pc_nr}.')
        elif user_nr > self.pc_nr:
            print('Väiksem')
        elif user_nr < self.pc_nr:
            print('Suurem')
        elif user_nr == self.pc_nr:
            self.game_over = True
            self.stopwatch.stop()
            print(f'Leidsid õige numbri {self.steps} sammmudega.')

    def let_paly(self):
        """Mängime mängu- avalik meetod"""
        self.stopwatch.start() #Käivitab stopperi
        while not self.game_over:
            self.ask()
        print(f'Mäng kestis {self.stopwatch.format_time()}') #Näita mängu kestvust
        self.what_next() #Mis on järgmiseks #Nime küsimine ja kirje lisamine
        self.show_menu() #Näita mängu menüüd

    def what_next(self):
        """Küsime mängija nime ja lisame info andmebaasi"""
        name = self.ask_name()
        db = Database() # Loo andmebaasi objekt
        db.add_record(name, self.steps, self.pc_nr, self.cheater, self.stopwatch.seconds)




    @staticmethod
    def ask_name():
        """Küsib nime ja tagastab korrektse nime"""
        name = input('Kuidas on mängija nimi: ')
        if not name.strip():
            name = 'Teadmata'
        return name.strip()

    def show_menu(self):
        """Näita mängu menüüd"""
        print('1 - Mängima')
        print('2 - Edetabel')
        print('3 - Välju programmist')
        user_input = int(input('Sisesta number [1, 2 või 3]: '))
        if 1 <= user_input <= 3:
            if user_input == 1:
                self.rest_game()# Nulli mäng ära
                self.let_paly() # Alusta uut mängu
            elif user_input == 2:
                self.show_no_change() # Näita edetabelit
                self.show_menu() #Näita menüüd
            elif user_input == 3:
                print('Bye,bye :)')
                exit() #Igasugune skript lõpetab töö

        else:
            self.show_menu()

#Minu loodud tabel, kellaaja vormindamine poolik
    @staticmethod
    def format_time(seconds):
        hours = seconds // 3600 # Toppeltkaldkriips ei arvestata jääki võetakse täis osa
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        #return "%02d:%02d:%02d" % (hours, minutes, seconds) sama, mis teine return
        return f'{hours:02}:{minutes:02}:{seconds:02}'


#Õpetaja tehtud, minu täiendatud, kriipsud on minu tabel
    def manual_table(self, data):
        print('Nimi               Number   Sammud    Mänguaeg')
        for row in data:
            print('----------------------------------------------------')
            print(f'{row[0][:15]:<16} | {row[1]:>6} | {row[2]:>6} | {self.format_time(row[3]):>9}')


    def show_no_change(self):
        """Edetabel asatele mängijatele"""
        db= Database()
        data = db.no_cheater()
        if data:
            #Vormindus funksioon veerule
            formatters = {'Mängu aeg': self.format_time,}
            print() #Tühirida enne endetabelit
            #self.print_tabel(data,formatters)
            self.manual_table(data)
            print()

    @staticmethod #Näitab kõike, ei ole vormindatud
    def show_leaderboard():
        db = Database()
        data = db.read_records()
        if data:
            for record in data:
                print(record) # Hetkel näitab tervet listi, kui tahad näha nt ainult nimesid: print(record[1])

    @staticmethod# Minu tehtud tabel
    def my_table():
        db = Database()
        data = db.no_cheater()
        if data:
            formatted_data = [
                (row[0], row[1], row[2], Model.format_time(row[3])) for row in data
            ]
            headers = ["Nimi", "Arvatav number", "Sammud", "Mängu kestus"]

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(tabulate(formatted_data, headers=headers, tablefmt="pretty")) # Hetkel näitab tervet listi, kui tahad näha nt ainult nimesid: print(record[1])

