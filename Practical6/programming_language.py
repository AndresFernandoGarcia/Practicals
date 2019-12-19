class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        # Construct a ProgrammingLanguage object from given values
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        # Return string representation from ProgrammingLanguage object
        return "{}, {} Typing, {}, {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        # Function to check if programming language is dynamically typed
        return self.typing == 'Dynamic'

    def get_name(self):  # gets name
        # function to get the name of the programming language from the programming language object
        return self.name
