import pygame

import random

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

from game.components.spaceship import Spaceship

from game.components.enemy import Enemy

from game.components.bullet_spaceship import Bullet


# Game tiene un Spaceship
# Game puede decirle al spaceship que se actualice llamandole al metodo update(). update() espera una lista que contiene los eventos de teclado que ocurrieron
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10 # el numero de pixeles que el "objeto / imagen" se mueve en patalla
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.number_of_enemies = None
        self.list_of_enemies = []
        self.create_new_group_of_enemies = False
        self.spaceship_collision = False
        self.shooted = False

    # establece un numero aleatorio de enemigos entre 1 y 6
    def set_random_number_of_enemies(self):
        random_number_of_enemies = random.randint(1,6)
        self.number_of_enemies = random_number_of_enemies

    # crea multiples enemigos a partir de la clase enemigos y del numero de de enemigos del juego y los va colocando de izquierda a derecha
    def make_multiple_enemies(self):
        # creamos los nombres de los enmigos de acuerdo al numero de estos y los ponemos en la lista de enemigos
        """for i in range(self.number_of_enemies):
            enemyname = "enemy"+str(i+1)
            self.list_of_enemies.append(enemyname)
        """
        # cada elemento de la lista sera un objeto de la clase Enemy
        for j in range(self.number_of_enemies):
            self.list_of_enemies.insert(j,Enemy())
        
        self.set_position_of_enemies()


    # set_position_of_enemies nos ayuda a establecer la posicion inicial de los enemigos con base en el atributo de cantidad de enemigos
    def set_position_of_enemies(self):
        # establecemos donde aparecera cada enemigo
        screen_division = int(SCREEN_WIDTH/self.number_of_enemies) # screen_division nos da el grosor de cada subpantallap
        position_x = int(screen_division/2) # position_x nos ayudara a establecer el enemigo en la mitad de cada subpantalla
        
        # para colocar a cada enemigo lo colocamos en la mitad de cada subpantalla mas una distancia de tantas subpantallas igual al numero de enemigo que es
        for k in range(self.number_of_enemies):
            self.list_of_enemies[k].rect.x = position_x + k*screen_division

    # delete_group_of_enemies_beyond_screen nos permite eliminar vaciar la lista de enemigos cuando todos hayan salido de la pantalla
    def delete_group_of_enemies_beyond_screen(self):
        counter_of_enemies_out_of_screen = 0 
        # mientras el contador de enemigos que estan fuera de pantalla sea menor que la cantidad de enemigos inicial, para cada enemigo en la lista verifica que
        while (counter_of_enemies_out_of_screen < self.number_of_enemies):
            for i in range(self.number_of_enemies):
                if self.list_of_enemies[i].rect.y > SCREEN_HEIGHT: # si hay un enemigo en la lista de enemigos cuya posicion en y sea mayor que la altura en la pantalla
                    counter_of_enemies_out_of_screen += 1 # aumenta en uno el contador de enemigos fuea de la pantala
            if counter_of_enemies_out_of_screen == self.number_of_enemies: # si el contador de enemigos que estan fuera de la pantalla es igual a la cantidad de enemigos que se crearon
                self.list_of_enemies.clear() # vacia la lista de enemigos
                self.create_new_group_of_enemies = True # cambia el estado del atributo de crear_nuevo_grupo_de_enemigos de la clase Game a verdadero
                break
            if self.create_new_group_of_enemies == False: # si el atributo de crear_nuevo_grupo_de_enemigos de la clase Game sigue siendo falso, salte del while
                break

    # el metodo check_collision_of_spaceship verifica si alguna nave enemiga colisiono con la nave
    def check_collision_of_spaceship(self):
        for i in range(0,self.number_of_enemies):
            if self.spaceship.rect.colliderect(self.list_of_enemies[i]) == True:
                self.spaceship_collision = True

    # el metodo checar colisiones entre enemigos permite que dos enemigos se muevan si no estan colisionando
    def check_collision_between_enemies(self):
        if self.number_of_enemies == 1:
            self.list_of_enemies[0].update()
        else:
            for i in range(0,self.number_of_enemies):
                for j in range(i+1,self.number_of_enemies):
                    if self.list_of_enemies[i].rect.colliderect(self.list_of_enemies[j]) == False:
                        self.list_of_enemies[i].update()
                        self.list_of_enemies[j].update()
                    else:
                        pass
    
    def fire_bullet(self, screen):
        bullet = Bullet()
        self.shooted = True
        bullet.draw(screen)
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        # mientras los atributos jugando sea verdadero, crear_nuevo_grupo_de_enemigos sea falso y colision_de_la_nave sea falso
        while self.playing and self.create_new_group_of_enemies == False and    self.spaceship_collision == False:
            # establece un numero aleatorio de enemigos y crea grupos de multiples enemigos y
            self.set_random_number_of_enemies()
            self.make_multiple_enemies()
            while self.playing:
                self.handle_events() # verifica que no se quiera salir
                self.update() # verifica las actualizaciones 
                if self.spaceship_collision == True: # si despues del update de Game, el estado de colision de la nave cambia a verdadero, salte del juego
                    break
                self.delete_group_of_enemies_beyond_screen() # elimina al grupo de enemigos (si todos estan fuera de la pantalla)
                if self.create_new_group_of_enemies == True: # si el atributo de crear nuevo grupo de enemigos es verdadero
                    self.create_new_group_of_enemies = False # cambialo a falso inmediatamento y salte del while
                    break
                self.draw() # dibuja

        else:
            print("Something ocurred to quit the game!")
            pygame.display.quit()
            pygame.quit()

    def handle_events(self):
        # pygame.event.get() es un iterable (lista)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #el QUIT event es el click en el icono que cierra ventana
                self.playing = False
            
    # update de Game llama al update de algunos de los objetos de mi juego
    def update(self):
        events = pygame.key.get_pressed() # pygame.key.get_pressed() obtiene los eventos del teclado en un game loops        
        
        self.spaceship.update(events)
        
        # como enemy se mueve de manera indepediente de las teclas que el usuario presione, no es necesario pasarle events
        self.check_collision_of_spaceship()
        self.check_collision_between_enemies() # recordar que dentro del metodo check_collision_between_enemies se actualiza el estado de los enemigos

    
    def draw(self):
        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar
        self.screen.fill((255, 255, 255)) # lleno el screen de color BLANCO???? 255, 255, 255 es el codigo RGB
        self.draw_background()

        # Game le ordena al spaceship dibujarse llamando a un metodo llamando draw del Spaceship (el metodo draw espera que le pase screen)
        self.spaceship.draw(self.screen)

        # Game le ordena a los enemigos de la lista dibujarse llamando a un metodo llamando draw del Enemy (el metodo draw espera que le pase screen)
        #self.enemy.draw(self.screen)
        for i in range(self.number_of_enemies):
            self.list_of_enemies[i].draw(self.screen)

        

        pygame.display.update() # esto hace que el dibujo se actualice en el display de pygame
        pygame.display.flip()  # hace el cambio

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()# alto de la imagen
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) # blit "dibuja"
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    

