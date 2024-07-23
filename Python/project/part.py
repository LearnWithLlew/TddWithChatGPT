class Part:
    def __init__(self, text, change_type):
        self.text = text
        self.change_type = change_type

    def is_unchanged(self):
        return self.change_type == 'unchanged'

    def is_removed(self):
        return self.change_type == 'removed'

    def is_added(self):
        return self.change_type == 'added'
