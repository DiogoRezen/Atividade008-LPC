import pygame

from bee import Bee
from text import Text
from menu import Menu
from spider import Spider
from flower import Flower
from gameover import GameOver
import config as cf
import random
from np_mobile_obj import NPMobileObj
from config import (
    SIZE_WINDOW_X,
    SIZE_WINDOW_Y,
    DEFAULT_LIFE_BEE,
    DEFAULT_PTS_BEE,
    N_TICKS,
)


class Game:
    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/bg.ogg")
        pygame.mixer.music.play(-1)

        self.window = pygame.display.set_mode([SIZE_WINDOW_X, SIZE_WINDOW_Y])
        pygame.display.set_caption("Bee Honey Infinity Runner")
        self.loop = True
        self.fps = pygame.time.Clock()
        self.start_screen = Menu("assets/start.png")
        self.game_over = GameOver("assets/game_over.png")
        self.bg = NPMobileObj("assets/bg.png", cf.INIT_X, cf.INIT_Y)
        self.bg2 = NPMobileObj("assets/bg.png", cf.INIT_X, cf.POSITION_Y_BG2)
        self.spider1 = Spider(
            "assets/spider1.png",
            random.randrange(0, cf.SIZE_WINDOW_X - 40),
            cf.POSITION_Y_SPIDER,
        )
        self.flower1 = Flower(
            "assets/flower1.png",
            random.randrange(0, cf.SIZE_WINDOW_X - 40),
            cf.POSITION_Y_FLOWER,
        )
        self.bee = Bee(
            "assets/bee1.png",
            cf.INITIAL_POSITION_BEE_X,
            cf.INITIAL_POSITION_BEE_Y,
        )
        self.change_scene = False
        self.score = Text(cf.SIZE_TEXT_SCORE, cf.INIT_TEXT_SCORE)
        self.lives = Text(cf.SIZE_TEXT_LIVES, cf.INIT_TEXT_LIVES)

    def update(self):
        while self.loop:
            self.fps.tick(N_TICKS)
            self.draw_screen()
            self.events()
            pygame.display.update()

    def draw(self, window):
        self.bg.draw(window)
        self.bg2.draw(window)
        self.bee.draw(window)
        self.flower1.draw(window)
        self.spider1.draw(window)
        self.score.draw(
            window, cf.POSITION_TEXT_SCORE_X, cf.POSITION_TEXT_SCORE_Y
        )
        self.lives.draw(
            window, cf.POSITION_TEXT_LIVES_X, cf.POSITION_TEXT_LIVES_Y
        )

    def update_objs(self):
        self.bg.movement(cf.TAX_UPDATE_Y_BG)
        self.bg.reposition(cf.POS_INITIAL_Y_BG, 0)
        self.bg2.movement(cf.TAX_UPDATE_Y_BG2)
        self.bg2.reposition(0, cf.POS_INITIAL_Y_BG2)
        self.spider1.anim("spider", cf.N_TICKS_SPIDER, cf.N_SPRITES_SPIDER)
        self.spider1.move_spider()
        self.flower1.anim("flower", cf.N_TICKS_FLOWER, cf.N_SPRITES_FLOWER)
        self.flower1.move_flower()
        self.bee.anim("bee", cf.N_TICKS_BEE, cf.N_SPRITES_BEE)
        self.bee.collision(self.spider1.group, "Spider")
        self.bee.collision(self.flower1.group, "Flower")
        self.game_over_check()
        self.score.update_text(str(self.bee.pts))
        self.lives.update_text(str(self.bee.life))

    def game_over_check(self):
        if self.bee.life <= 0:
            self.change_scene = True

    def draw_screen(self):
        self.window.fill([0, 0, 0])
        if self.start_screen.change_scene is False:
            self.start_screen.draw(self.window)
        elif self.change_scene is False:
            self.draw(self.window)
            self.update_objs()
        elif self.game_over.change_scene is False:
            self.game_over.draw(self.window)
        else:
            self.start_screen.change_scene = False
            self.change_scene = False
            self.game_over.change_scene = False
            self.bee.life = DEFAULT_LIFE_BEE
            self.bee.pts = DEFAULT_PTS_BEE

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
                pygame.quit()
            if self.start_screen.change_scene is False:
                self.start_screen.event(event)
            elif self.change_scene is False:
                self.bee.move_bee(event)
            else:
                self.game_over.event(event)
