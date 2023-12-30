from src.db.managerBase import ManagerBase
from src.db.reasons import Reason, RemovalReason
from src.exceptions import ReasonError


class UserSettings(ManagerBase):
    """Class to manage user specific database settings like reasons and removal reasons. 

    Inherits from ManagerBase.
    """
    def __init__(self):
        super().__init__('./data/usersettings.json')

        self.settings = self.read_file()
        
        # convert dictionaries into objects for easier manipulation
        self.reasons = [Reason(
            reason['abbreviation'], 
            reason['description'])
            for reason in self.settings['reasons']]
        
        self.removalReasons = [RemovalReason(
            reason['abbreviation'],
            reason['description'], 
            reason['turfjeCount'])
            for reason in self.settings['removalReasons']]
    

    def does_reason_exist(self, abbreviation: str):
        """Only for internal use, do not call outside of class, Use get_reason instead for consistency. Checks if a reasons exists.

        Args:
            abbreviation (str): Abbreviation of the reason to be checked.

        Returns:
            bool: True if the reason exists, else false.
        """
        for reason in self.reasons:
            if reason.abbreviation == abbreviation:
                return True
        
        return False

    def get_reason(self, abbreviation: str):
        """Gets a reason based on its abbreviation. 

        Args:
            abbreviation (str): Abbreviation of the reason to be gotten.

        Raises:
            ReasonError: Thrown if the reason doesn't exist

        Returns:
            Reason: The desired reason.
        """
        for reason in self.reasons:
            if reason.abbreviation == abbreviation:
                return reason
        
        raise ReasonError(abbreviation, "doesntexist")

    def create_reason(self, abbreviation: str, description: str):
        """Creates a new reason.

        Args:
            abbreviation (str): The abbreviation for the new reason.
            description (str): The description for the new reason.

        Raises:
            ReasonError: Thrown if a reason with this abbreviation already exists.

        Returns:
            Reason: Returns the reason that was just created.
        """
        if self.does_reason_exist(abbreviation):
            raise ReasonError(abbreviation, 
                "exists")

        reason = Reason(abbreviation, description)
        self.reasons.append(reason)

        self.save_file()

        return reason

    def delete_reason(self, abbreviation: str):
        """Deletes a reason based on its abbreviation.

        Args:
            abbreviation (str): Abbreviation of the reason to be deleted.

        Raises:
            ReasonError: Raised if no reason with given abbreviation found.
        
        Returns:
            Reason: The reason that was just deleted.
        """
        for reason in self.reasons:
            if reason.abbreviation == abbreviation:
                self.reasons.remove(reason)

                self.save_file()

                return(reason)
        
        raise ReasonError(abbreviation, "doesntexist")

    
    def does_removal_reason_exist(self, abbreviation: str):
        """Only for internal use, do not call outside of class, Use get_removal_reason instead for consistency. Checks if a reasons exists.

        Args:
            abbreviation (str): Abbreviation of the reason to be checked.

        Returns:
            bool: True if the reason exists, else false.
        """
        for reason in self.removalReasons:
            if reason.abbreviation == abbreviation:
                return True
        
        return False
        
    def get_removal_reason(self, abbreviation: str):
        """Gets a reason based on its abbreviation. 

        Args:
            abbreviation (str): Abbreviation of the reason to be gotten.

        Raises:
            ReasonError: Thrown if the reason doesn't exist

        Returns:
            RemovalReason: The desired reason.
        """
        for reason in self.removalReasons:
            if reason.abbreviation == abbreviation:
                return reason

        raise ReasonError(abbreviation, 
            "doesntexist")

    def create_removal_reason(self, abbreviation: str, description: str, turfjeCount: int):
        """Creates a new reason.

        Args:
            abbreviation (str): The abbreviation for the new reason.
            description (str): The description for the new reason.
            turfjeCount (int): The amount of turfjes the new reason should remove.

        Raises:
            ReasonError: Thrown if a reason with this abbreviation already exists.

        Returns:
            RemovalReason: Returns the reason that was just created.
        """
        if self.does_removal_reason_exist(abbreviation):
            raise ReasonError(abbreviation, 
                "exists")

        reason = RemovalReason(abbreviation, description, turfjeCount)
        self.removalReasons.append(reason)

        self.save_file()

        return reason

    def delete_removal_reason(self, abbreviation: str):
        """Deletes a reason based on its abbreviation.

        Args:
            abbreviation (str): Abbreviation of the reason to be deleted.

        Raises:
            ReasonError: Raised if no reason with given abbreviation found.
        
        Returns:
            RemovalReason: The reason that was just deleted.
        """
        for reason in self.removalReasons:
            if reason.abbreviation == abbreviation:
                self.removalReasons.remove(reason)

                self.save_file()

                return reason

        raise ReasonError(abbreviation, "doesntexist")

    def save_file(self):
        """Adjusted version of ManagerBase.save_file(), does not need to be provided data.
        """
        # convert objects into dicts to make settings serializable
        serializedSettings = {
            'reasons': [],
            'removalReasons': []
        }

        serializedSettings['reasons'] = [{
            'abbreviation': reason.abbreviation,
            'description': reason.description
        } for reason in self.reasons]

        serializedSettings['removalReasons'] = [{
            'abbreviation': reason.abbreviation,
            'description': reason.description,
            'turfjeCount': reason.turfjeCount
        } for reason in self.removalReasons]

        super().save_file(serializedSettings)

    def reset(self):
        """Empty out reason and removal reason lists and reset to no data. WARNING: REMOVES ALL CURRENTLY STORED REASONS IMMEDIATELY.
        """
        self.settings = {
            'reasons': [],
            'removalReasons': []
        }

        self.reasons = []
        self.removalReasons = []

        self.save_file()
