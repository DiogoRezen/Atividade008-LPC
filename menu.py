import pygame
from obj import Obj

#classe responsavel pelas cenas, ou troca de telas, do jogo
#cada objeto criado na classe Menu será uma cena separada, ou seja,
#uma tela diferente.

class Menu:

    def __init__(self, image):

        self.bg = Obj(image, 0, 0)

        self.change_scene = False           #ao clicar enter, o método event.type, da classe Menu
                                            #é, é True, torcando o estado da variavel self.change_scene
                                            #para True, sendo usado para troca da imagem de tela
                                            #no if self.start_screen.change_scene.
                                            #Caso seja verdadeiro, ou seja, caso pressionamos
                                            #a tecla enter, a variavel self.change_scene será trocada
                                            #para True no método event, da classe Menu, esse valor é
                                            #passado para a classe Main, no método draw, no trecho:

                                            #1        self.window.fill([0, 0, 0])
                                            #2        if self.start_screen.change_scene == False:
                                            #3            self.start_screen.draw(self.window)   
                                            #4        elif self.game.change_scene == False:
                                            #5            self.game.draw(self.window)
                                            #6            self.game.update()
                                            #7        elif self.gameover.change_scene == False:
                                            #8            self.gameover.draw(self.window)
                                            #9        else:
                                            #10           self.start_screen.change_scene = False
                                            #11           self.game.change_scene = False
                                            #12           self.gameover.change_scene = False
                                            #13           self.game.bee.life = 3
                                            #14           self.game.bee.pts = 0

                                            #o objeto self.start_screen, criada no construtor de Main
                                            #possui a variavel self.change_scene da classe Menu e todos
                                            #os seus métodos. Assim, na linha 2, se ela for false, é
                                            #desenhado na tela, pelo metodo draw, da classe Menu, o
                                            #objeto self.bg, o qual foi criado na classe Main, como
                                            #como objeto Menu, e recebe a imagem do fundo da tela de inicio.
                                            #Na linha 4, se o objeto self.game, do tipo Game(),
                                            #criado na classe construtora de Main, tiver como valor da sua
                                            #variavel change_scene o valor false, será desenhado na tela,
                                            #usando o metodo draw, da classe Game, todos os componentes
                                            #do jogo: plano de fundo animado, abelha, flores e aranha, alem
                                            #de ser chamado o método update, que atualiza a tela gerando
                                            #as animações.
                                            #Se o objeto self.gameover, do tipo GameOver, criado em Main,
                                            #tem sua variavel change_scene com valor falso, será desenhado
                                            #na window a tela de game over, com o metodo draw, pertencente a
                                            #classe GameOver, que herda tudo da classe Menu. Nesse caso, o
                                            #metodo draw usado, da classe gameover, usa o metodo draw herdado
                                            #de Menu. Esse metodo usa o metodo draw do objeto self.bg, do
                                            #tipo Obj. Por ele ser do tipo Obj, o metodo draw de Obj desenha
                                            #em window todo os objetos pertencentes ao grupo de sprite.
                                            #Por fim, se o else for acionado, ele irá atribuir false as
                                            #variaveis change_scene, dos objetos: self.start_screen (da classe
                                            #Main), self.game (da classe Game), self.gameover (da classe gameover)
                                            #e colocará a quantoidade de vidas em 3 e de pontos em 0
                                            #A imagem de gameover é passada no objeto self.gameover, do tipo
                                            #GameOver, no construtor da classe Main. Assim, o objeto do tipo
                                            #GameOver terá todos os parametros e métodos herdados da classe
                                            #Menu, mas com a imagem gameover.png instanciada no construtor da classe
                                            #Main.
                                            #O else reinicia os verificadores e as variaveis de score, para quando
                                            #reiniciar o jogo sempre com 3 vidas e 0 pontos e com verificadores
                                            #dos if´s default

    def draw(self, window):
        self.bg.draw(window)                #como self.bg é um objeto de Obj
                                            #então ele tem todos os parametros
                                            #do Obj.
                                            #O self.bg é um objeto Obj, que é
                                            #instanciado como um grupo de
                                            #sprites, por isso chama-se .group.draw()
                                            #para desenha-lo na tela window
                                            #A variavel window vem da classe main

    def event(self, event):
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_RETURN:
                self.change_scene = True
                                            #quando a função events for chamada no
                                            #main, podemos passar o parametro event
                                            #para de main para a classe menu.
                                            #Verificamos qual tecla foi pressionadao
                                            #e se foi o enter (return), o self.change_scene
                                            #passa a ser verdadeiro, que antes era falso
                                            #pelo construtor __init__ da classe Menu.
                                            #Com self.change_scene sendo verdadeiro, podemos
                                            #trocar a cena/tela para o qual quisermos.
                #print(self.change_scene)

class GameOver(Menu):
    
    def __init__(self, image):
        super().__init__(image)

                                
