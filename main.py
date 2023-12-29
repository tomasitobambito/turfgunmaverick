from src.db.database import DataBase
from src.db.turfje import TurfjeManager
import time
from src.db.reasons import RemovalReason

turfjes = TurfjeManager()
reason = RemovalReason('hello', 'im a description', 2)

turfjes.remove_turfjes(0, reason)