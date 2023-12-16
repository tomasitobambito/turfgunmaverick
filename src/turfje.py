import time
import os.path

class Turfje:
    def __init__(self, person: Person, reason: Reason, creationDate: float = time.time()):
        self.person = person
        self.reason = reason
        self.creationDate = creationDate
        self.removed = False

class TurfjeManager:
    def __init__(self):
        self.turfjesDBPath = "./data/turfjes.json"