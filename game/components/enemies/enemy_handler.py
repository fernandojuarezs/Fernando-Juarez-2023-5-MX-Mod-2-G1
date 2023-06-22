import random

from game.components.enemies.enemy_ship import EnemyShip

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT


class EnemyHandler:
    number_of_enemies = None

    def __init__(self):
        self.enemies = []
        self.delay_time = 0
        self.enemies_died = 0
        self.deaths_of_player = 0

    def update(self):
        if self.enemies == []:
            self.set_random_number_of_enemies()
            self.make_multiple_enemies()
            for enemy in self.enemies:
                enemy.is_shooting = True
        else:
            for enemy in self.enemies:
                enemy.update()
                if enemy.is_alive == False:
                    self.remove_enemy(enemy)
                if enemy.is_shooting == False and self.delay_time % 30 == 0:
                    enemy.is_shooting = True
        self.delay_time += 1

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        
    # establece un numero aleatorio de enemigos entre 1 y 6
    def set_random_number_of_enemies(self):
        random_number_of_enemies = random.randint(1,5)
        self.number_of_enemies = random_number_of_enemies

    # crea multiples enemigos a partir de la clase enemigos y del numero de de enemigos del juego y los va colocando de izquierda a derecha
    def make_multiple_enemies(self):
        # cada elemento de la lista sera un objeto de la clase Enemy
        for j in range(self.number_of_enemies):
            self.enemies.insert(j,EnemyShip())
        self.set_position_of_enemies()

    # set_position_of_enemies nos ayuda a establecer la posicion inicial de los enemigos con base en el atributo de cantidad de enemigos
    def set_position_of_enemies(self):
        # establecemos donde aparecera cada enemigo
        screen_division = int(SCREEN_WIDTH/self.number_of_enemies) # screen_division nos da el grosor de cada subpantallap
        position_x = int(screen_division/2) # position_x nos ayudara a establecer el enemigo en la mitad de cada subpantalla
        
        # para colocar a cada enemigo lo colocamos en la mitad de cada subpantalla mas una distancia de tantas subpantallas igual al numero de enemigo que es
        for k in range(self.number_of_enemies):
            self.enemies[k].rect.x = position_x + k*screen_division

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def die_by_bullet(self, bullets):
        for enemy in self.enemies:
            for bullet in bullets:
                if enemy.rect.colliderect(bullet.rect):
                    enemy.is_alive = False
                    self.enemies_died += 1

    def kill_by_bullet(self, player):
        for enemy in self.enemies:
            for bullet in enemy.bullets_shooted:
                if bullet.rect.colliderect(player.rect):
                    player.is_alive = False
                    self.deaths_of_player += 1


    

