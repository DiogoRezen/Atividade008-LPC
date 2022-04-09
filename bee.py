import pygame
from obj import Obj
import config as cf

class Bee(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)
                                                                    #class Bee(Obj): - declaração da classe Bee
                                                                    #que herdará tudo da classe Obj, ou seja,
                                                                    #terá todos os métodos e objetos da classe Obj
                                                                    #O método construtor de Bee tem os mesmos
                                                                    #parametros de entrada
                                                                    #Ao declararmos super(). estamos colocando
                                                                    #que Bee herdará tudo de Obj
                                                                    #Fizemos isso para nao ter que copiar todos os
                                                                    #metodos de Obj novamente, alem de podermos
                                                                    #escrever novos métodos para Bee, que não estão
                                                                    #presentes em Obj
                                                                    #Outro motivo é que precisamos criar eventos
                                                                    #para Bee que não existem em aranha ou na flor.Esses
                                                                    #eventos incluem, por exemplo, o movimento da
                                                                    #abelha pelas setas ou pelo mouse

        pygame.mixer.init()                                         #inicia o tocador de audio do pygame
        self.sound_pts = pygame.mixer.Sound("assets/sounds/score.ogg")
        self.sound_block = pygame.mixer.Sound("assets/sounds/bateu.ogg")
                                                                    #a função pygame.mixer.Sound() serve para reproduzirmos
                                                                    #um som/audio menor, uma vez apenas
        
        self.life = cf.DEFAULT_LIFE_BEE                                               #quantidade inicial de vidas
        self.pts = cf.DEFAULT_PTS_BEE                                                #quantidade inicial de pontos
        
        
    def move_bee(self, event):
        if event.type == pygame.MOUSEMOTION:                        #Se o movimento do mouse for um tipo de evento
                                                                    #na tela do jogo, ele fará alguma ação
            
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] + cf.SHIFT_X_MOUSE    #a posição do sprite em x receberá a posicao
                                                                    #do mouse no eixo x
                                                                    #O -35 é a metade do tamanho da imagem da
                                                                    #abelha em x, para que o centro x dela fique
                                                                    #posicionado no cursor em x
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] + cf.SHIFT_Y_MOUSE    #a posição do sprite em y receberá a posicao
                                                                    #do mouse no eixo y
                                                                    #O -30 é a metade do tamanho da imagem da
                                                                    #abelha em y, para que o centro y dela fique
                                                                    #posicionado no cursor em y

    def colision(self, group, name):
        name = name
        colision = pygame.sprite.spritecollide(self.sprite, group, True)
                                                #a funcao do pygame, spritecollide verifica se está havendo
                                                #colisoes entre os sprites
                                                #Os argumentos acima, self.sprite, são objetos da classe
                                                #Obj que foram criados justamente para receber quaisquer
                                                #que sejam os elementos que são instanciados em outras
                                                #classes como aranha, abelha, flores. Esse self.sprite
                                                #é o objeto responsavel por identificar a colisao, foi
                                                #instanciado em Obj, e praticamente é o proprio objeto de
                                                #Obj. Nesse caso, quem identificará a colisão é o self.sprite
                                                #da abelha.
                                                #O group são os grupos de sprite que colidem com o sprite
                                                #considerado, que nesse caso é o self.sprite, que são os
                                                #grupos das flores e o grupo das aranhas.
                                                #O False é para que o sprite que colide não seja destruido
                                                #quando houver a colisão. Se colocar True, o objeto saira da cena

                                                #colision só retorna True (há colisão) ou False (não há colisão),
                                                #ou seja, se esta havendo
                                                #colisão ou nao do grupo com o objeto considerado (self.sprite)

        if name == "Flower" and colision:
            #print("Flower")
            self.pts += 1                       #ao colidir com uma flor, adiciona um ponto
            self.sound_pts.play()               #coloca para tocar a variavel self.sound_pts
            print(self.pts)
        elif name == "Spider" and colision:
            #print("Spider")
            self.life -= 1                      #ao colidir com uma aranha, subtrai uma vida
            self.sound_block.play()             #coloca para tocar a variavel self.sound_block
            print(self.life)
                                                #quando houver colisao de algum grupo com a abelha,
                                                #ele mostrará na tela quem foi que colidiu, se foi flor ou
                                                #aranha
