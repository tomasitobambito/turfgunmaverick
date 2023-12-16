class ReasonError(Exception):
    def __init__(self, abbreviation, type):
        if type == 'exists':
            self.message = (f"A reason with this abbreviation already exists: {abbreviation}")
        elif type == 'doesntexist':
            self.message = (f"No reason with this abbreviation found: {abbreviation}")

        super().__init__(self.message)