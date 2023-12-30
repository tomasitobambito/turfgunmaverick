class ReasonError(Exception):
    """Exception thrown when an error with non-existant or duplicate reason abbreviations is found.

    Inherits from Exception
    """
    def __init__(self, abbreviation, type):
        if type == 'exists':
            self.message = (f"A reason with this abbreviation already exists: {abbreviation}")
        elif type == 'doesntexist':
            self.message = (f"No reason with this abbreviation found: {abbreviation}")

        super().__init__(self.message)


class TurfjeDoesNotExistError(Exception):
    """Exception thrown when a turfje can not be found.

    Inherits from Exception
    """
    def __init__(self, id):
        super().__init__(f"Turfje with id {id} does not exist.")


class PersonDoesNotExistError(Exception):
    """Exception thrown when a person can not be found.

    Inherits from Exception
    """
    def __init__(self, id):
        super().__init__(f"Person with id {id} does not exist.")