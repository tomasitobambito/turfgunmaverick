import os
import time
from src.db.settings import Settings
from src.db.usersettings import UserSettings
from src.db.turfje import TurfjeManager
from src.db.person import PersonManager
from src.db.reasons import RemovalReason


class DataBase():
    """Central db controller that manages all the other db managers. Used as a central point to interface with the db from the frontend.
    """
    def __init__(self):
        if not os.path.isdir('./data'):
            os.mkdir('./data')

        self.settings = Settings()
        self.userSettings = UserSettings()
        self.turfjes = TurfjeManager()
        self.people = PersonManager()

    # ----------- UserSettings -----------
    def get_reason(self, abbreviation: str):
        """Gets a reason from the db.

        Args:
            abbreviation (str): Abbreviation of the reason to be gotten.

        Returns:
            Reason: The desired reason.
        """
        return self.userSettings.get_reason(abbreviation)

    
    def create_reason(self, abbreviation: str, description: str):
        """Creates a new reason in the db.

        Args:
            abbreviation (str): Abbreviation of the new reason.
            description (str): Description of the new reason.
        """
        self.userSettings.create_reason(abbreviation, description)

    
    def delete_reason(self, abbreviation: str):
        """Deletes a reason from the db.

        Args:
            abbreviation (str): Abbreviation of the reason to be deleted.
        """
        self.userSettings.delete_reason(abbreviation)


    def get_removal_reason(self, abbreviation: str):
        """Gets a removal reason from the db.

        Args:
            abbreviation (str): Abbreviation of the reason to be gotten.

        Returns:
            Reason: The desired reason.
        """
        return self.userSettings.get_removal_reason(abbreviation)


    def create_removal_reason(self, abbreviation: str, description: str, turfjeCount: int = 1):
        """Creates a removal reason in the db.

        Args:
            abbreviation (str): Abbreviation of the new reason.
            description (str): Description of the new reason.
            turfjeCount (int, optional): Amount of turfjes removed by the new reason. Defaults to 1.
        """
        self.userSettings.create_removal_reason(abbreviation, description, turfjeCount)


    def delete_removal_reason(self, abbreviation: str):
        """Delete a removal reason from the db.

        Args:
            abbreviation (str): Abbreviation of the reason to be deleted.
        """
        self.userSettings.delete_removal_reason(abbreviation)

    
    # ----------- Turfje -----------
    def get_turfje(self, id: int):
        """Gets a turfje based on its ID from the db.

        Args:
            id (int): ID of the turfje to be gotten.

        Returns:
            Turfje: The desired turfje.
        """
        return self.turfjes.get_turfje(id)

    
    def get_turfjes(self, personId: int):
        """Gets all turfjes collected by a person, both active and removed ones.

        Args:
            personId (int): ID of the person whose turfjes are desired.

        Returns:
            List(Turfje): List of turfjes collected by the desired person.
        """
        return self.turfjes.get_turfjes(personId)

    
    def create_turfje(self, personId: int, reasonAbbreviation: str, creationDate: float = time.time()):
        """Creates a new turfje in the db.

        Args:
            personId (int): ID of the person who the turfje is being assigned to.
            reasonAbbreviation (str): Abbreviation of the reason the turfje is given.
            creationDate (float, optional): The time the turfje was handed out. Defaults to time.time().
        """
        newestId = self.settings.get_turfje_ID()
        
        # check if person and reason exist
        self.people.get_person(personId)
        self.userSettings.get_reason(reasonAbbreviation)

        self.turfjes.create_turfje(newestId, personId, reasonAbbreviation, creationDate)

    
    def remove_turfjes(self, personId: int, reasonAbbreviation: str):
        """Removes a set number of turfjes from a person based on the reason abbreviation. Selecting the oldest active ones.

        Args:
            personId (int): ID of the person whose turfjes are being removed.
            reasonAbbreviation (str): Abbreviation of the reason that the turfjes are being removed (this is a removal reason).
        """
        # check that person and reason exists
        self.people.get_person(personId)
        reason = self.userSettings.get_removal_reason(reasonAbbreviation)

        self.turfjes.remove_turfjes(personId, reason)

    
    def remove_turfjes(self, personId: int, reason: RemovalReason):
        """"Removes a set number of turfjes from a person based on the reason object. Selecting the oldest active ones.

        Args:
            personId (int): ID of the person whose turfjes are being removed.
            reason (RemovalReason): The reason the turfjes are being removed (this is a removal reason).
        """
        # check that person and reason exist
        self.people.get_person(personId)
        self.userSettings.get_removal_reason(reason.abbreviation)

        self.turfjes.remove_turfjes(personId, reason)


    # ----------- Person -----------
    def get_person(self, id: int):
        """Gets a person from the db.

        Args:
            id (int): ID of the person to be gotten.

        Returns:
            Person: The desired person.
        """
        return self.people.get_person(id)

    
    def create_person(self, name: str, position: str):
        """Creates a new person in the db.

        Args:
            name (str): Name of the new person.
            position (str): Position of the new person.
        """
        id = self.settings.get_person_ID()

        self.people.create_person(id, name, position)

    
    def update_person(self, id: int, name: str = '', position: str = ''):
        """Updates a person in the db.

        Args:
            id (int): ID of the person to be updated.
            name (str, optional): The updated name. Defaults to '', which is processed as the original name.
            position (str, optional): The updated position. Defaults to '', which is processed as the original position.
        """
        self.people.update_person(id, name, position)


    def delete_person(self, id: int):
        """Deletes a person from the db.

        Args:
            id (int): ID of the person to be deleted.
        """
        self.people.delete_person(id)


    # ----------- General -----------
    def reset(self):
        """Empty out entire database. WARNING IRREVERSIBLE.
        """
        self.settings.reset()
        self.userSettings.reset()
        self.turfjes.reset()
        self.people.reset()
