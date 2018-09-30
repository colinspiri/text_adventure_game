class Interaction:
    def __init__(self, preview, aftermath, action_text):
        self.preview = preview
        self.aftermath = aftermath
        self.interacted_with = False
        self.action_text = action_text

    def get_description(self):
        if not self.interacted_with:
            return self.preview
        else:
            return self.aftermath

    def get_preview(self):
        return self.preview

    def get_aftermath(self):
        return self.aftermath

    def has_been_interacted_with(self):
        return self.interacted_with

    def get_action_text(self):
        return self.action_text
