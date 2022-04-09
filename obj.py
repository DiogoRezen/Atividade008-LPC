import pygame


class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()  #verifica se há colisão dos objetos
                                            #que estão nesse grupo
                                            #Group() guarda, por exemplo, todos os objetos aranha em um grupo,
                                            #para se trabalhar
        self.sprite = pygame.sprite.Sprite(self.group)  #Sprite() trabalha com imagens, dimensoes, tamanhos
                                                        #do objeto Group(), criado em self.group

                                                        #As linhas abaixo acessam a parte relacionada a uma imagem e rects ao objeto
                                                        #self.sprite criado acima
                                                        #Desse modo, colocar informações nessa áreas do objeto
                                                        #self.sprit
        self.sprite.image = pygame.image.load(image)    #Dentro do Sprite já temos como acessar image,
                                                        #rect, por isso ele é chamado nos self abaixo
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1                                  #variavel responsavel pelo numero da primeira
                                                        #imagem a ser chamada do spider, que será usada no
                                                        #método anim, para que essa variavel seja atualizada
                                                        #e mude a cada frame a imagem da aranha a ser colocada
                                                        #na tela do jogo, no caso, na variavel window da classe
                                                        #Main

        self.tick = 0

        #self.change_scene = False                       #essa variavel será usada no metodo gameover, da classe
                                                        #Bee, para verificar se as vidas se esgotaram e retornar
                                                        #True. Raciocinio parecido ao feito em Main, que caso a
                                                        #variavel self.change_scene for True, trocamos a cena/tela.

    def draw(self, window):
        self.group.draw(window)                         #desenha o grupo de objetos self.group, com o método draw
                                                        #na tela
        
    def anim(self, image, tick, frames):
        self.tick += 1
        if self.tick == tick: #8: #30:
            self.tick = 0
            self.frame += 1
                                                        #na classe Main cria o objeto self.fps com a
                                                        #função .Clock() do pygame. Esse objeto é usado
                                                        #no método update, dentro do laço while.
                                                        #Como instanciado, a cada segundo, 30 imagens
                                                        #são carregadas na tela, sendo essas imagens
                                                        #correspondentes ao objetos animados
                                                        #Na classe Obj, é criado a variável self.tick
                                                        #no método construtor. Essa variavel é incrementada
                                                        #em 1 a cada chamada do método anim().
                                                        #Quando self.tick chega em 30, que equivale a 1
                                                        #segundo, definido no método update, da classe
                                                        #Main, ele volta a ser 0.
                                                        #A cada 1 segundo, a variavel self.frame é aumentada
                                                        #trocando o sprite da aranha, abelha, etc, que esteja na tela.
                                                        #Assim, a durante 1 segundo se mantem a mesma imagem na tela,
                                                        #que é carregada por 30 vezes. Após passar 1 segundo,
                                                        #essa imagem é trocada e a nova carregada 30 vezes na
                                                        #tela, dando mais suavidade ao movimento dos sprites.

                                                        #trocando o numero do if de 30 para 8, diminuimos a
                                                        #o tempo de troca de sprite para animação, deixando o tempo
                                                        #de troca mais rápido.
                                                        #Ou seja, a cada 8 ticks, ao invés de 30 ticks, o sprite
                                                        #do objeto será trocado.
        
        if self.frame == frames: #4:
            self.frame = 1
                                                        #atualização da variavel self.frame que sera
                                                        #adicionada uma unidade para dar a impressao
                                                        #de movimento a cada vez que o metodo anim
                                                        #for chamado.
                                                        #self.frama é o indice do nome do arquivo da
                                                        #imagem da aranha
        self.sprite.image = pygame.image.load("assets/"+ image + str(self.frame) +".png")

                                #Alteramos o método anim() colocando os parametros image, tick, frames
                                #Assim, mudando o conteudo da variavel image, que é o nome da imagem
                                #a ser carregada, temos a mudança da figura que será animada na tela,
                                #nesse caso: aranha, flor ou abelha.
                                #Fornecemos, tambem, quantos ticks devem ocorrer para mudar o frame,
                                #ou seja, quantos ciclos de maquina ocorrem até mudar a imagem
                                #do componente a ser animado na tela.
                                #Fornecemos, tambem, o frames, que justamente é o indexador,
                                #o número da imagem de cada componente que será carregado na tela
                                #para dar a idéia de movimento.
        

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
        
        self.life = 3                                               #quantidade inicial de vidas
        self.pts = 0                                                #quantidade inicial de pontos
        
        
    def move_bee(self, event):
        if event.type == pygame.MOUSEMOTION:                        #Se o movimento do mouse for um tipo de evento
                                                                    #na tela do jogo, ele fará alguma ação
            
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35    #a posição do sprite em x receberá a posicao
                                                                    #do mouse no eixo x
                                                                    #O -35 é a metade do tamanho da imagem da
                                                                    #abelha em x, para que o centro x dela fique
                                                                    #posicionado no cursor em x
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30    #a posição do sprite em y receberá a posicao
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

                                                

class Text:

    def __init__(self, size, text):

        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, False, (255, 255, 255))
                                                #a variavel self.render é usada
                                                #para colocar o texto que vai
                                                #para a tela.        

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update_text(self, update):
        self.render = self.font.render(update, False, (255, 255, 255))
        
        
