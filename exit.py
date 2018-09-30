class Exit:
    def __init__(self, direction, leads_to, description):
        self.direction = direction
        self.leads_to = leads_to
        self.description = description

    def get_direction(self):
        return self.direction

    def get_leads_to(self):
        return self.leads_to

    def get_description(self):
        return self.description
