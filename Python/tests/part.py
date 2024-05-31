class Part:
    def __init__(self, text, status):
        self.text = text
        self.status = status

    def is_unchanged(self):
        return self.status == "unchanged"

    def is_removed(self):
        return self.status == "removed"

    def is_added(self):
        return self.status == "added"

    def __str__(self):
        return f"`{self.text}`[{self.status}]"
