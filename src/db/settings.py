from src.db.managerBase import ManagerBase


class Settings(ManagerBase):
    def __init__(self):
        super().__init__('./data/settings.json')
        
        self.settings = self.read_file()


    def get_turfje_ID(self):
        self.settings['currentTurfjeID'] += 1
        self.save_file(self.settings)

        return self.settings['currentTurfjeID']


    def get_person_ID(self):
        self.settings['currentPersonID'] += 1
        self.save_file(self.settings)

        return self.settings['currentPersonID']

    
    def reset(self):
        self.settings = {
            'currentTurfjeID': -1,
            'currentPersonID': -1
        }

        self.save_file(self.settings)
