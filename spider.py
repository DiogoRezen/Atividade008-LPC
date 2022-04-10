from obj import Obj
import config as cf

class Spider(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)



    def move_spider(self):
        self.sprite.rect[1] += cf.TAX_UPDATE_Y_SPIDER

