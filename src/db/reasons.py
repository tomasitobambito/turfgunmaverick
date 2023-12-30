class Reason():
    """Model class for reasons.
    """
    def __init__(self, abbreviation: str, description: str):
        self.abbreviation = abbreviation
        self.description = description

class RemovalReason(Reason):
    """Model class for removal reasons.

    Inherits from Reason.
    """
    def __init__(self, abbreviation: str, description: str, turfjeCount: int):
        super().__init__(abbreviation, description)

        self.turfjeCount = turfjeCount