from src.db.managerBase import ManagerBase
from src.db.reasons import Reason, RemovalReason
from src.exceptions import ReasonError


class UserSettings(ManagerBase):
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
        for reason in self.reasons:
            if reason.abbreviation == abbreviation:
                return True
        
        return False

    def get_reason(self, abbreviation: str):
        for reason in sdb.elf.reasons:
            if reason.abbreviation == abbreviation:
                return reason
        
        raise ReasonError(abbreviation, "doesntexist")

    def create_reason(self, abbreviation: str, description: str):
        if self.does_reason_exist(abbreviation):
            raise ReasonError(abbreviation, 
                "exists")

        reason = Reason(abbreviation, description)
        self.reasons.append(reason)

        self.save_file()

        return reason

    def delete_reason(self, abbreviation: str):
        for reason in self.reasons:
            if reason.abbreviation == abbreviation:
                self.reasons.remove(reason)

                self.save_file()

                return(reason)
        
        raise ReasonError(abbreviation, "doesntexist")

    
    def does_removal_reason_exist(self, abbreviation: str):
        for reason in self.removalReasons:
            if reason.abbreviation == abbreviation:
                return True
        
        return False
        
    def get_removal_reason(self, abbreviation: str):
        for reason in self.removalReasons:
            if reason.abbreviation == abbreviation:
                return reason

        raise ReasonError(abbreviation, 
            "doesntexist")

    def create_removal_reason(self, abbreviation: str, description: str, turfjeCount: int):
        if self.does_removal_reason_exist(abbreviation):
            raise ReasonError(abbreviation, 
                "exists")

        reason = RemovalReason(abbreviation, description, turfjeCount)
        self.removalReasons.append(reason)

        self.save_file()

        return reason

    def delete_removal_reason(self, abbreviation: str):
        for reason in self.removalReasons:
            if reason.abbreviation == abbreviation:
                self.removalReasons.remove(reason)

                self.save_file()

                return reason

        raise ReasonError(abbreviation, "doesntexist")

    def save_file(self):
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
        self.settings = {
            'reasons': [],
            'removalReasons': []
        }

        self.reasons = []
        self.removalReasons = []

        self.save_file()
