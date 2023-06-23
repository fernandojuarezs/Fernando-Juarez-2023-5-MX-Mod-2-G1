import pygame
import sys

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, GAME_OVER

class GameOver:
    font = pygame.font.Font(FONT_STYLE, 40) # fuente que se utilizara
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
         # lista para mantener los scores

    # este metodo permite resetar algunos atributos del jugador
    def reset(self, player):
        player.is_alive = True
        player.current_score = 0

    # metodo que permite mostrar el puntaje, el maximo puntaje y las muertes
    def display_game_over(self, current_score, total_deaths, game_scores):
        self.screen.fill((255, 255, 255)) # dibujo una pantalla blanca
        
        game_over_image = pygame.transform.scale(GAME_OVER, (400,100)) # utilizo la imagen de game over y le asigno un ancho de 400 y un alto de 100
        self.screen.blit(game_over_image, (200,100)) # posiciono la imagen en 200 y en 100

        play_again = "Press any key to play again"
        score = "Actual score: " + str(current_score)
        max_score = "Max score: " + str(self.get_max_score(game_scores))
        deaths = "Total deaths: " + str(total_deaths)

        self.render_text(play_again, SCREEN_WIDTH//2, 200)
        self.render_text(score, SCREEN_WIDTH//2, 300)
        self.render_text(max_score,SCREEN_WIDTH//2, 400)
        self.render_text(deaths, SCREEN_WIDTH//2, 500)

        pygame.display.flip()

    # este metodo permite renderizar cualquier texto   
    def render_text(self, text, x_pos, y_pos):
        string = self.font.render(text, True, (0,0,0))
        self.screen.blit(string, (x_pos,y_pos))

    # permite obtener el maximo puntaje de game scores
    def get_max_score(self, game_scores):
        return max(game_scores)
