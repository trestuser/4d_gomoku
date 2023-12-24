import numpy as np
import pygame
import sys
from engine import Engine

# TODO Добавить красивые переходы между осями
# TODO Подсветка активного круга
# TODO отображение координат по w,z на игровом поле
# TODO добавить возможность хода
## TODO переключение между игроками
## TODO добавление выбранных точек в структуру
## TODO отрисовка точек из структы

class teacher():
    """
    Отвечает ход машины
    """
    def make_step(self):
        return np.random.randint()
    
class player():
    """
    Отвечает ход машины
    """
    def make_step(self):
        return np.random.randint()

# def check_win(player):
#     pass

# # TODO переделать
# def draw_info(text_list):
#     text = font.render("akdfj;asdfkja;lkdfja;ldfjkasdf;jka", True, BLACK)
#     screen.blit(text, (50, 50))


def handle_arrow_keys(event):
    global selected_point
    if event.key == pygame.K_LEFT and selected_point[2] > 0:
        selected_point[2] -= 1
    elif event.key == pygame.K_RIGHT and selected_point[2] < shape[2] - 1:
        selected_point[2] += 1
    elif event.key == pygame.K_UP and selected_point[3] < shape[3] - 1:
        selected_point[3] += 1
    elif event.key == pygame.K_DOWN and selected_point[3] > 0:
        selected_point[3] -= 1
    elif event.key == pygame.K_w and selected_point[1] > 0:
        selected_point[1] -= 1
    elif event.key == pygame.K_s and selected_point[1] < shape[1] - 1:
        selected_point[1] += 1
    elif event.key == pygame.K_a and selected_point[0] > 0:
        selected_point[0] -= 1
    elif event.key == pygame.K_d and selected_point[0] < shape[0] - 1:
        selected_point[0] += 1



def game_loop():
    clock = pygame.time.Clock()
    workspace = Engine()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key in (pygame.K_LEFT,
                                   pygame.K_RIGHT,
                                   pygame.K_UP,
                                   pygame.K_DOWN,
                                   pygame.K_w,
                                   pygame.K_s,
                                   pygame.K_a,
                                   pygame.K_d,
                                   ):
                    handle_arrow_keys(event)
                    
                    print(*selected_point)
            
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         selected_point = [event.pos[1] // CELL_SIZE, event.pos[0] // CELL_SIZE, 0, 0]
            #         print(*selected_point)
            #     elif event.button == 3:
            #         arrow_rect = pygame.Rect(WINDOW_SIZE[0] // 2-60, WINDOW_SIZE[1]-60, 50, 50)
            #         if arrow_rect.collidepoint(event.pos):
            #             if arrow_rect.collidepoint(event.pos[0], event.pos[1]):
            #                 selected_point[0] = max(0, selected_point[2] - 1)
            #             elif arrow_rect.collidepoint(event.pos[0], event.pos[1]-100):
            #                 selected_point[0] = min(shape[0] - 1, selected_point[2] + 1)
        
        # draw_info(selected_point)
        # pygame.draw.circle(screen, BLACK, (y * CELL_SIZE+STRIDE, x * CELL_SIZE+STRIDE), RADIUS)
        
        workspace.redraw_board()
        workspace.draw_board()
        
        # draw_arrows()

        

        clock.tick(workspace.FPS)

if __name__ == "__main__":
    game_loop()