import pygame
from obj import Obj
import config as cf


# Defining Bee Class
class Bee(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)
                                                                   
        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound("assets/sounds/score.ogg")
        self.sound_block = pygame.mixer.Sound("assets/sounds/collided.ogg")
        self.life = cf.DEFAULT_LIFE_BEE                                               
        self.pts = cf.DEFAULT_PTS_BEE                                                
        
    def move_bee(self, event):
        if event.type == pygame.MOUSEMOTION:                        
                                                                    
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] + cf.SHIFT_X_MOUSE    
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] + cf.SHIFT_Y_MOUSE    

    def collision(self, group, name):
        name = name
        collision = pygame.sprite.spritecollide(self.sprite, group, True)
                                                
        if name == "Flower" and collision:
            self.pts += 1                       
            self.sound_pts.play()
            print(self.pts)
        elif name == "Spider" and collision:
            self.life -= 1                      
            self.sound_block.play()
            print(self.life)
                                                
