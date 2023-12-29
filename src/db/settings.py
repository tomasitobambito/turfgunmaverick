from src.db.managerBase import ManagerBase


class Settings(ManagerBase):
    """Class that manages the most recent ID for turfjes and people. Any other future DB specific internal settings go in here as well.

    Inherits from ManagerBase.
    """
    def __init__(self):
        super().__init__('./data/settings.json')
        
        self.settings = self.read_file()


    def get_turfje_ID(self):
        """Gets the next turfjes ID and increases the latest used ID stored in settings.json.

        Returns:
            int: The new ID.
        """
        self.settings['currentTurfjeID'] += 1
        self.save_file(self.settings)

        return self.settings['currentTurfjeID']


    def get_person_ID(self):
        """Gets the next persons ID and increases the latest used ID stored in settings.json

        Returns:
            int: The new ID.
        """
        self.settings['currentPersonID'] += 1
        self.save_file(self.settings)

        return self.settings['currentPersonID']

    
    def reset(self):
        """Resets both IDs to -1 to restart at 0 when next called. DO NOT DO THIS IF DATA ALREADY EXISTS.
        """
        self.settings = {
            'currentTurfjeID': -1,
            'currentPersonID': -1
        }

        self.save_file(self.settings)
