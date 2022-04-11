from np_mobile_obj import NPMobileObj
import random
import config as cf


# Defining Flower Class
class Flower(NPMobileObj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    def move_flower(self):
        self.sprite.rect[1] += cf.TAX_UPDATE_Y_FLOWER
        if self.sprite.rect[1] > cf.LIM_Y_FLOWER:
            self.sprite.kill()
            self.__init__ ("assets/flower1.png", random.randrange(0, cf.SIZE_WINDOW_X - 40),
                           cf.INITIAL_POSITION_FLOWER_Y)
