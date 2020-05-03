
class Elevator:
    __max_speed = 0.1  # meters/second

    def __init__(self, controller, floors, name: str, index: int):
        self.controller = controller
        self.destination = None
        self.elevation = floors[0].elevation  # meters
        self.velocity = 0.0  # meters/second
        self.name = name
        self.index = index
        self.buttons = {floor: False for floor in floors}

    def __str__(self):
        return f"{self.name} h={self.elevation} v={self.velocity}"

    def tick(self):
        if self.destination is not None:
            distance = self.destination.elevation - self.elevation
            if distance > 0.1:
                self.velocity = self.__max_speed
            elif distance < -0.1:
                self.velocity = -self.__max_speed
            else:
                self.velocity = 0.0
                self.controller.on_elevator_arrived(self)

            self.elevation += self.velocity
