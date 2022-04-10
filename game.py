from bee import Bee
from text import Text
from spider import Spider
from flower import Flower
import config as cf
import random
from np_mobile_obj import NPMobileObj


class Game:

    def __init__(self):

        self.bg = NPMobileObj("assets/bg.png", cf.INIT_X, cf.INIT_Y)            #bg é o background que será o
                                                        #o fundo da tela do jogo
        self.bg2 = NPMobileObj("assets/bg.png", cf.INIT_X, cf.POSITION_Y_BG2)        #bg2 é o background que será o
                                                        #o fundo da tela do jogo. Ele
                                                        #ficará em clico com bg para que
                                                        #um fique em continuação com o
                                                        #outro no ciclo dando a impressão
                                                        #de movimento
                                                        #Colocando -640 em y, essa imagem
                                                        #é colocada acima da primeira imagem (bg)
                                                        #de modo a elas ficarem como uma só, sendo
                                                        #deslocadas para baixo em um screen (tela
                                                        #do jogo) com metade do seu tamanho
                                                        #Deste modo, não vemos quando elas são
                                                        #são reposicionadas no início, dando a
                                                        #impressão de movimento.

        self.spider1 = Spider("assets/spider1.png",random.randrange(0, cf.SIZE_WINDOW_X - 40), cf.POSITION_Y_SPIDER)
                                                        #na linha acima a primeira aranha
                                                        #é gerada em uma posição aleatória

        #self.spider = Obj("assets/spider1.png",200,-50) #criação do objeto aranha, com inicio
                                                        #na imagem spider1, que será, a partir
                                                        #dela, colocada em ciclo para dar
                                                        #impressão de animação, sendo atualizada
                                                        #a cada vez que o método anim, da classe
                                                        #Obj for chamado

                                            #as animações dos objetos na tela são feitas por
                                            #meio dos objetos instanciados da classe Obj, como
                                            #self.bg, self.bg2 e self.spider.
                                            #Esses objetos tem consigo todos os métodos da classe
                                            #Obj, inclusive, o método anim(), que tem as animações
                                            #de cada um deles, de quanto em quanto tempo muda o
                                            #sprite (1 segundo) e quantas mesmas imagens são
                                            #carregadas a cada segundo (30 imagens), para dar suavidade
                                            #ao movimento e animação dos objetos na tela.

        #self.flower = Obj("assets/florwer1.png",random.randrange(0, cf.SIZE_WINDOW_X - 40), cf.POSITION_Y_FLOWER)
                                            #criação do objeto flor, que tem todos os
                                            #métodos da classe Obj()
        self.flower1 = Flower("assets/florwer1.png",random.randrange(0, cf.SIZE_WINDOW_X - 40), cf.POSITION_Y_FLOWER)
                                            #copia o objeto flower_obj, criado na classe Flower
                                            #que tem todas instancias e metodos de Obj

        self.bee = Bee("assets/bee1.png",cf.INITIAL_POSITION_BEE_X,cf.INITIAL_POSITION_BEE_Y)
                                            #cria o objeto bee, da classe Bee, que
                                            #herdou tudo de Obj, mais o método criado para movimentar
                                            #a abelha pelo mouse (método move_bee)

        self.change_scene = False           #variavel de controle, a qual será usada
                                            #no condicional do método draw, da classe main
                                            #para alternancia entre telas
                                            #servirá para troca de telas entre menu, tela do jogo
                                            #e gameover
                                            #Cada classe tem sua variavel self.change_scene, que é
                                            #alterada de acordo com os metodos de cada classe,
                                            #carregando a tela desejada, ou de menu, ou de jogo,
                                            #ou de gameover
        self.score = Text(cf.SIZE_TEXT_SCORE,cf.INIT_TEXT_SCORE)
        self.lifes = Text(cf.SIZE_TEXT_LIFES,cf.INIT_TEXT_LIFES)

    def draw(self, window):                 #Funcao que desenha na tela bg e bg2
        self.bg.draw(window)             #Como bg e bg2 são atualizados a cada iteração
        self.bg2.draw(window)            #do while do metodo events da classe Main
                                            #quando o método draw() é chamado em Main,
                                            #dentro do while do metodo events(), as atualizaçoes
                                            #feitas com a chamada de display.update() são mostradas
                                            #na tela

        self.bee.draw(window)               #desenhamos a abelha na tela, criada no construtor
                                            #da classe Game, que é objeto da classe Bee, que
                                            #herdou tudo da classe Obj mais os seus proprios metodos

        #self.spider.draw(window)         #desenha o objeto spider, criado no construtor da classe
                                            #Game, com a figura atual, conforme o self.frame atual
                                            #(indice da figura da imagem spider), atualizado a cada vez
                                            #que o metodo anim, da classe Obj é chamado

        #self.flower.draw(window)         #desenho da flor na tela do jogo. Segue o mesmo
                                            #raciocínio do objeto spider
        self.flower1.draw(window)
        self.spider1.draw(window)
        

        self.score.draw(window,cf.POSITION_TEXT_SCORE_X,cf.POSITION_TEXT_SCORE_Y)
        self.lifes.draw(window,cf.POSITION_TEXT_LIFES_X,cf.POSITION_TEXT_LIFES_Y)
                                            #objetos criados com base na classe
                                            #Text (Obj)
                                            #self.lifes é a variavel que controla o
                                            #objeto, que por sua vez controla o texto,
                                            #que controla a quantidade de vidas

    #def move_bg(self):                      #método com o objetivo de atualizar a tela
                                            #quando ocorrer qualquer tipo de movimentação
                                            #da mesma, apenas do background
        
        #self.bg.sprite.rect[1] += cf.TAX_UPDATE_Y_BG  #1    #é atribuido ao self.bg, a posição y, sendo atualizada
                                            #1 pixel por fps, dando a impressão de movimento
                                            #O sprite.rect são as propriedades adquiridas da classe
                                            #Obj, que são atribuidas ao objeto self.bg, e que nesse
                                            #caso, atualização para y, já que a classe Obj tem como
                                            #entradas no método construtor: image, x, y
                                            #Essa posição em y é atualizada a cada vez que for chamada
                                            #no laço while, do método update, do objeto Main
        #if self.bg.sprite.rect[1] >= cf.POS_INITIAL_Y_BG:
            #self.bg.sprite.rect[1] = 0
                                            #estas 3 primeiras linhas fazem a figura do fundo de mover
                                            #de y=0 até y=640 (limite da tela na vertical.
                                            #Quando y>=640, a figura bg é colocada novamente em y=0
                                            #para reiniciar o ciclo

            
        #self.bg2.sprite.rect[1] += cf.TAX_UPDATE_Y_BG2  #1

        #if self.bg2.sprite.rect[1] >= 0:
            #self.bg2.sprite.rect[1] = cf.POS_INITIAL_Y_BG2
                                            #se self.bg2 chegar na posição 0, ele retornar para
                                            #-640. Assim, nao vemos descontinuidades na figura
                                            #dando a impressão de movimento de subida mesmo com
                                            #o reposicionamento das mesmas.

                                            #com a diminuição do número de ticks no if do metodo anim()
                                            # da classe Obj, devemos aumentar a velocidade de atualização
                                            #ou animação do nosso bg e bg2.
                                            #Desse modo, modificamos os valores das variaveis
                                            #self.bg.sprite.rect[1] e self.bg2.sprite.rect[1] para que
                                            #aumentando-as para que nosso background seja animado/desca
                                            #mais rapidamente.
    def update(self):
        self.bg.movement(cf.TAX_UPDATE_Y_BG)
        self.bg.reposition(cf.POS_INITIAL_Y_BG, 0)
        self.bg2.movement(cf.TAX_UPDATE_Y_BG2)
        self.bg2.reposition(0, cf.POS_INITIAL_Y_BG2)

        self.spider1.anim("spider", cf.N_TICKS_SPIDER, cf.N_SPRITES_SPIDER)    #esta linha, após a modificação do metodo anim(), da
                                            #classe Obj, inseri o nome da imagem a ser carregada,
                                            #o número de ticks (8) que é de quanto em quanto tempo
                                            #fazemos a alteração do sprite, e a quantidade de frames
                                            #(5) que temos, ou seja, quantas imagens compoem o movimento
                                            #completo da figura até reiniciar o ciclo de movimento
                                            #dela. Nesse caso, no da aranha, temos 5 figuras que compoem
                                            #o movimento completo dela.
            
        self.spider1.move_spider()
          #ao criarmos o método move_spiders(), devemos chamo-lo
                                            #no método update, pois no update() temos a animação da aranha
                                            #pelo metodo spider.anim() e o movimento das aranhas pela
                                            #tela pelo método move_spiders()

        #self.flower.anim("florwer", cf.N_TICKS_FLOWER, cf.N_SPRITES_FLOWER)   #animação das flores, com base no metodo anim()
                                            #pertencente a classe Obj
        self.flower1.anim("florwer", cf.N_TICKS_FLOWER, cf.N_SPRITES_FLOWER)
        
        #self.move_flower()
        self.flower1.move_flower()


        self.bee.anim("bee", cf.N_TICKS_BEE, cf.N_SPRITES_BEE) 
        #self.bee.anim("bee", 8, 4)          #animacao da figura da abelha, pelo metodo anim()
                                            #pertencente a classe obj, com a cada 8 ticks
                                            #gera um ciclo de amostras na tela de sequencia das
                                            #suas 4 imagens usadas para movimento
                                            #Se diminuirmos o número 8, que é o numero de ticks,
                                            #a taxa de troca de imagens da abelha ficara mais rapida,
                                            #ou seja, a abelha tera uma animação mais rápida devido a troca
                                            #das imagens ter um periodo de tempo mais curto para ocorrer.
        
                                            #as duas linhas acima tem o mesmo raciocinio das linhas
                                            #self.spider.anim() e self.move_spiders()

        self.bee.colision(self.spider1.group, "Spider")
                                            #chama o metodo colision, da classe Bee, e coloca o
                                            #grupo spider (self.group = pygame.sprite.Group(),
                                            #que foi criado com a classe Obj, para
                                            #verificar a colisão de alguma aranha com a abelha.
                                            #O spider é o nome do grupo instanciado no construtor
                                            #da classe game, criado com base da classe Obj

        #self.bee.colision(self.flower.group, "Flower")
        self.bee.colision(self.flower1.group, "Flower")
                                            #chama o metodo colision, da classe Bee, e coloca o
                                            #grupo flower (self.group = pygame.sprite.Group(),
                                            #que foi criado com a classe Obj, para
                                            #verificar a colisão de alguma flor com a abelha.
                                            #O flower é o nome do grupo instanciado no construtor
                                            #da classe game, criado com base da classe Obj

                                            #Os nomes Flower e Spider, são os mesmos usados na condicao
                                            #do método colision, da classe Bee(Obj), para verificarmos
                                            #se está sendo reconhecida a colisão de forma correta.

        self.gameover()                     #retorna a variavel que acusa se a quantidade de vidas
                                            #zerou. Essa variavel é atualizada na classe Bee, que herda
                                            #os metodos da classe Obj, e pega o resultado do método gameover
                                            #da classe Bee.

        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(str(self.bee.life))
                                            #o argumento das linhas acima são passados para string,
                                            #pois o método do objeto Texto, o qual self.score e
                                            #self.lifes fazem parte, recebe como parametro de entrada
                                            #variáveis do tipo texto (esta no arquivo obj)
   # def reset_spider(self):

        #if self.spider1.sprite.rect[1] > cf.LIM_Y_SPIDER:
            #self.spider1.sprite.kill()
            #self.spider1 = Spider("assets/spider1.png",random.randrange(0, cf.SIZE_WINDOW_X - 40), cf.POSITION_Y_SPIDER)

    #def reset_flower(self):

        #if self.flower1.sprite.rect[1] > cf.LIM_Y_FLOWER:
            #self.flower1.sprite.kill()
            #self.flower1 = Flower("assets/florwer1.png",random.randrange(0, cf.SIZE_WINDOW_X - 40), cf.INITIAL_POSITION_FLOWER_Y)

            
    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True