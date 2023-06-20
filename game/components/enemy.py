import pygame

import random

from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    def __init__(self):
        self.image = self.random_image()
        self.image_width = 40
        self.image_height = 50
        self.start_screen = 0 # nos referimos a la esquina superior izquierda como start screen
        self.image = pygame.transform.scale(self.image, (self.image_width,self.image_height))
        self.rect = self.image.get_rect()
        # definimos los valores de self.rect.x e y con los que iniciara la nave
        self.rect.x = 0
        self.rect.y = 0
        # definimos las posibles velocidades que los enemigos podran usar
        self.option1_xspeed = 5
        self.option2_xspeed = 2
        self.option1_yspeed = 5
        self.option2_yspeed = 2

    # metodo del enemigo para dibujarse en pantalla
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    # metodo del enemigo para actualizar la posicion del enemigo movimiento de acuerdo a una caminata aleatoria
    def update(self):
        self.walk_random()

    # metodo para establecer de manera aleatoria la imagen del enemigo
    def random_image(self):
        random_number = random.random()
        if random_number >= 0.5:
            return ENEMY_2
        else:
            return ENEMY_1
    
    # metodo para moverse de forma aleatoria
    def walk_random(self):
        random_number_for_moving = random.random() # entrega un numero entre 0 y 1 (decimales)
        random_number_for_speed = random.random()
        # metodos para moverse hacia adelante, atras, derecha o izquierda dependiendo de los numeros aleatorios anteriores
        self.move_forward(random_number_for_moving, random_number_for_speed)
        self.move_backwards(random_number_for_moving, random_number_for_speed)
        self.move_to_right(random_number_for_moving, random_number_for_speed)
        self.move_to_left(random_number_for_moving, random_number_for_speed)

    # metodo para moverse hacia abajo (solo se ejecutara si el primer numero aleatorio es mayor o igual que 0.3)
    def move_forward(self, random_number_1, random_number_2):
        # si el numero random 2 es mayor que 0.5 lo hara con la primer velocidad para el eje y
        if random_number_1 >= 0.3 and random_number_2 >= 0.5: #and self.rect.y < SCREEN_HEIGHT-self.image_height:
            self.rect.y += self.option1_yspeed
        # si el numero random 2 es menor que 0.5 lo hara con la segunda velocidad
        elif random_number_1 >= 0.3 and random_number_2 < 0.5:
            self.rect.y += self.option2_yspeed
    
    # metodo para moverse hacia a arriba (solo se ejecutara si el primer numero aleatorio es menor que 0.3)
    def move_backwards(self, random_number_1, random_number_2):
        # si el enemigo no se ha salido del borde superior y el numero random 2 es mayor que 0.5 lo hara con la primer velocidad para el eje y
        if random_number_1 < 0.3 and self.rect.y > self.start_screen and random_number_2 >= 0.5:
            self.rect.y -= self.option1_yspeed
        # si el enemigo no se ha salido del borde superior y el numero random 2 es menor que 0.5 lo hara con la primer velocidad para el eje y      
        elif random_number_1 < 0.3 and self.rect.y > self.start_screen and random_number_2 < 0.5:
            self.rect.y -= self.option2_yspeed

    # metodo para moverse hacia la derecha (solo se ejecutara si el primer numero aleatorio es mayor o igual que 0.5)
    def move_to_right(self, random_number_1, random_number_2):
        # si el enemigo no se ha salido del lateral derecho y el numero random 2 es mayor o igual que 0.5 lo hara con la primer velocidad para el eje x
        if random_number_1 >= 0.5 and self.rect.x < SCREEN_WIDTH-self.image_width and random_number_2 >= 0.5:
            self.rect.x += self.option1_xspeed
        # si el enemigo no se ha salido del lateral derecho y el numero random 2 es menor que 0.5 lo hara con la segunda velocidad para el eje x
        elif random_number_1 >= 0.5 and self.rect.x < SCREEN_WIDTH-self.image_width and random_number_2 < 0.5:
            self.rect.x += self.option2_xspeed

    # metodo para moverse hacia la izquierda (solo se ejecutara si el primer numero aleatorio es menor que 0.5)
    def move_to_left(self, random_number_1, random_number_2):
        # si el enemigo no se ha salido del lateral izquierdo y el numero random 2 es mayor o igual que 0.5 lo hara con la primer velocidad para el eje x
        if random_number_1 < 0.5 and self.rect.x > self.start_screen and random_number_2 >= 0.5:
            self.rect.x -= self.option1_xspeed
        # si el enemigo no se ha salido del lateral izquierdo y el numero random 2 es menor que 0.5 lo hara con la segunda velocidad para el eje x
        elif random_number_1 < 0.5 and self.rect.x > self.start_screen and random_number_2 < 0.5:
            self.rect.x -= self.option2_xspeed
  