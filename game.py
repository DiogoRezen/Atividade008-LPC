from obj import Obj, Bee, Text
import random


class Game:

    def __init__(self):

        self.bg = Obj("assets/bg.png", 0, 0)            #bg é o background que será o
                                                        #o fundo da tela do jogo
        self.bg2 = Obj("assets/bg.png", 0, -640)        #bg2 é o background que será o
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
        
        self.spider = Obj("assets/spider1.png",random.randrange(0, 320), -50)
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

        self.flower = Obj("assets/florwer1.png",random.randrange(0, 320), 200)
                                            #criação do objeto flor, que tem todos os
                                            #métodos da classe Obj()

        self.bee = Bee("assets/bee1.png",150,600)
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
        self.score = Text(120,"0")
        self.lifes = Text(60,"3")

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
        
        self.spider.draw(window)         #desenha o objeto spider, criado no construtor da classe
                                            #Game, com a figura atual, conforme o self.frame atual
                                            #(indice da figura da imagem spider), atualizado a cada vez
                                            #que o metodo anim, da classe Obj é chamado

        self.flower.draw(window)         #desenho da flor na tela do jogo. Segue o mesmo
                                            #raciocínio do objeto spider

        self.score.draw(window,160,50)
        self.lifes.draw(window,50,50)
                                            #objetos criados com base na classe
                                            #Text (Obj)
                                            #self.lifes é a variavel que controla o
                                            #objeto, que por sua vez controla o texto,
                                            #que controla a quantidade de vidas

    def move_bg(self):                      #método com o objetivo de atualizar a tela
                                            #quando ocorrer qualquer tipo de movimentação
                                            #da mesma, apenas do background
        
        self.bg.sprite.rect[1] += 10  #1    #é atribuido ao self.bg, a posição y, sendo atualizada
                                            #1 pixel por fps, dando a impressão de movimento
                                            #O sprite.rect são as propriedades adquiridas da classe
                                            #Obj, que são atribuidas ao objeto self.bg, e que nesse
                                            #caso, atualização para y, já que a classe Obj tem como
                                            #entradas no método construtor: image, x, y
                                            #Essa posição em y é atualizada a cada vez que for chamada
                                            #no laço while, do método update, do objeto Main
        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
                                            #estas 3 primeiras linhas fazem a figura do fundo de mover
                                            #de y=0 até y=640 (limite da tela na vertical.
                                            #Quando y>=640, a figura bg é colocada novamente em y=0
                                            #para reiniciar o ciclo

            
        self.bg2.sprite.rect[1] += 10  #1

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640
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
        self.move_bg()
        self.spider.anim("spider", 8, 5)    #esta linha, após a modificação do metodo anim(), da
                                            #classe Obj, inseri o nome da imagem a ser carregada,
                                            #o número de ticks (8) que é de quanto em quanto tempo
                                            #fazemos a alteração do sprite, e a quantidade de frames
                                            #(5) que temos, ou seja, quantas imagens compoem o movimento
                                            #completo da figura até reiniciar o ciclo de movimento
                                            #dela. Nesse caso, no da aranha, temos 5 figuras que compoem
                                            #o movimento completo dela.
            
        self.move_spiders()                 #ao criarmos o método move_spiders(), devemos chamo-lo
                                            #no método update, pois no update() temos a animação da aranha
                                            #pelo metodo spider.anim() e o movimento das aranhas pela
                                            #tela pelo método move_spiders()

        self.flower.anim("florwer", 8, 3)   #animação das flores, com base no metodo anim()
                                            #pertencente a classe Obj
        self.move_flower()

        self.bee.anim("bee", 2, 5) 
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

        self.bee.colision(self.spider.group, "Spider")
                                            #chama o metodo colision, da classe Bee, e coloca o
                                            #grupo spider (self.group = pygame.sprite.Group(),
                                            #que foi criado com a classe Obj, para
                                            #verificar a colisão de alguma aranha com a abelha.
                                            #O spider é o nome do grupo instanciado no construtor
                                            #da classe game, criado com base da classe Obj

        self.bee.colision(self.flower.group, "Flower")
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
        

    def move_spiders(self):
                                            #função responsavel por movimentar/transladar a
                                            #aranha pela pela
        self.spider.sprite.rect[1] += 11
                                            #objeto aranha desce a tela a uma taxa de 10 pixels a
                                            #cada frame

        if self.spider.sprite.rect[1] > 640:
            self.spider.sprite.kill()       #ao sair da tela, na parte inferior,
                                            #o objeto aranha é eliminado
            self.spider = Obj("assets/spider1.png", random.randrange(0, 320), -50)
                                            #após a primeira aranha ser eliminada pela função
                                            #sprite.kill(), com a chamada do método update(),
                                            #que chama o método move_spiders(), da classe Game,
                                            #temo a criação de uma nova aranha em uma posição, também,
                                            #aleatória, no inicio da tela de jogo, na parte superior
                                            #da janela do jogo.
            #print("aranha morreu")

    def move_flower(self):
                                            #função responsavel por movimentar/transladar a
                                            #flor pela pela
        self.flower.sprite.rect[1] += 8
                                            #objeto flor desce a tela a uma taxa de 6 pixels a
                                            #cada frame

        if self.flower.sprite.rect[1] > 640:
            self.flower.sprite.kill()       #ao sair da tela, na parte inferior,
                                            #o objeto flor é eliminado
            self.flower = Obj("assets/florwer1.png", random.randrange(0, 320), -100)
                                            #após a primeira flor ser eliminada pela função
                                            #sprite.kill(), com a chamada do método update(),
                                            #que chama o método move_spiders(), da classe Game,
                                            #temo a criação de uma nova flor em uma posição, também,
                                            #aleatória, no inicio da tela de jogo, na parte superior
                                            #da janela do jogo.
            #print("flor morreu")
            
    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True
