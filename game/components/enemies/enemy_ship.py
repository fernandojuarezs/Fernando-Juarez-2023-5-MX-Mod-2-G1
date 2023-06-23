import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2

class EnemyShip(Enemy):
    
    WIDTH = 40
    HEIGHT = 60

    image_selected = random.choice([ENEMY_1, ENEMY_2])

    def __init__(self):
        self.image = self.image_selected
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)

