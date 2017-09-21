import pygame

from pygame import *

WIN_WIDTH = 800                     #ширина окна
WIN_HEIGHT = 640                    #высота окна
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)   #поместим высоту и ширину в один объект
      #цвет заднего фона
BLOCK_COLOR = Color("#FF6262")
TOWER_COLOR = Color("#000000")
TRIANGLE_COLOR = Color("#00BFFF")


def main():
    BACKGROUND_COLOR = Color("#FFFFFF")
    BRUSH_COLOR = Color("#FF0000")
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Paint")
    background = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создаём рабочую область, её размеры совпадают с размерами окна
    background.fill(BACKGROUND_COLOR)  # Заполняем её цветом заднего фона
    screen.blit(background, (0, 0))
    draw = False
    triangle_in_mouse = False
    rect_in_mouse = False
    circle_in_mouse = False

    fontObj = pygame.font.Font('Purista Bold Italic.otf', 20)

    clock = pygame.time.Clock()

    while 1:

        for event in pygame.event.get():  # Для всех событий проверяем, какие случились
            if event.type == QUIT:  # Если случился выход, то
                raise SystemExit("QUIT")  # Закрывает
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    draw = True
                elif event.button == 3:
                    triangle_in_mouse = False
                    rect_in_mouse = False
                    circle_in_mouse = False

            if event.type == MOUSEBUTTONUP:
                draw = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    screen.blit(background, (0, 0))

        if draw:
            pos = pygame.mouse.get_pos()
            if pos[1] > 70 and not triangle_in_mouse and not rect_in_mouse and not circle_in_mouse:
                pygame.draw.circle(screen, BRUSH_COLOR, pos, 10, 0)
            elif (pos[1] < 60 and pos[0] >= 20 and pos[0] <= 180):
                triangle_in_mouse = True
                rect_in_mouse = False
                circle_in_mouse = False
            elif (pos[1] < 60 and pos[0] > 180 and pos[0] <= 350):
                rect_in_mouse = True
                circle_in_mouse = False
                triangle_in_mouse = False
            elif (pos[0] > 350 and pos[0] <= 420 and pos[1] < 60):
                circle_in_mouse = True
                rect_in_mouse = False
                triangle_in_mouse = False
            elif pos[0] >= 420 and pos[0] < 520 and pos[1] > 20 and pos[1] <= 40:
                circle_in_mouse = False
                rect_in_mouse = False
                triangle_in_mouse = False
                BRUSH_COLOR = Color("#FF0000")
            elif pos[0] >= 420 and pos[0] < 520 and pos[1] > 40 and pos[1] <= 60:
                circle_in_mouse = False
                rect_in_mouse = False
                triangle_in_mouse = False
                BRUSH_COLOR = BACKGROUND_COLOR


        if draw and (triangle_in_mouse or rect_in_mouse or circle_in_mouse):
            pos = pygame.mouse.get_pos()
            if pos[1] > 70:
                if triangle_in_mouse:
                    pygame.draw.polygon(screen, TRIANGLE_COLOR,((pos[0] - 70, pos[1] + 40), (pos[0] + 70, pos[1] + 40), (pos)), 5)
                if rect_in_mouse:
                    pygame.draw.rect(screen, TRIANGLE_COLOR, (pos[0], pos[1], 140, 40))
                if circle_in_mouse:
                    pygame.draw.circle(screen, TRIANGLE_COLOR, pos, 20, 5)

        upload_menu_punkt = fontObj.render('Upload', True, TRIANGLE_COLOR)
        brush_menu_punkt = fontObj.render('Brush', True, TRIANGLE_COLOR)
        eraser_menu_punkt = fontObj.render('Eraser', True, TRIANGLE_COLOR)

        upload_menu = upload_menu_punkt.get_rect()
        upload_menu.center = (480, 7)

        brush_menu =  brush_menu_punkt.get_rect()
        brush_menu.center = (480, 27)

        eraser_menu = eraser_menu_punkt.get_rect()
        eraser_menu.center = (480, 47)

        pygame.draw.rect(screen, BLOCK_COLOR, (0, 0, 800, 60))
        pygame.draw.polygon(screen, TRIANGLE_COLOR, ((30, 50), (170, 50), (100, 10)), 0)
        pygame.draw.rect(screen, TRIANGLE_COLOR, (200, 10, 140, 40))
        pygame.draw.circle(screen, TRIANGLE_COLOR, (390, 30), 20, 0)
        screen.blit(upload_menu_punkt, upload_menu)
        screen.blit(brush_menu_punkt, brush_menu)
        screen.blit(eraser_menu_punkt, eraser_menu)

        pos = pygame.mouse.get_pos()

        if pos[0] >= 20 and pos[0] <= 180 and pos[1] <= 60:
            pygame.draw.polygon(screen, TOWER_COLOR, ((30, 50), (170, 50), (100, 10)), 0)

        if pos[0] > 180 and pos[0] <= 350 and pos[1] <= 60:
            pygame.draw.rect(screen, TOWER_COLOR, (200, 10, 140, 40))

        if pos[0] > 350 and pos[0] <= 420 and pos[1] <= 60:
            pygame.draw.circle(screen, TOWER_COLOR, (390, 30), 20, 0)

        if pos[0] >= 420 and pos[0] < 520 and pos[1] <= 20:
            in_upload_punkt_menu = True
        else:
            in_upload_punkt_menu = False

        if pos[0] >= 420 and pos[0] < 520 and pos[1] > 20 and pos[1] <= 40:
            in_brush_punkt_menu = True
        else:
            in_brush_punkt_menu = False

        if pos[0] >= 420 and pos[0] < 520 and pos[1] > 40 and pos[1] <= 60:
            in_eraser_punkt_menu = True
        else:
            in_eraser_punkt_menu = False

        if in_upload_punkt_menu:
            upload_menu_punkt = fontObj.render('Upload', True, TOWER_COLOR)
            screen.blit(upload_menu_punkt, upload_menu)

        if in_brush_punkt_menu:
            upload_brush_punkt = fontObj.render('Brush', True, TOWER_COLOR)
            screen.blit(upload_brush_punkt, brush_menu)

        if in_eraser_punkt_menu:
            upload_eraser_punkt = fontObj.render('Eraser', True, TOWER_COLOR)
            screen.blit(upload_eraser_punkt, eraser_menu)

        pygame.display.update()



if __name__ == "__main__":
    main()
