import pygame
from obj import Obj
import config as cf
import random

class Flower(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        self.flower_obj = Obj(image, x, y)
        #("assets/florwer1.png",random.randrange(0, cf.SIZE_WINDOW_X - 40), cf.POSITION_Y_FLOWER)
    
#    def move_flower(self,y):
                                                    #função responsavel por movimentar/transladar a
                                                    #flor pela pela
#        self.flower.sprite.rect[1] += cf.TAX_UPDATE_Y_FLOWER
                                                    #objeto flor desce a tela a uma taxa de 6 pixels a
                                                    #cada frame

#        if self.flower.sprite.rect[1] > cf.LIM_Y_FLOWER:
#            self.flower.sprite.kill()       #ao sair da tela, na parte inferior,
                                                    #o objeto flor é eliminado
#            self.flower = Obj("assets/florwer1.png", random.randrange(0, cf.SIZE_WINDOW_X - 40), cf.INITIAL_POSITION_FLOWER_Y)
                                                    #após a primeira flor ser eliminada pela função
                                                    #sprite.kill(), com a chamada do método update(),
                                                    #que chama o método move_spiders(), da classe Game,
                                                    #temo a criação de uma nova flor em uma posição, também,
                                                    #aleatória, no inicio da tela de jogo, na parte superior
                                                    #da janela do jogo.
            #print("flor morreu")