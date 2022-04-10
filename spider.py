from obj import Obj
import config as cf

class Spider(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        self.spider_obj = Obj(image, x, y)