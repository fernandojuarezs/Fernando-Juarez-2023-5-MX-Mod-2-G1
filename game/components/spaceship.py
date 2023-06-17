import pygame

from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

# sprite es un objeto de pygame (objeto dibujable)
class Spaceship(Sprite):
    def __init__(self):
        self.image = SPACESHIP
        self.image_width = 40
        self.image_height = 50
        self.image = pygame.transform.scale(self.image, (self.image_width,self.image_height))
        self.rect = self.image.get_rect()
        # definimos los valores de self.rect.x e y con los que iniciara la nave
        self.rect.x = int(SCREEN_WIDTH/2)
        self.rect.y = SCREEN_HEIGHT-self.image_height # nos permite que la nave completa aparezca por encima del borde inferior de la pantalla
        # definimos la valocidad en 5
        self.speed = 8

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, keyboard_events):
        if keyboard_events[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH-self.image_width: # permite que la nave completa no se salga del borde lateral derecho
            self.move_to_right()
        if keyboard_events[pygame.K_LEFT] and self.rect.x > 0:
            self.move_to_left()

    def move_to_right(self):
        self.rect.x += self.speed
    
    def move_to_left(self):
        self.rect.x -= self.speed





