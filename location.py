class Location:
    def __init__(self, description1, description2 ):
        self.description1 = description1
        self.description2 = description2
        self.exits = []
        self.interactions = []

    def show(self):
        returned = self.description1

        # Show previews or aftermath of interactions
        for interaction in self.interactions:
            returned += interaction.get_description()

        returned += self.description2

        # Show descriptions of exits
        for exit in self.exits:
            returned += exit.get_description()

        print(returned)

    def get_description(self):
        return self.description1 + self.description2

    def get_exits(self):
        return self.exits

    def get_interactions(self):
        return self.interactions

    def add_exit(self, new_exit):
        self.exits.append(new_exit)

    def add_interaction(self, new_interaction):
        self.interactions.append(new_interaction)
