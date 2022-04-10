from bee import Bee
from text import Text
from spider import Spider
from flower import Flower
import config as cf
import random
from np_mobile_obj import NPMobileObj


class Game:

    def __init__(self):

        self.bg = NPMobileObj("assets/bg.png", cf.INIT_X, cf.INIT_Y)            
        self.bg2 = NPMobileObj("assets/bg.png", cf.INIT_X, cf.POSITION_Y_BG2)                                                                
        self.spider1 = Spider("assets/spider1.png",random.randrange(0, cf.SIZE_WINDOW_X - 40), cf.POSITION_Y_SPIDER)                                                      
        self.flower1 = Flower("assets/florwer1.png",random.randrange(0, cf.SIZE_WINDOW_X - 40), cf.POSITION_Y_FLOWER)                                           
        self.bee = Bee("assets/bee1.png",cf.INITIAL_POSITION_BEE_X,cf.INITIAL_POSITION_BEE_Y)
        self.change_scene = False           
        self.score = Text(cf.SIZE_TEXT_SCORE,cf.INIT_TEXT_SCORE)
        self.lifes = Text(cf.SIZE_TEXT_LIFES,cf.INIT_TEXT_LIFES)

    def draw(self, window):                 
        self.bg.draw(window)             
        self.bg2.draw(window)            
        self.bee.draw(window)                      
        self.flower1.draw(window)
        self.spider1.draw(window)        
        self.score.draw(window,cf.POSITION_TEXT_SCORE_X,cf.POSITION_TEXT_SCORE_Y)
        self.lifes.draw(window,cf.POSITION_TEXT_LIFES_X,cf.POSITION_TEXT_LIFES_Y)
                                       
    def update(self):
        self.bg.movement(cf.TAX_UPDATE_Y_BG)
        self.bg.reposition(cf.POS_INITIAL_Y_BG, 0)
        self.bg2.movement(cf.TAX_UPDATE_Y_BG2)
        self.bg2.reposition(0, cf.POS_INITIAL_Y_BG2)
        self.spider1.anim("spider", cf.N_TICKS_SPIDER, cf.N_SPRITES_SPIDER)    
        self.spider1.move_spider()                  
        self.flower1.anim("florwer", cf.N_TICKS_FLOWER, cf.N_SPRITES_FLOWER)               
        self.flower1.move_flower()
        self.bee.anim("bee", cf.N_TICKS_BEE, cf.N_SPRITES_BEE)       
        self.bee.colision(self.spider1.group, "Spider")                                           
        self.bee.colision(self.flower1.group, "Flower")                                        
        self.gameover()                  
        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(str(self.bee.life))
                                                   
    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True
