import pygame
import random

from game.components.shield import Shield

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP_SHIELD


class ShieldHandler:
    def __init__(self):
        self.shields = []
        self.counter = 0

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

    def spawn_a_shield(self):
        self.shields.append(Shield())
        self.set_position_of_shields()
    
    def set_position_of_shields(self):
        # establecemos donde aparecera cada enemigo
        pos_x_random = random.randint(20,1000)
        for shield in self.shields:
            shield.rect.x = pos_x_random

    def remove(self, shield):
        self.shields.remove(shield)

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

        