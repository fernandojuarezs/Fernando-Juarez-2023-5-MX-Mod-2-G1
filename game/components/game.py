import pygame
import sys

import random

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, GAME_OVER, SPACESHIP_SHIELD
from game.components.enemies.enemy_handler import EnemyHandler

from game.components.spaceship import Spaceship

from game.components.gameoverscreen import GameOver

from game.components.shield_handler import ShieldHandler


# Game tiene un Spaceship
# Game puede decirle al spaceship que se actualice llamandole al metodo update(). update() espera una lista que contiene los eventos de teclado que ocurrieron
class Game:
    score = 0
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10 # el numero de pixeles que el "objeto / imagen" se mueve en patalla
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.enemy_handler = EnemyHandler()

        self.wait = False
        self.games_scores = []
        self.total_deaths = 0
        self.screen_game_over = GameOver()

        self.shield_handler = ShieldHandler()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        # mientras los atributos jugando sea verdadero y si la nave esta viva
        while self.playing == True and self.wait == False:
            self.handle_events() # verifica que no se quiera salir
            self.update() # verifica las actualizaciones 
            self.draw() # dibuja
        # si se cierra la ventana se sale del juego
        else:
            print("Something ocurred to quit the game!")
            pygame.display.quit()
            pygame.quit()
                
    def handle_events(self):
        # pygame.event.get() es un iterable (lista)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #el QUIT event es el click en el icono que cierra ventana
                self.playing = False

    # update de Game llama al update de algunos de los objetos de mi juego
    def update(self):
        events = pygame.key.get_pressed() # pygame.key.get_pressed() obtiene los eventos del teclado en un game loops        
        self.spaceship.update(events)
        self.shield_handler.update()
        self.shield_handler.active_shield_for_spaceship(self.spaceship, self.spaceship.rect.x, self.spaceship.rect.y)
        self.enemy_handler.update()
        # checa si los enemigos han muerto y aumenta el score actual en la misma cantidad que el enemy handler
        self.enemy_handler.die_by_bullet(self.spaceship.bullets_shooted)
        self.score = self.enemy_handler.enemies_died
        # checa si el jugador ha muerto y aumenta el numero de muertes actual en la misma cantidad que el enemy handler
        self.enemy_handler.kill_by_bullet(self.spaceship, self.spaceship.rect.x, self.spaceship.rect.y)
        self.total_deaths = self.enemy_handler.deaths_of_player

    def draw(self):
        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar
        self.screen.fill((255, 255, 255)) # lleno el screen de color BLANCO???? 255, 255, 255 es el codigo RGB
        self.draw_background()

        # Game le ordena al spaceship dibujarse llamando a un metodo llamando draw del Spaceship (el metodo draw espera que le pase screen)
        self.spaceship.draw(self.screen)
        self.enemy_handler.draw(self.screen)
        self.shield_handler.draw(self.screen)
        # si el jugador muere, llamara a la pantalla de game over
        self.display_game_over()

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

    # muestra la pantalla de game over y hasta que no se presione una tecla o se cierre la aplicacion, se seguira mostrando la pantalla de gamve over
    def display_game_over(self):
        if self.spaceship.is_alive == False:
            self.wait = True
            while self.wait == True:
                self.manage_scores() # utiliza el metodo manage scores que a su vez utiliza un metodo de la clase GameOver
                self.enemy_handler.enemies.clear()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        self.screen_game_over.reset(self.spaceship)
                        self.wait = False
                    if event.type == pygame.QUIT:
                        print("me sali")
                        sys.exit()
            self.enemy_handler.enemies_died = 0  # resetea el score actual (recordemos que score es igual a las muertes de los enemigos) 

    def manage_scores(self):
        self.games_scores.append(self.score)
        self.screen_game_over.display_game_over(self.score, self.total_deaths, self.games_scores)

   