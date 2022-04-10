from obj import Obj
import config as cf
import random


class Spider(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)



    def move_spider(self):
        self.sprite.rect[1] += cf.TAX_UPDATE_Y_SPIDER
        if self.sprite.rect[1] > cf.LIM_Y_SPIDER:
            self.sprite.kill()
            self.__init__("assets/spider1.png", random.randrange(0, cf.SIZE_WINDOW_X - 40),
                          cf.POSITION_Y_SPIDER)

