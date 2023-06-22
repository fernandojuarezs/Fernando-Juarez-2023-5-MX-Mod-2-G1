import pygame

import random

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, GAME_OVER
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.spaceship import Spaceship


# Game tiene un Spaceship
# Game puede decirle al spaceship que se actualice llamandole al metodo update(). update() espera una lista que contiene los eventos de teclado que ocurrieron
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.font = pygame.font.Font(FONT_STYLE, 40)
        self.game_speed = 10 # el numero de pixeles que el "objeto / imagen" se mueve en patalla
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.enemy_handler = EnemyHandler()

        self.games_scores = [] # puntajes de partidas
        self.max_score = None
        self.currently_score = 0
        self.total_deaths = 0

        self.playing_again = False


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        # mientras los atributos jugando sea verdadero, crear_nuevo_grupo_de_enemigos sea falso y colision_de_la_nave sea falso
        while self.playing == True and self.spaceship.is_alive == True:
            self.handle_events() # verifica que no se quiera salir
            self.update() # verifica las actualizaciones 
            self.draw() # dibuja
            if self.playing == False:
                print("Something ocurred to quit the game!")
                pygame.display.quit()
                pygame.quit()
                # aqui va el dibujo de la pantalla de game over
            if self.spaceship.is_alive == False:
                self.games_scores.append(self.currently_score)
                while self.playing_again == False:
                    self.handle_events()
                    self.draw_score()
                    if self.playing_again == True:
                        self.spaceship.is_alive == True
                        break
                    if self.playing == False:
                        print("Something ocurred to quit the game!")
                        pygame.display.quit()
                        pygame.quit()
                

    def handle_events(self):
        # pygame.event.get() es un iterable (lista)
        events = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #el QUIT event es el click en el icono que cierra ventana
                self.playing = False
        if events[pygame.K_RETURN]:
            self.playing_again = True
            
    # update de Game llama al update de algunos de los objetos de mi juego
    def update(self):
        events = pygame.key.get_pressed() # pygame.key.get_pressed() obtiene los eventos del teclado en un game loops        
        self.spaceship.update(events)
        self.enemy_handler.update()
        self.enemy_handler.die_by_bullet(self.spaceship.bullets_shooted)
        self.currently_score = self.enemy_handler.enemies_died
        self.enemy_handler.kill_by_bullet(self.spaceship)
        self.total_deaths = self.enemy_handler.deaths_of_player

        
    def draw(self):
        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar
        self.screen.fill((255, 255, 255)) # lleno el screen de color BLANCO???? 255, 255, 255 es el codigo RGB
        self.draw_background()

        # Game le ordena al spaceship dibujarse llamando a un metodo llamando draw del Spaceship (el metodo draw espera que le pase screen)
        self.spaceship.draw(self.screen)

        self.enemy_handler.draw(self.screen)

        # Game le ordena a los enemigos de la lista dibujarse llamando a un metodo llamando draw del Enemy (el metodo draw espera que le pase screen)
        pygame.display.update() # esto hace que el dibujo se actualice en el display de pygame
        pygame.display.flip()  # hace el cambio

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()# alto de la imagen
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) # blit "dibuja"
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

        # dibujamos el letrero del puntaje

    def draw_score(self):
        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar
        self.screen.fill((255, 255, 255))
        image = pygame.transform.scale(GAME_OVER, (400,100))
        x_pos = 200
        y_pos = 100
        self.screen.blit(image, (x_pos,y_pos))
        
        play_again = self.font.render("Press enter to play again", True, (0,0,0))
        score = self.font.render("Score : " + str(self.currently_score), True, (0,0,0))
        max_score = self.font.render("Max score :" + str(self.get_max_score()), True, (0,0,0))
        deaths = self.font.render("Total deaths: " + str(self.total_deaths), True, (0,0,0))


        self.screen.blit(play_again, (SCREEN_WIDTH//2,200))
        self.screen.blit(score, (SCREEN_WIDTH//2,300))
        self.screen.blit(max_score, (SCREEN_WIDTH//2,400))
        self.screen.blit(deaths, (SCREEN_WIDTH//2,500))

        pygame.display.update() # esto hace que el dibujo se actualice en el display de pygame
        pygame.display.flip()  # hace el cambio

    def get_max_score(self):
        if self.games_scores == []:
            return 0
        else:
            return max(self.games_scores)




    

