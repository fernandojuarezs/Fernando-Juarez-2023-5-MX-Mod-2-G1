import pygame
import random

from pygame.sprite import Sprite

from game.utils.constants import SHIELD, SCREEN_WIDTH, SCREEN_HEIGHT

# sprite es un objeto de pygame (objeto dibujable)
class Shield:
    def __init__(self):
        self.image = SHIELD
        self.image_width = 50
        self.image_height = 50
        self.image = pygame.transform.scale(self.image, (self.image_width,self.image_height))
        self.rect = self.image.get_rect()
        # definimos los valores de self.rect.x e y con los que iniciara la nave
        self.rect.x = 0
        self.rect.y = 0 # nos permite que la nave completa aparezca por encima del borde inferior de la pantalla
        # definimos la valocidad en 5
        self.speed = 6
        self.is_active = True
        self.direction = [-1,1]

    def update(self):
        if self.rect.y > SCREEN_HEIGHT or self.rect.x < -self.image_width or self.rect.x > SCREEN_WIDTH:
            self.is_active = False
        direction = random.choice(self.direction)
        if direction == -1:
            self.move_to_left()
        else:
            self.move_to_right()

    def move_to_right(self):
        self.rect.x += self.speed
        self.rect.y += self.speed    

    def move_to_left(self):
        self.rect.x -= self.speed
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

