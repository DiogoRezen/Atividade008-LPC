import pygame
from obj import Obj
import config as cf


class Menu:

    def __init__(self, image):

        self.bg = Obj(image, cf.INIT_X, cf.INIT_Y)

        self.change_scene = False

    def draw(self, window):
        self.bg.draw(window)                

    def event(self, event):
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_RETURN:
                self.change_scene = True


class GameOver(Menu):
    
    def __init__(self, image):
        super().__init__(image)

                                
