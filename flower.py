from obj import Obj
import config as cf

class Flower(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        self.flower_obj = Obj(image, x, y)