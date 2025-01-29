from models.Database import Database
from datetime import datetime


class ExportToFile:
    def __init__(self, model):
        self.model = model
        self.db = Database()
        self.data = self.db.for_export()

    def export(self):
        if not self.data:
            print('Andmebaas on tühi, eksporti ei tehta.')
            return
        txt_filename = 'game_leaderboard_v2.txt'
        headers = 'id;name;steps;quess;cheater;game_length;game_time'
        with open(txt_filename, 'w', encoding='utf-8') as file:
            file.write(headers + '\n')
            for row in self.data:
                id_, name, steps, quess, cheater, game_length, game_time = row  #
                formatted_time = self.model.format_time(game_length)
                formatted_datetime = datetime.strptime(game_time, '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M:%S')
                line = f'{id_};{name};{steps};{quess};{cheater};{formatted_time};{formatted_datetime}\n'
                file.write(line)
        print(f'Edetabel eksporditi faili: {txt_filename}')
