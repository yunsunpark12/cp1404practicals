class ProgrammingLanguage:
    def __init__(self, field='', typing='', reflection='', year=''):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == 'Dynamic' or self.typing == 'dynamic':
            print(self.field)
            return True
        else:
            return False

    def __str__(self):
        return