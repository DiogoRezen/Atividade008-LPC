import pygame
from menu import Menu
from gameover import GameOver
from game import Game
from config import SIZE_WINDOW_X, SIZE_WINDOW_Y, DEFAULT_LIFE_BEE, DEFAULT_PTS_BEE, N_TICKS


class Main:

    def __init__(self):
        
        pygame.init()  
        pygame.mixer.init()                                     
        pygame.mixer.music.load("assets/sounds/bg.ogg")         
        pygame.mixer.music.play(-1)                            
       
        self.window = pygame.display.set_mode([SIZE_WINDOW_X, SIZE_WINDOW_Y])           
        self.title = pygame.display.set_caption("Bee Honey Infinity Runner")              
        self.loop = True        
        self.fps = pygame.time.Clock()                   
        self.start_screen = Menu("assets/start.png")
        self.game = Game()
        self.gameover = GameOver("assets/gameover.png")

    def draw(self):
   
        self.window.fill([0, 0, 0])
        if self.start_screen.change_scene == False:
            self.start_screen.draw(self.window)
        elif self.game.change_scene == False:
            self.game.draw(self.window)
            self.game.update()
        elif self.gameover.change_scene == False:
            self.gameover.draw(self.window)
        else:
            self.start_screen.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.bee.life = DEFAULT_LIFE_BEE
            self.game.bee.pts = DEFAULT_PTS_BEE
                                                                
    def events(self):
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            if self.start_screen.change_scene == False:
                self.start_screen.event(event)
            elif self.game.change_scene == False:
                self.game.bee.move_bee(event)
            else:
                self.gameover.event(event) 

    def update(self):
        while self.loop:
            self.fps.tick(N_TICKS)                   
            self.draw()
            self.events()
            pygame.display.update()
