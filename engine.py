import numpy as np
import pygame

class Engine():
    """
        основной класс, в котором находятся методы для прорисовки
        рабочего стола
    """
    def __init__(self):
        self.shape = (15, 15, 15, 15)

        self.plr_num = 1
        self.global_text = ""

        self.WINDOW_SIZE = (
            self.shape[1] * 30, 
            self.shape[0] * 30
            )
        
        self.FPS = 30
        self.GAME_POLIGON = np.zeros(self.shape,
                                     dtype=int)
        self.RADIUS = self.WINDOW_SIZE[0]//35
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
        self.STRIDE = 40

        self.selected_point = [0, 0, 0, 0]
        self.SELECTED_POINTS: list[tuple] = [] #tuple (x,y,z,w, idx_player) 
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE,
                                              pygame.RESIZABLE)
        pygame.display.set_caption('4D Gomoku')

    def redraw_board(self):
        pygame.init()

        font_text = pygame.font.Font('freesansbold.ttf', 32)
        text = font_text.render(self.global_text,
                            True, 
                            self.colors["BLACK"],
                            self.colors["WHITE"])
        textRect = text.get_rect()
        textRect.center = (self.WINDOW_SIZE[0] // 2, 
                            self.WINDOW_SIZE[1] // 2 + 170)
        self.screen.blit(text, textRect,)

        pygame.display.flip()

    def available_step(self):
        """
        Можно ли сходить в выбранную точку
        """
        if self.GAME_POLIGON[self.selected_point[0],
                              self.selected_point[1],
                              self.selected_point[2],
                              self.selected_point[3]] == 0:
            return True
        else:
            return False
        
    def draw_board(self):
        self.screen.fill(self.colors["WHITE"])

        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                color = self.colors["BLACK"]

                if self.GAME_POLIGON[x, y, self.selected_point[2],
                                     self.selected_point[3]] == -1:
                    color = self.colors["RED"]
                elif self.GAME_POLIGON[x, y, self.selected_point[2],
                                       self.selected_point[3]] == 1:
                    color = self.colors["BLUE"]

                pygame.draw.circle(
                    self.screen,
                    color,
                    (x * self.CELL_SIZE+self.STRIDE, y * self.CELL_SIZE+self.STRIDE),
                            self.RADIUS)
        pygame.draw.circle(
            self.screen,
            self.colors["GREEN"],
            (self.selected_point[0] * self.CELL_SIZE+self.STRIDE,
             self.selected_point[1] * self.CELL_SIZE+self.STRIDE),
            self.RADIUS
        )


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

        elif event.key == pygame.K_RETURN:
            if self.available_step():
            
                self.GAME_POLIGON[self.selected_point[0],
                                self.selected_point[1],
                                self.selected_point[2],
                                self.selected_point[3]] = self.plr_num
                self.plr_num *= -1
                self.global_text = ""
            
            else:
                # TODO сделать глобальные надписи
                # чтобы можно было делать задержку

                self.global_text = "Точка уже занята!!!"
