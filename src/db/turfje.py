from src.db.managerBase import ManagerBase
from src.exceptions import TurfjeDoesNotExistError
from src.db.reasons import RemovalReason
import time
import os.path

class Turfje:
    """Model class for turfjes.
    """
    def __init__(self, id: int, personId: int, reasonAbbreviation: str, remReasonAbbreviation: str, creationDate: float, removed: bool = False):
        self.id = id
        self.personId = personId
        self.reasonAbbreviation = reasonAbbreviation
        self.remReasonAbbreviation = remReasonAbbreviation
        self.creationDate = creationDate
        self.removed = removed


class TurfjeManager(ManagerBase):
    """Class that manages the addition of turfjes to the database and facilitates communication with the file. Input validation is not handled here.

    Inherits from ManagerBase.
    """
    def __init__(self):
        super().__init__('./data/turfjes.json')

        self.turfjes = self.read_file()

        self.turfjes = [Turfje(
            turfje['id'],
            turfje['personId'], 
            turfje['reasonAbbreviation'],
            turfje['remReasonAbbreviation'],
            turfje['creationDate'],
            turfje['removed'])
            for turfje in self.turfjes]


    def create_turfje(self, id: int, personId: int, reasonAbbreviation: str, creationDate: float):        
        """Creates new turfje in the internal manager. Does NOT check if valid Id and abbreviation were entered.

        Args:
            id (int): The turfjes ID.
            personId (int): ID of person turfje is assigned to.
            reasonAbbreviation (str): Abbreviation of the reason the turfje was given.
            creationDate (float, optional): Time the turfje was handed out. Defaults to time.time().
        """
        newTurfje = Turfje(id, personId, reasonAbbreviation, '', creationDate)

        self.turfjes.append(newTurfje)

        self.save_file()
    

    def get_turfje(self, id: int):
        """Gets a turfje based on its id.

        Args:
            id (int): ID of the turfje to be gotten.

        Raises:
            TurfjeDoesNotExistError: Raised when no turfje with id found.
        
        Returns:
            Turfje: Turfje with the given id.
        """

        for turfje in self.turfjes:
            if turfje.id == id:
                return turfje

        raise TurfjeDoesNotExistError(id)


    def get_turfjes(self, personId: int):
        """Gets all turfjes assigned to a person.

        Args:
            personId (int): ID of the person whose turfjes are to be gotten.

        Returns:
            [Turfje]: All turfjes belonging to a person. 
        """
        turfjes = []
        
        for turfje in self.turfjes:
            if turfje.personId == personId:
                turfjes.append(turfje)

        return turfjes


    def remove_turfje_by_id(self, id: int, remReasonAbbreviation: str):
        """Remove a turfje by its id. This is used internally by TurfjeManager.remove_turfje_by_person.

        Args:
            id (int): Id of the turfje to be removed.
        """
        # check if the turfje exists
        self.get_turfje(id)

        for turfje in self.turfjes:
            if turfje.id == id:
                turfje.removed = True
                turfje.remReasonAbbreviation = remReasonAbbreviation

        self.save_file()


    def remove_turfjes(self, personId: int, reason: RemovalReason):
        """Removes a persons oldest turfje.

        Args:
            personId (int): The id of the person whose turfje is to be removed.
        """
        personsTurfjes = []

        for turfje in self.turfjes:
            if turfje.personId == personId and not turfje.removed:
                personsTurfjes.append(turfje)

        personsTurfjes.sort(key = lambda turfje: turfje.creationDate, reverse = True)

        for i in range(reason.turfjeCount):
            # end removal early if no turfjes left
            if len(personsTurfjes) == 0:
                return

            turfje = personsTurfjes.pop()
            self.remove_turfje_by_id(turfje.id, reason.abbreviation)


    def save_file(self):
        """Adjusted version of ManagerBase.save_file, specific to TurfjeManager. Called without providing data.
        """
        serializedList = [{
            'id': turfje.id,
            'personId': turfje.personId,
            'reasonAbbreviation': turfje.reasonAbbreviation,
            'remReasonAbbreviation': turfje.remReasonAbbreviation,
            'creationDate': turfje.creationDate,
            'removed': turfje.removed
        } for turfje in self.turfjes]

        super().save_file(serializedList)


    def reset(self):
        """Empty out turfje list and reset to no data. WARNING: REMOVES ALL CURRENTLY STORED TURFJES IMMEDIATELY.
        """
        self.turfjes = []

        self.save_file()