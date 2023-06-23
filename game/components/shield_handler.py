import pygame
import random

from game.components.shield import Shield

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP_SHIELD


class ShieldHandler:
    def __init__(self):
        self.shields = []
        self.counter = 0

    # actualiza el estado de los escudos en la lista. Si no hay escudos en la lista y el contador es divisible entre 40 de forma exacta, creara un escudo (se puede cambiar el numero para que los escudos aparezcan con mas o menos frecuencia). En caso de que si haya escudos, se actualiza el estado del escudo.
    def update(self):
        if self.shields == [] and self.counter % 40 == 0:
            self.spawn_a_shield()
        elif self.shields != []:
            for shield in self.shields:
                shield.update()
                if shield.is_active == False:
                    self.remove(shield)
        self.counter += 1

    def draw(self, screen):
        for shield in self.shields:
            shield.draw(screen)

    # metodo para generar escudos en una posicion aleatoria
    def spawn_a_shield(self):
        self.shields.append(Shield())
        self.set_position_of_shields()
    
    # metodo para definir la posicion aleatoria del escudo
    def set_position_of_shields(self):
        # establecemos donde aparecera cada enemigo
        pos_x_random = random.randint(20,1000)
        for shield in self.shields:
            shield.rect.x = pos_x_random

    def remove(self, shield):
        self.shields.remove(shield)

    # metodo para activar el escudo en el jugador en caso de que colisione con un escudo. Cambia la imagen y el estado a indestructible a el jugador. Al final elimina el escudo de la lista
    def active_shield_for_spaceship(self, player, spacheship_xpos, spaceship_ypos):
        for shield in self.shields:
            if shield.rect.colliderect(player.rect) and player.is_indestructible == False:
                player.image = SPACESHIP_SHIELD
                player.name_image = "spaceship_shield"
                player.image_width = 50
                player.image_height = 60
                player.image = pygame.transform.scale(player.image, (player.image_width,player.image_height))
                player.rect = player.image.get_rect()
                player.rect.x = spacheship_xpos
                player.rect.y = spaceship_ypos
                player.is_indestructible = True
                self.shields.remove(shield)

        