class Guitar:
    def __init__(self, name, year, cost):
        """Construct a Guitar object from given values"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation from Guitar object"""
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Function to get 2019 minus the year the guitar was released"""
        return 2019 - self.year

    def is_vintage(self):
        """Checks if 2019 minus the year the guitar was released is equal or greater than 50"""
        return self.get_age() >= 50

    def get_name(self):
        """Gets the name of the guitar from the Guitar object"""
        return self.name

    def get_year(self):
        """Gets the year the guitar was released from the Guitar object"""
        return self.year

    def get_cost(self):
        """Gets the cost of the guitar from the Guitar object"""
        return self.cost
