import threading
import time
from subprocess import check_output


class Stopwatch:
    def __init__(self):
        """Stopper konstruktor"""
        self.seconds = 0 # Aeg sekundites
        self.running = False # Kas aeg jookseb
        self.thread = None # Aeg eraldi threadi, e aeg jookseb tausatl, et oleks võimalik samaaeg mängida

    def start(self):
        """Käivita stopper"""
        if not self.running:
            self.running = True # Aeg jookseb
            self.thread = threading.Thread(target=self._run) #Lisatud threadi
            self.thread.start() # Käivita thread

    def _run(self):
        """Aeg jookseb threadis"""
        while self.running:
            time.sleep(1) # Oota 1 sekund
            self.seconds += 1 #Suurenda sekundit ühe võrra

    def stop(self):
        """Peata stopper"""
        self.running = False

    def reset(self):
        """Taaskäivita stopper"""
        self.stop() #Aega peatada
        self.seconds = 0 #Aega nullida

    def format_time(self):
        """Aeg inimlikul kujul mitte 715sek vaid 1min 15sek"""
        hours = self.seconds // 3600 # Toppeltkaldkriips ei arvestata jääki võetakse täis osa
        minutes = (self.seconds % 3600) // 60
        seconds = self.seconds % 60
        #return "%02d:%02d:%02d" % (hours, minutes, seconds) sama, mis teine return
        return f'{hours:02}:{minutes:02}:{seconds:02}'



