from src.settings import Settings
from src.usersettings import UserSettings


settings = Settings()
userSettings = UserSettings()

# print(settings.get_person_ID())
# print(settings.get_turfje_ID())
# print(settings.settings)
userSettings.create_reason('hel', 'hello im a reason')
# userSettings.delete_reason('hel')