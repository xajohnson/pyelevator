import pygame
import pygame.locals
from .floor import Floor

pygame.init()


class FloorUI:
    arrow_size = (20, 20)
    background = pygame.Color("blue")
    foreground = pygame.Color("white")
    up_image = None
    up_lit_image = None
    down_image = None
    down_lit_image = None
    font = pygame.font.Font(None, 28)

    def __init__(self, ui, floor: Floor, rect):
        self.ui = ui
        self.rect = rect
        self.floor = floor
        if self.up_image is None:
            self.up_image = pygame.transform.scale(pygame.image.load("images/up.png"), self.arrow_size)
        if self.down_image is None:
            self.down_image = pygame.transform.scale(pygame.image.load("images/down.png"), self.arrow_size)
        if self.up_lit_image is None:
            self.up_lit_image = pygame.transform.scale(pygame.image.load("images/up-lit.png"), self.arrow_size)
        if self.down_lit_image is None:
            self.down_lit_image = pygame.transform.scale(pygame.image.load("images/down-lit.png"), self.arrow_size)

        x = self.rect.left + 5
        y = self.rect.centery-self.arrow_size[0]/2
        self.up_arrow_rect = self.up_image.get_rect().move(x, y)
        x += self.arrow_size[0]+5
        self.down_arrow_rect = self.down_image.get_rect().move(x, y)
        x += self.arrow_size[0]+10
        self.text_surface = self.font.render(self.floor.name, 1, self.foreground)
        self.text_rect = self.text_surface.get_rect().move(x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.background, self.rect)

        if self.floor != self.ui.controller.floors[-1]:
            surface.blit(self.up_lit_image if self.floor.up_button else self.up_image, self.up_arrow_rect)
        if self.floor != self.ui.controller.floors[0]:
            surface.blit(self.down_lit_image if self.floor.down_button else self.down_image, self.down_arrow_rect)
        surface.blit(self.text_surface, self.text_rect)

    def click(self, surface, point):
        if self.up_arrow_rect.collidepoint(point):
            self.ui.controller.on_floor_up_button_pushed(self.floor)
        if self.down_arrow_rect.collidepoint(point):
            self.ui.controller.on_floor_down_button_pushed(self.floor)
