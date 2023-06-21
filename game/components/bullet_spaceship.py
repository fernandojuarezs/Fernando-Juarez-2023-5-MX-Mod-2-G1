import pygame

from pygame.sprite import Sprite

from game.utils.constants import BULLET, SCREEN_WIDTH, SCREEN_HEIGHT

# sprite es un objeto de pygame (objeto dibujable)
class Bullet(Sprite):
    def __init__(self):
        self.image = BULLET
        self.image_width = 20
        self.image_height = 20
        self.image = pygame.transform.scale(self.image, (self.image_width,self.image_height))
        self.rect = self.image.get_rect()
        # definimos los valores de self.rect.x e y con los que iniciara la nave
        self.rect.x = int(SCREEN_WIDTH/2)
        self.rect.y = SCREEN_HEIGHT-50-10 # nos permite que la nave completa aparezca por encima del borde inferior de la pantalla
        # definimos la valocidad en 5
        self.speed = 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_forward(self):
        while self.rect.y > -20:
            self.rect.y -= self.speed
        
