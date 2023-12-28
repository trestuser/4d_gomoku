import numpy as np
import pygame

class Engine():
    def __init__(self):
        self.shape = (15, 15, 15, 15)

        self.plr_num = 1
        self.WINDOW_SIZE = (
            self.shape[1] * 25, 
            self.shape[0] * 25
            )
        self.FPS = 30
        self.GAME_POLIGON = np.zeros(self.shape,
                                     dtype=int)
        self.RADIUS = 10
        self.CELL_SIZE = self.RADIUS*2

        self.colors = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "RED": (255, 0, 0),
            "BLUE": (0, 0, 255),
            "GREEN": (0, 200, 64)
            }

        # Создается окно

        # TODO добавить динамическое изменение
        # в зависимости от размера поля

        # self.font = pygame.font.Font(None, 36)
        self.STRIDE = 20

        self.selected_point = [0, 0, 0, 0]
        self.SELECTED_POINTS: list[tuple] = [] #tuple (x,y,z,w, idx_player) 
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption('4D Gomoku')

    def redraw_board(self):
        pygame.init()
        pygame.display.flip()

    def available_step(self):
        """
        Можно ли сходить в выбранную точку
        """
        pass
        
    def draw_board(self):
        self.screen.fill(self.colors["WHITE"])
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                for z in range(self.shape[2]):
                    for w in range(self.shape[3]):
                        pygame.draw.circle(
                            self.screen,
                            self.colors["BLACK"],
                            (y * self.CELL_SIZE+self.STRIDE, x * self.CELL_SIZE+self.STRIDE),
                            self.RADIUS)
                        # TODO прорисовка выбранных точек
                        if self.GAME_POLIGON[x, y, z, w] == 1:
                            pygame.draw.circle(
                                self.screen,
                                self.colors["RED"],
                                (y * self.CELL_SIZE+self.STRIDE, x * self.CELL_SIZE+self.STRIDE),
                                self.RADIUS)
        pygame.draw.circle(
            self.screen,
            self.colors["GREEN"],
            (self.selected_point[0] * self.CELL_SIZE+self.STRIDE,
             self.selected_point[1] * self.CELL_SIZE+self.STRIDE),
            self.RADIUS
        )
                        # TODO активность с игроком
                        # if [x, y, z, w] == selected_point:
                        #     pygame.draw.circle(screen, BLUE, (y * CELL_SIZE+STRIDE, x * CELL_SIZE+STRIDE), RADIUS)

    def handle_arrow_keys(self, event):
        if event.key == pygame.K_LEFT and self.selected_point[2] > 0:
            self.selected_point[2] -= 1
        elif event.key == pygame.K_RIGHT and self.selected_point[2] < self.shape[2] - 1:
            self.selected_point[2] += 1
        elif event.key == pygame.K_UP and self.selected_point[3] < self.shape[3] - 1:
            self.selected_point[3] += 1
        elif event.key == pygame.K_DOWN and self.selected_point[3] > 0:
            self.selected_point[3] -= 1
        elif event.key == pygame.K_w and self.selected_point[1] > 0:
            self.selected_point[1] -= 1
        elif event.key == pygame.K_s and self.selected_point[1] < self.shape[1] - 1:
            self.selected_point[1] += 1
        elif event.key == pygame.K_a and self.selected_point[0] > 0:
            self.selected_point[0] -= 1
        elif event.key == pygame.K_d and self.selected_point[0] < self.shape[0] - 1:
            self.selected_point[0] += 1
        #elif event.key == pygame.K_RETURN:
        #    self.GAME_POLIGON[self.selected_point[0]; self.selected_point[1]] = self.plr_num
