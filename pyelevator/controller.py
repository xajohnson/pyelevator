from .elevator import Elevator
from .floor import Floor
import logging


class Controller:
    def __init__(self, num_elevators, num_floors):
        self.floors = []
        elevation = 0.0
        for f in range(0, num_floors):
            self.floors.append(Floor(self, "G" if f == 0 else str(f), f, elevation))
            elevation += 3.0

        self.elevators = []
        for e in range(0, num_elevators):
            self.elevators.append(Elevator(self, self.floors, f"Car {e}", e))
        self.time = 0

    def tick(self):
        for elevator in self.elevators:
            elevator.tick()
            logging.log(logging.INFO, f"{self.time}: {elevator}")
        self.time += 1

    def on_elevator_arrived(self, elevator):
        elevator.destination.up_button = False
        elevator.destination.down_button = False
        elevator.buttons[elevator.destination] = False
        elevator.destination = None
        for button, pushed in elevator.buttons.items():
            if pushed:
                elevator.destination = button
                break
        if elevator.destination is None:
            for floor in self.floors:
                if floor.up_button or floor.down_button:
                    elevator.destination = floor
                    break

    def on_floor_up_button_pushed(self, floor):
        floor.up_button = True
        for elevator in self.elevators:
            if elevator.destination is None:
                elevator.destination = floor
                break

    def on_floor_down_button_pushed(self, floor):
        floor.down_button = True
        for elevator in self.elevators:
            if elevator.destination is None:
                elevator.destination = floor
                break

    def on_elevator_panel_button_pushed(self, elevator, floor):
        elevator.buttons[floor] = True
        if elevator.destination is None:
            elevator.destination = floor
