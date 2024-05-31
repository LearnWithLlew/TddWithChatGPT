class Part:
    def __init__(self, text, state):
        self.text = text
        self.state = state

    def is_unchanged(self):
        return self.state == 'unchanged'

    def is_removed(self):
        return self.state == 'removed'

    def is_added(self):
        return self.state == 'added'
