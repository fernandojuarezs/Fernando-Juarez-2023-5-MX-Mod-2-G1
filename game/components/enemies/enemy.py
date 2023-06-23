import pygame
import random

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT

from game.components.enemies.bullet_enemy import BulletEnemy

class Enemy:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.start_screen = 0
        self.rect.x = 0
        self.rect.y = 0
        # definimos las posibles velocidades que los enemigos podran usar
        self.option1_xspeed = 5
        self.option2_xspeed = 2
        self.option1_yspeed = 5
        self.option2_yspeed = 2
        self.is_alive = True
        self.is_shooting = False
        self.bullets_shooted = []

    # permite al enemigo cambiar su estado de vivo a Falso si esta fuera de la pantalla, permite moverse, cargar balas en la lista si su estado de disparar es verdadero y eliminar las balas que no esten activas de la lista de balas disparadas
    def update(self):
        if self.rect.y > SCREEN_HEIGHT:
            self.is_alive = False
        self.walk_random()
        if self.is_shooting == True:
            self.charge_bullet()
        for bullet in self.bullets_shooted:
            bullet.update()
            if not bullet.is_active:
                self.bullets_shooted.remove(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for i in range(len(self.bullets_shooted)):
            self.bullets_shooted[i].draw(screen)

    # permite al enemigo poner balas en su lista y una vez que cargo solo una bala, el estado del enemigo de disparar cambia a Falso
    def charge_bullet(self):
        self.bullets_shooted.append(BulletEnemy(self.rect.x, self.rect.y))
        self.is_shooting = False

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
        if random_number_1 >= 0.5 and self.rect.x < SCREEN_WIDTH-self.rect.width and random_number_2 >= 0.5:
            self.rect.x += self.option1_xspeed
        # si el enemigo no se ha salido del lateral derecho y el numero random 2 es menor que 0.5 lo hara con la segunda velocidad para el eje x
        elif random_number_1 >= 0.5 and self.rect.x < SCREEN_WIDTH-self.rect.width and random_number_2 < 0.5:
            self.rect.x += self.option2_xspeed

    # metodo para moverse hacia la izquierda (solo se ejecutara si el primer numero aleatorio es menor que 0.5)
    def move_to_left(self, random_number_1, random_number_2):
        # si el enemigo no se ha salido del lateral izquierdo y el numero random 2 es mayor o igual que 0.5 lo hara con la primer velocidad para el eje x
        if random_number_1 < 0.5 and self.rect.x > self.start_screen and random_number_2 >= 0.5:
            self.rect.x -= self.option1_xspeed
        # si el enemigo no se ha salido del lateral izquierdo y el numero random 2 es menor que 0.5 lo hara con la segunda velocidad para el eje x
        elif random_number_1 < 0.5 and self.rect.x > self.start_screen and random_number_2 < 0.5:
            self.rect.x -= self.option2_xspeed

