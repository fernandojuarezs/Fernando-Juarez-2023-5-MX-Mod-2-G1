import random
import pygame

from game.components.enemies.enemy_ship import EnemyShip

from game.components.shield_handler import ShieldHandler

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP_SHIELD, SPACESHIP

class EnemyHandler:
    pygame.init()
    explosion_sound = pygame.mixer.Sound('game\components\enemies\explosion-03.wav')
    number_of_enemies = None

    def __init__(self):
        self.enemies = []
        self.delay_time = 0
        self.enemies_died = 0
        self.deaths_of_player = 0
        self.counter_to_delete_indestructible_defense = 0

    # si la lista de enemigos esta vacia, va a crear un numero de enemigos y a cada enemigo en la lista, le cambiara su estado a verdadero para disparar
    # en caso de que la lista no este vacia, cada enemigo se actualiza, elimina los enemigos que no esten vivos y permitira disparar con cierto retrado
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
                    self.enemies_died += 1
                if enemy.is_shooting == False and self.delay_time % 70 == 0:
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

    # permite eliminar a los enemigos por la bala del jugador y aumenta en uno los enemigos muertos
    def die_by_bullet(self, bullets):
        for enemy in self.enemies:
            for bullet in bullets:
                if enemy.rect.colliderect(bullet.rect):
                    enemy.is_alive = False
                    self.explosion_sound.play()

    # permite matar al jugador por balas y aumenta en uno las muertes del jugador. Si el jugador tiene escudo, al tercer contacto con bala pierde el escudo
    def kill_by_bullet(self, player, spacheship_xpos, spaceship_ypos):
        for enemy in self.enemies:
            for bullet in enemy.bullets_shooted:
                if bullet.rect.colliderect(player.rect):
                    bullet.is_active = False
                    if player.name_image == "spaceship":
                        print("me dieron sin escudo")
                        player.is_alive = False
                        self.deaths_of_player += 1
                    else:
                        print("me dieron con escudo")
                        self.counter_to_delete_indestructible_defense += 1
                        if self.counter_to_delete_indestructible_defense % 3 == 0:
                            self.deactive_shield_for_spaceship(player, spacheship_xpos, spaceship_ypos)

    # permite resetar la imagen del spaceship para que quede sin escudo
    def deactive_shield_for_spaceship(self, player, spacheship_xpos, spaceship_ypos):
        player.image = SPACESHIP
        player.name_image = "spaceship"
        player.image_width = 50
        player.image_height = 60
        player.image = pygame.transform.scale(player.image, (player.image_width,player.image_height))
        player.rect = player.image.get_rect()
        player.rect.x = spacheship_xpos
        player.rect.y = spaceship_ypos
        player.is_indestructible = False





    

