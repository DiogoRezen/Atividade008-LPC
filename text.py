import pygame
import config as cf


# Defining Text Class
class Text:

    def __init__(self, size, text):
        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, False, cf.COLOR)       

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update_text(self, update):
        self.render = self.font.render(update, False, cf.COLOR)
