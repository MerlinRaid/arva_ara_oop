#import time # katsetuste jaoks

#from models.Database import Database # katsetuste jaoks
from models.Model import Model
#from models.Stopwatch import Stopwatch # katsetuste jaoks


if __name__ == '__main__':
    model = Model()

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