import pygame
import pygame.locals
import time
from .floorui import FloorUI
from .elevatorui import ElevatorUI
from .elevatorpanelui import ElevatorPanelUI

pygame.init()


class UI:
    background = pygame.Color("red")

    def __init__(self, width, height, controller):
        self.controller = controller
        self.surface_rect = pygame.Rect(0, 0, width, height)
        self.surface = pygame.display.set_mode(self.surface_rect.size)
        self.main_rect = pygame.Rect(5, 5, width-10, height-10)

        self.panels_rect = self.main_rect.copy()
        self.panels_rect.height = 100
        self.panels_rect.top = self.main_rect.bottom-100

        self.floors_rect = self.main_rect.copy()
        self.floors_rect.width = 100
        self.floors_rect.height -= self.panels_rect.height

        self.elevators_rect = self.main_rect.copy()
        self.elevators_rect.left = self.floors_rect.right
        self.elevators_rect.height -= self.panels_rect.height
        self.elevators_rect.width -= self.floors_rect.width

        floor_height = self.floors_rect.height / len(self.controller.floors)
        self.floor_uis = []
        for f in controller.floors:
            rect = self.floors_rect.copy()
            rect.height = floor_height
            rect.y = self.main_rect.top+(len(self.controller.floors)-1-f.index) * floor_height
            self.floor_uis.append(FloorUI(self, f, rect))

        elevator_width = self.elevators_rect.width / len(self.controller.elevators)
        self.elevator_uis = []
        self.elevator_paneluis = []
        for e in controller.elevators:
            rect = self.elevators_rect.copy()
            rect.width = elevator_width-5
            rect.x = self.elevators_rect.left + 5 + e.index * elevator_width
            self.elevator_uis.append(ElevatorUI(self, e, rect))

            rect_panel = rect.copy()
            rect_panel.height = self.panels_rect.height
            rect_panel.top = self.panels_rect.top
            self.elevator_paneluis.append(ElevatorPanelUI(self, e, rect_panel))

    def run(self):
        self.controller.on_floor_down_button_pushed(self.controller.floors[len(self.controller.floors)-1])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    self.click(event.pos)
            self.surface.fill(self.background)
            self.draw()
            pygame.display.flip()
#            time.sleep(0.05)
            self.controller.tick()

    def draw(self):
        for f in self.floor_uis:
            f.draw(self.surface)
        for e in self.elevator_uis:
            e.draw(self.surface)
        for p in self.elevator_paneluis:
            p.draw(self.surface)

    def click(self, point):
        for f in self.floor_uis:
            f.click(self.surface, point)
        for e in self.elevator_uis:
            e.click(self.surface, point)
        for p in self.elevator_paneluis:
            p.click(self.surface, point)




