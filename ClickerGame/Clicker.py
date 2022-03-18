import time

from setting import *
from soundtrack import *

pygame.init()
pygame.font.init()
ps = pygame.font.get_fonts()
print(ps)

bg = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()
sound.play(-1)

screen = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('ClickMouse', 'clickmouse.png')
mouse = pygame.image.load('gamemouse.png')
pygame.display.set_icon(mouse)


def autominer():
    global click
    time.sleep(0.1)
    click = click + autog


def DrawRect():
    pygame.draw.rect(screen, black, (x - 10, y - 10, width + 20, height + 20))
    pygame.draw.rect(screen, grey_blue, (x, y, width, height))

    pygame.draw.rect(screen, black, (50 - 5, 550 - 5, 100 + 10, 50 + 10))
    pygame.draw.rect(screen, grey_blue2, (50, 550, 100, 50))

    pygame.draw.rect(screen, black, (600 - 5, 550 - 5, 100 + 10, 50 + 10))
    pygame.draw.rect(screen, grey_blue3, (600, 550, 100, 50))

    pygame.draw.rect(screen, black, (0, 0, 210, 110))
    pygame.draw.rect(screen, white, (0, 0, 200, 100))


def DrawText(text, dectext, color, x, y, size):
    font = pygame.font.SysFont(dectext, size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


while run_game:
    if run_game:
        autominer()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

        keys = pygame.key.get_pressed()

        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePos = pygame.mouse.get_pos()
            print(MousePos)

            if MousePos >= (300, 0):
                if MousePos <= (500, 0):
                    grey_blue = light_blue
                    click = click + mong
                    soundclick.play(0)

            if MousePos >= (50, 0):
                if MousePos <= (150, 0):
                    if click >= up_click:
                        click = click - up_click
                        up_click = round(up_click * up_factor)
                        up_factor += 0.2
                        grey_blue2 = light_blue
                        mong += 1
                        soundclick.play(0)
                    elif click < up_click:
                        grey_blue2 = red
                        noclick.play(0)

            if MousePos >= (600, 0):
                if MousePos <= (700, 0):
                    if click >= up_autoclick:
                        click = click - up_autoclick
                        up_autoclick = round(up_autoclick * up_auto_factor)
                        up_auto_factor += 0.2
                        grey_blue3 = light_blue
                        autog += 1
                        soundclick.play(0)
                    elif click < up_autoclick:
                        grey_blue3 = red
                        noclick.play(0)
        else:
            grey_blue = (100, 100, 255)
            grey_blue2 = (100, 100, 255)
            grey_blue3 = (100, 100, 255)

    if click >= rank_click:
        if k < len(rank_mass):
            k_mass += 1
            k += 1
            rank_up += 1
            rank_click = round(rank_click * rank_up)
            lvl_up.play(0)
        else:
            ...

    screen.blit(bg, (0, 0))
    DrawRect()
    DrawText('Click: ' + str(click) + '/' + str(rank_click), 'arial.ttf', black, 80, 40, 32)
    DrawText('Factor: ' + str(mong), 'arial.ttf', black, 80, 80, 32)
    DrawText('Auto: ' + str(autog) + '/s', 'arial.ttf', black, 80, 60, 32)
    DrawText('Rank: ' + str(rank_mass[k_mass]), 'arial.ttf', black, 90, 20, 32)
    DrawText('version: 0.033a', 'arial.ttf', white, 700, 20, 30)

    DrawText('Click here = ПКМ', 'arial.ttf', white, x + 100, y - 50, 54)

    DrawText('Upgrade = ' + str(up_click), 'arial.ttf', white, x - 200, y + 250, 36)
    DrawText('Autoclicker = ' + str(up_autoclick), 'arial.ttf', white, x + 350, y + 250, 36)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()