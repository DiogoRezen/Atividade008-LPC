import pygame
from menu import Menu, GameOver
from obj import Obj, Bee, Text
import random


class Game:
    #loop = True

    def __init__(self):

        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/bg.ogg")
        pygame.mixer.music.play(-1)

        self.window = pygame.display.set_mode([360, 640])
        self.title = pygame.display.set_caption("Bee Honey")

        self.loop = True
        self.fps = pygame.time.Clock()

        self.start_screen = Menu("assets/start.png")
        #self.game = Game()
        self.gameover = GameOver("assets/gameover.png")
        
        self.bg = Obj("assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/bg.png", 0, -640)

        self.spider = Obj("assets/spider1.png", random.randrange(0, 320), -50)
        self.flower = Obj("assets/florwer1.png", random.randrange(0, 320), 200)
        self.bee = Bee("assets/bee1.png", 150, 600)

        self.change_scene = False

        self.score = Text(120, "0")
        self.lifes = Text(60, "3")

        #instancias da antiga classe menu
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            if not self.start_screen.change_scene:
                self.start_screen.event(event)
            elif not self.game.change_scene:
                self.game.bee.move_bee(event)
            else:
                self.gameover.event(event)        

    def draw(self):
        self.window.fill([0, 0, 0])
        if not self.start_screen.change_scene:
            self.start_screen.draw(self.window)

        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        elif not self.gameover.change_scene:
            self.gameover.draw(self.window)
        else:
            self.start_screen.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.bee.life = 3
            self.game.bee.pts = 0
            #self.window onde era só window daqui até o fim do metodo draw
            self.bg.draw(self.window)
            self.bg2.draw(self.window)
            self.bee.draw(self.window)
            self.spider.draw(self.window)
            self.flower.draw(self.window)
            self.score.draw(self.window, 160, 50)
            self.lifes.draw(self.window, 50, 50)

    def update(self):

        self.move_bg()
        self.spider.anim("spider", 8, 5)
        self.flower.anim("florwer", 8, 3)
        self.bee.anim("bee", 2, 5)
        self.move_spiders()
        self.move_flower()
        self.bee.colision(self.spider.group, "Spider")
        self.bee.colision(self.flower.group, "Flower")
        self.gameover()
        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(str(self.bee.life))

    def move_bg(self):
        self.bg.sprite.rect[1] += 10
        self.bg2.sprite.rect[1] += 10

        if self.bg.sprite.rect[1] > 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] > 0:
            self.bg2.sprite.rect[1] = -640

    def move_spiders(self):
        self.spider.sprite.rect[1] += 11

        if self.spider.sprite.rect[1] > 640:
            self.spider.sprite.kill()
            self.spider = Obj("assets/spider1.png", random.randrange(0, 320), -50)

    def move_flower(self):
        self.flower.sprite.rect[1] += 8

        if self.flower.sprite.rect[1] > 640:
            self.flower.sprite.kill()
            self.flower = Obj("assets/florwer1.png", random.randrange(0, 320), -100)

    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True

    def menu(self, image):
        self.bg = Obj(image, 0, 0)

        self.change_scene = False

    def draw(self, window):
        self.bg.draw(window)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True

#class GameOver(Menu):

#    def __init__(self, image):
#        super().__init__(image)    

    def updates(self):                    
        self.fps.tick(30)
        self.draw(self)
        self.events(self)
        pygame.display.update()
