
class Floor:
    def __init__(self, controller, name, index, elevation):
        self.controller = controller
        self.name = name
        self.index = index
        self.elevation = elevation  # meters above lowest floor in shaft
        self.up_button = False
        self.down_button = False

    def __str__(self):
        return self.name

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self.name == other.name
