from src.db.managerBase import ManagerBase
from src.exceptions import PersonDoesNotExistError

class Person():
    def __init__(self, id: int, name: str, position: str):
        self.id = id
        self.name = name
        self.position = position


class PersonManager(ManagerBase):
    """Class that manages the list of people in the committee.

    Args:
        Inherits from ManagerBase.
    """
    def __init__(self):
        super().__init__('./data/people.json')

        self.people = self.read_file()

        self.people = [Person(
            person['id'], 
            person['name'], 
            person['position'])
            for person in self.people]


    def create_person(self, id: int, name: str, position: str):
        """Creates new person in the internal manager. DOES NOT check if Id is valid.

        Args:
            id (int): The persons ID.
            name (str): The name of the person.
            position (str): The position of the person in the committe.
        """
        newPerson = Person(id, name, position)

        self.people.append(newPerson)

        self.save_file()

    
    def get_person(self, id: int):
        """Gets a person based on their ID.

        Args:
            id (int): The ID of the person to be gotten.

        Raises:
            PersonDoesNotExistError: Raised when no person with ID is found.

        Returns:
            Person: Person with the given ID.
        """
        for person in self.people:
            if id == person.id:
                return person

        raise PersonDoesNotExistError(id)


    def update_person(self, id: int, name: str, position: str):
        """Updates a person based on their ID.

        Args:
            id (int): The ID of the person to be updated.
            name (str, optional): New name for the person. '' is processed as original name.
            position (str, optional): New position for the person. '' is processed as original position.
        """
        person = self.get_person(id)

        updatedPerson = Person(
            id,
            person.name if name == '' else name,
            person.position if position == '' else position)

        self.people.remove(person)
        self.people.append(updatedPerson)

        self.save_file()


    def delete_person(self, id: int):
        """Deletes a person from the internal manager.

        Args:
            id (int): ID of the person to be deleted.
        """
        person = self.get_person(id)

        self.people.remove(person)

        self.save_file()

    
    def save_file(self):
        """Adjusted version of ManagerBase.save_file, specific to PersonManager. Called without providing data
        """
        serializedList = [{
            'id': person.id,
            'name': person.name,
            'position': person.position
        } for person in self.people]

        super().save_file(serializedList)


    def reset(self):
        """Empty out person list and reset to no data. WARNING: REMOVES ALL CURRENTLY STORED PEOPLE IMMEDIATELY.
        """
        self.people = []

        self.save_file()