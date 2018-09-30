class PlayerCharacter:
    def __init__(self, starting_location):
        self.current_location = starting_location

    def get_current_location(self):
        return self.current_location

    def set_current_location(self, new_location):
        self.current_location = new_location
