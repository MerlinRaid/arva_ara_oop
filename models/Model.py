from random import randint

from models.Stopwatch import Stopwatch


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
        self.stopwatch.start() #Käivitab stopperi

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
        while not self.game_over:
            self.ask()
        print(f'Mäng kestis {self.stopwatch.format_time()}') #Näita mängu kestvust

