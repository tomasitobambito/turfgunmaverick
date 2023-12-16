class Reason():
    def __init__(self, abbreviation: str, description: str):
        self.abbreviation = abbreviation
        self.description = description

class RemovalReason(Reason):
    def __init__(self, abbreviation: str, description: str, turfjeCount: int):
        super().__init__(abbreviation, description)

        self.turfjeCount = turfjeCount