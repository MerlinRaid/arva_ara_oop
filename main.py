#import time # katsetuste jaoks

#from models.Database import Database # katsetuste jaoks
from models.Model import Model
#from models.Stopwatch import Stopwatch # katsetuste jaoks

"""
1. Tehke meetod no_cheater() <database klassi, mis tagastab ainult ausad mängijad.
2. Näita edetabelis ainult ausaid mängijaid nind edetabelis näita nimi, äraarvatav number, sammude arv ja aeg (00:00:00) ilusti.
Nimest näita ainult 15 esimest tähte kui on pikem nimi. 
"""

if __name__ == '__main__':
    model = Model()
    model.show_menu()

    #TODO Järgnev rida oli show_menu osa
    #model.let_paly() #kui on see ainult siis käivitab mäng kohe ja menüü tuleb pärast mängu ei pea ole show_menu'd

"""from models.Database import Database
db = Database()  
data = db.for_export()  
if data:
    for row in data:
        print(row)  
else:
    print("Andmebaasis ei ole kirjeid või esines viga!")""" #Kontroll, kas kogu tabeli export toimib




"""proovimine, kas numbri küsimine töötab ja aega jookseb ilusti
    model.ask()
    model.let_paly()"""


""" kas arvuti mõtleb numbri ja stopper töötab
    print(f'Juhuslik number: {model.pc_nr}') # Arvuti mõeldud number ja käivitati ka stopper
    time.sleep(2) # Oota 2 sek
    model.stopwatch.stop() # Jäta stopper seisma
    print(model.stopwatch.format_time()) # Näita aega"""



"""Kontroll, et andmebaas töötab
   db = Database()
   
   data = db.read_records()
    if data:
        for record in data:
            print(record)"""





""" Kontroll, kas stopper töötab
    stopper = Stopwatch() #Objekt loodud
    stopper.start()
    input("Oota....")
    stopper.stop()
    print(stopper.format_time())
"""