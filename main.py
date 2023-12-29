from src.database import DataBase
from src.turfje import TurfjeManager
import time
from src.reasons import RemovalReason

turfjes = TurfjeManager()
reason = RemovalReason('hello', 'im a description', 2)

turfjes.remove_turfje_by_person(0, reason)