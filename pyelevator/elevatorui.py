import pygame
import pygame.locals
from .elevator import Elevator

pygame.init()


class ElevatorUI:
    background = pygame.Color("white")
    elevator_image = None

    def __init__(self, ui, elevator: Elevator, rect):
        self.ui = ui
        self.elevator = elevator
        self.rect = rect
        if self.elevator_image is None:
            self.elevator_image = pygame.transform.scale(
                                        pygame.image.load("images/elevator.png"),
                                        (self.rect.width - 10, self.rect.width - 10)
                                )

    def draw(self, surface):
        pygame.draw.rect(surface, self.background, self.rect)

        elevation = self.elevator.elevation/self.ui.controller.floors[-1].elevation
        elevator_rect = self.elevator_image.get_rect()
        x = self.rect.left + 5
        y = self.rect.top + int((self.rect.height-elevator_rect.height)*(1-elevation))
        surface.blit(self.elevator_image, elevator_rect.move(x, y))

    def click(self, surface, point):
        pass
