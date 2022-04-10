from obj import Obj
import config as cf
import random



class NPMobileObj(Obj):
    def __init__(self, image, x, y):
        super ().__init__ (image, x, y)
    def movement(self, speed_var):
        self.sprite.rect[1] += speed_var



    def reposition(self, initial_position_y, final_position_y):
        if self.sprite.rect[1] >= initial_position_y:
            self.sprite.rect[1] = final_position_y
#"assets/spider1.png"
