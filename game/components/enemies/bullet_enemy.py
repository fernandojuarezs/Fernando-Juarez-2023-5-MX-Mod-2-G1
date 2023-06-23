import pygame

from pygame.sprite import Sprite

from game.utils.constants import BULLET_ENEMY, SCREEN_WIDTH, SCREEN_HEIGHT

# sprite es un objeto de pygame (objeto dibujable)
class BulletEnemy:
    def __init__(self, enemy_xpos, enemy_ypos):
        self.image = BULLET_ENEMY
        self.image_width = 20
        self.image_height = 20
        self.image = pygame.transform.scale(self.image, (self.image_width,self.image_height))
        self.rect = self.image.get_rect()
        # definimos los valores de self.rect.x e y con los que iniciara la nave
        self.rect.x = enemy_xpos
        self.rect.y = enemy_ypos-self.image_height # nos permite que la nave completa aparezca por encima del borde inferior de la pantalla
        # definimos la valocidad en 5
        self.speed = 10
        self.is_active = True

    def update(self):
        if self.rect.y > SCREEN_HEIGHT:
            self.is_active = False
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))



