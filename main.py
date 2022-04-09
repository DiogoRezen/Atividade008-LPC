import pygame
#from obj import Obj
from menu import Menu
from gameover import GameOver
from game import Game
from config import SIZE_WINDOW_X, SIZE_WINDOW_Y, DEFAULT_LIFE_BEE, DEFAULT_PTS_BEE, N_TICKS


class Main:

    def __init__(self):#, sizex, sizey, title):
        
        pygame.init()
        
        pygame.mixer.init()                                     #iniciamos o mixer do pygame, para executar arquivos de audio
        pygame.mixer.music.load("assets/sounds/bg.ogg")         #a musica que será tocada durante o jogo
        pygame.mixer.music.play(-1)                             #a musica carregada na linha anterior será colocada
                                                                #para tocar em loop, e assim que ela terminar, inicia
                                                                #de novo
                                                                #A funcao pygame.mixer.music serve para reproducao
                                                                #de sons maiores, com extensão maior.

        #self.window = pygame.display.set_mode([sizex, sizey])   #funcoes do pygame
        #self.title = pygame.display.set_caption(title)          #funcoes do pygame
        self.window = pygame.display.set_mode([SIZE_WINDOW_X, SIZE_WINDOW_Y])           #funcoes do pygame
        self.title = pygame.display.set_caption("Bee Honey Infinity Runner")        #funcoes do pygame

        #self.menu = Menu()                                      #variavel self.menu armazena a
                                                                #a classe Menu()

        #self.game = Game()                                      #variavel self.game armazena a
                                                                #a classe ou objeto Game()

        self.loop = True

        #self.start_screen = Obj("assets/start.png", 0, 0)   #variavel que recebe a tela
                                                            #inicial
                                                            #Objeto criado com a tela inicial,
                                                            #a partir da classe Obj
        
        self.fps = pygame.time.Clock()                      #os sprites estao animados de forma muito rádida
                                                            #criamos esta variavel para controle
                                                            #da taxa de fps que o jogo terá
                                                            #A função time.Clock() é a perfeita para isso

        self.start_screen = Menu("assets/start.png")
        self.game = Game()
        self.gameover = GameOver("assets/gameover.png")

    def draw(self):
        #self.start_screen.drawing(self.window)             #Chame o metodo drawing da classe
                                                            #Obj para desenhar o objeto start_screen
                                                            #na tela
                                                            #Parece repetido ter draw aqui e em Obj,
                                                            #Mas aqui o draw() é craido para desenhar tudo em uma só funcao,
                                                            #abelha, flores, aranhas, tela, etc, e depois chamar só draw()
                                                            #no loop principal
        
        #self.window.fill([0,0,0])                       #preenche a tela com a cor preta, caso pressione enter
                                                        #variavel self.menu.change_scene adquire valor True quando
                                                        #o enter é pressionado, vindo essa mudança da classe menu, no
                                                        #no método events()
        
        #if self.menu.change_scene == False:             #ele chama como self.start_screen.chage_scene, que é uma variavel
                                                        #que está na classe menu, para apresentar a tela inicial que
                                                        #requisita pressionar enter para iniciar o jogo
        #    self.menu.draw(self.window)
                                                        #variavel change_scene da classe Menu é instanciada como False
                                                        #a partir do momento que ela for verdadeira, haverá a troca
                                                        #de tela
                                                        #Ela passa a ser verdadeira quando pressionarmos a tecla enter
            
                                                        #da variavel self.menu, que armazena a classe Menu(),
                                                        #usando o método .draw() da classe Menu pois os parâmetros
                                                        #do método é o self.window (local onde será desenhado
                                                        #os objetos de Menu, que está em self.menu

        #else:# self.game.change_scene == False:            
        #    self.game.draw(self.window)
                                                        #variavel change_scene da classe Game é instanciada como False
                                                        #a partir do momento que ela for verdadeira, haverá a troca
                                                        #de tela, e será desenhada a cena/tela do jogo
        #    self.game.update()
                                                        #será desenhada, também, todas as atualizacoes da tela
                                                        #conforme qualquer atualização do método update(), da classe
                                                        #Game for sendo iterado
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
        #for events in pygame.event.get():
            #if events.type == pygame.QUIT:
            #    self.loop = False
                
            #if self.menu.change_scene == False:     #ele chama como self.start_screen.chage_scene, que é uma variavel
                                                    #que está na classe menu, para apresentar a tela inicial que
                                                    #requisita pressionar enter para iniciar o jogo

            #    self.menu.events(events)            #os eventos de menu, no caso, verifica se pressionou
                                                    #enter para poder mudar de cena.

            #elif self.game.change_scene == False:   #os eventos da abelha só ocorrem enquanto a variavel de estado
                                                    #self.game.change_scene for false. Quando ela for verdadeira,
                                                    #ou seja, for para a tela de menu ou de gameover, os eventos da
                                                    #abelha param devido ao elif só deixar eles ocorrerem enquando
                                                    #self.game.change_scene for false.
                
            #    self.game.bee.move_bee(events)      #pega a variavel self.game e verifica o evento de
                                                    #movimento da abelha, associado ao movimento do
                                                    #cursor do mouse. O evento associado ao movimento do
                                                    #cursor do mouse é o usado no metodo move_bee, da
                                                    #classe Bee, que herdou tudo de Obj, e tem seus
                                                    #próprios métodos particulares, como o metodo move_bee()
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
            self.fps.tick(N_TICKS)                       #a cada segundo, a função .tick(), do objeto self.fps
                                                    #criado no construtor __int__(), da classe Main, carregará
                                                    #30 imagens na cada segundo na tela.
                                                    #Por isso foi colocado dentro do laço while
            self.draw()
            self.events()
            pygame.display.update()


#game = Main(360, 640, "BeeHoney")
#game.update()
#Main().update()
