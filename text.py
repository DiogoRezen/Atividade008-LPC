import pygame
import config as cf

class Text:

    def __init__(self, size, text):

        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, False, cf.COLOR)
                                                #a variavel self.render é usada
                                                #para colocar o texto que vai
                                                #para a tela.        

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update_text(self, update):
        self.render = self.font.render(update, False, cf.COLOR)