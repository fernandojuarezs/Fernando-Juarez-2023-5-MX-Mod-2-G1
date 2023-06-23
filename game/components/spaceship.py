import pygame

from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP_SHIELD

from game.components.bullet_spaceship import BulletSpaceship # lo importamos para acceder a todos los metodos de las balas. Importante, no creamos ningun objeto BulletSpaceship en los atributos de la nave. Lo mismo se hizo con enemy handler. 

# sprite es un objeto de pygame (objeto dibujable)
class Spaceship(Sprite):
    name_image = "spaceship"
    pygame.init()
    bullet_sound = pygame.mixer.Sound('game\components\gun-gunshot-01.wav')    
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
        self.speed = 10
        self.delay_time = 0
        self.bullets_shooted = []
        self.is_alive = True
        self.is_indestructible = False # atributo que indica si trae consigo un escudo
        self.current_score = 0 

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for bullet in self.bullets_shooted:
            bullet.draw(screen)

    def update(self, keyboard_events):
        if keyboard_events[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH-self.image_width: # permite que la nave completa no se salga del borde lateral derecho
            self.move_to_right()
        if keyboard_events[pygame.K_LEFT] and self.rect.x > 0:
            self.move_to_left()
        if keyboard_events[pygame.K_UP] and self.rect.y > -self.image_height:
            self.move_up()
        if keyboard_events[pygame.K_DOWN] and self.rect.y < SCREEN_HEIGHT-self.image_height:
            self.move_down()
        if keyboard_events[pygame.K_SPACE] and self.delay_time % 4 == 0:
            self.bullets_shooted.append(BulletSpaceship(self.rect.x, self.rect.y))
            self.bullet_sound.play()
        for bullet in self.bullets_shooted:
            bullet.update()
            if not bullet.is_active:
                self.bullets_shooted.remove(bullet)
        self.delay_time += 1

    def move_to_right(self):
        self.rect.x += self.speed
    
    def move_to_left(self):
        self.rect.x -= self.speed

    def move_down(self):
        self.rect.y += self.speed
    
    def move_up(self):
        self.rect.y -= self.speed


