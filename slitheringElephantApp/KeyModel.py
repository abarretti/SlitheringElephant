class KeyModel:

    key = 'DarthSkywalker456'

    def __init__(self, submittedKey):
        self.submittedKey = submittedKey

    def isKey(self):
        return self.key == self.submittedKey
