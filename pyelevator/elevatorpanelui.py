import pygame
import pygame.locals
from .elevator import Elevator

pygame.init()


class ButtonUI:
    button_image = None
    button_lit_image = None
    font = pygame.font.Font(None, 28)
    foreground = pygame.Color("black")

    def __init__(self, controller, elevator, floor, rect):
        self.controller = controller
        self.elevator = elevator
        self.floor = floor
        self.rect = rect
        if self.button_image is None:
            self.button_image = pygame.transform.scale(
                pygame.image.load("images/button.png"),
                (self.rect.width - 5, self.rect.width - 5)
            )
        if self.button_lit_image is None:
            self.button_lit_image = pygame.transform.scale(
                pygame.image.load("images/button-lit.png"),
                (self.rect.width - 5, self.rect.width - 5)
            )
        self.text_surface = pygame.transform.scale(
            self.font.render(self.floor.name, 1, self.foreground),
            (self.rect.width - 12, self.rect.width - 12)
        )
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = rect.center

    def draw(self, surface):
        if self.elevator.buttons[self.floor]:
            surface.blit(self.button_lit_image, self.rect)
        else:
            surface.blit(self.button_image, self.rect)
        surface.blit(self.text_surface, self.text_rect)

    def click(self, surface, point):
        if self.rect.collidepoint(point):
            self.controller.on_elevator_panel_button_pushed(self.elevator, self.floor)


class ElevatorPanelUI:
    background = pygame.Color("green")

    def __init__(self, ui, elevator, rect):
        self.ui = ui
        self.elevator = elevator
        self.rect = rect

        floors = elevator.buttons.keys()
        cols = 4
        rows = (len(floors)+cols-1)/cols
        button_rect = pygame.Rect(0, 0, (self.rect.width - 10) / cols,(self.rect.height - 10) / rows)

        self.buttons = []
        for floor in floors:
            x = self.rect.left + (floor.index % cols) * button_rect.width
            y = self.rect.top + int(floor.index / cols) * button_rect.height
            self.buttons.append(ButtonUI(ui.controller, elevator, floor, button_rect.move(x, y)))

    def draw(self, surface):
        pygame.draw.rect(surface, self.background, self.rect)
        for button in self.buttons:
            button.draw(surface)

    def click(self, surface, point):
        for button in self.buttons:
            button.click(surface, point)

