import pygame

from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP

# sprite es un objeto de pygame (objeto dibujable)
class Spaceship(Sprite):
    def __init__(self):
        self.image = SPACESHIP
        self.image_width = 40
        self.image_height = 50
        self.image = pygame.transform.scale(self.image, (self.image_width,self.image_height))
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, keyboard_events):
        if keyboard_events[pygame.K_RIGHT]:
            self.rect.x += 4
            if self.rect.x > 1140:
                self.rect.x = -40
        if keyboard_events[pygame.K_LEFT]:
            self.rect.x -= 4
            if self.rect.x < -40:
                self.rect.x = 1100



