import os
import time
from src.settings import Settings
from src.usersettings import UserSettings
from src.turfje import TurfjeManager
from src.person import PersonManager
from src.reasons import RemovalReason


class DataBase():
    def __init__(self):
        if not os.path.isdir('./data'):
            os.mkdir('./data')

        self.settings = Settings()
        self.userSettings = UserSettings()
        self.turfjes = TurfjeManager()
        self.people = PersonManager()

    # ----------- UserSettings -----------
    def get_reason(self, abbreviation: str):
        self.userSettings.get_reason(abbreviation)

    
    def create_reason(self, abbreviation: str, description: str):
        self.userSettings.create_reason(abbreviation, description)

    
    def delete_reason(self, abbreviation: str):
        self.userSettings.delete_reason(abbreviation)


    def get_removal_reason(self, abbreviation: str):
        self.userSettings.get_removal_reason(abbreviation)


    def create_removal_reason(self, abbreviation: str, description: str, turfjeCount: int = 1):
        self.userSettings.create_removal_reason(abbreviation, description, turfjeCount)


    def delete_removal_reason(self, abbreviation: str):
        self.userSettings.delete_removal_reason(abbreviation)

    
    # ----------- Turfje -----------
    def get_turfje(self, id: int):
        return self.turfjes.get_turfje(id)

    
    def get_turfjes(self, personId: int):
        return self.turfjes.get_turfjes(personId)

    
    def create_turfje(self, personId: int, reasonAbbreviation: str, creationDate: float = time.time()):
        newestId = self.settings.get_turfje_ID()
        
        # check if person and reason exist
        self.people.get_person(personId)
        self.userSettings.get_reason(reasonAbbreviation)

        self.turfjes.create_turfje(newestId, personId, reasonAbbreviation, creationDate)

    
    def remove_turfjes(self, personId: int, reasonAbbreviation: str):
        # check that person and reason exists
        self.people.get_person(personId)
        reason = self.userSettings.get_removal_reason(reasonAbbreviation)

        self.turfjes.remove_turfjes(personId, reason)

    
    def remove_turfjes(self, personId: int, reason: RemovalReason):
        # check that person and reason exist
        self.people.get_person(personId)
        self.userSettings.get_removal_reason(reason.abbreviation)

        self.turfjes.remove_turfjes(personId, reason)


    # ----------- Person -----------
    def get_person(self, id: int):
        return self.people.get_person(id)

    
    def create_person(self, name: str, position: str):
        id = self.settings.get_person_ID()

        self.people.create_person(id, name, position)

    
    def update_person(self, id: int, name: str = '', position: str = ''):
        self.people.update_person(id, name, position)


    def delete_person(self, id: int):
        self.people.delete_person(id)



    def reset(self):
        """Empty out entire database. WARNING IRREVERSIBLE.
        """
        self.settings.reset()
        self.userSettings.reset()
        self.turfjes.reset()
        self.people.reset()
