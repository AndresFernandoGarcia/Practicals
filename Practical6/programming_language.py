class ProgrammingLanguage:

    def __init__(self, name, typing,reflection,year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, {}, {}".format(self.name, self.typing, self.reflection, self.year)

    def is_Dynamic(self):
        return self.typing == 'Dynamic'

    def get_Name(self):
        return self.name

