import os
import sys

import pygame
import random

FPS = 50
n = 0
clock = pygame.time.Clock()



p = ['ybloki.jpg', 'ybloki.jpg', 'grusha.jpg', 'grusha.jpg', 'sliva.jpg', 'sliva.jpg']
random.shuffle(p)
b = []

p_n = [p[:3], p[3:]]
picture = {}
picture_1 = {}


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def proverka_cc(x, y):  # координаты
    x0 = (x - 130) // 150
    y0 = (y - 100) // 150
    if -1 < x0 < 2 and -1 < y0 < 3: # x = 0, 1; y = 0, 1, 2
        return y0, x0
    else:
        print(None)


def finish(one, two):
    picture_1[one] = 1
    picture_1[two] = 1
    if len(picture_1) == 6:
        print("FINISH")
        return True


def end_screen():
    intro_text = ["ПОЗДРАВЛЯЕМ!", " ", "ВЫ СОБРАЛИ ВСЕ ФРУКТЫ.", "МОЛОДЦЫ!"]
    back = pygame.image.load('tree.jpg')
    screen.blit(back, (0, 0))
    pygame.draw.rect(screen, (200, 255, 200), (40, 100, 530, 300))
    pygame.draw.rect(screen, (150, 255, 150), (40, 100, 530, 300), 8)

    pygame.display.update()
    font = pygame.font.Font(None, 50)
    text_coord = 150

    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color((255, 0, 255)))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 70
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def look(z):  # показать
    image = load_image(p_n[z[1]][z[0]])
    image1 = pygame.transform.scale(image, (150, 150))  # размер картинки
    screen.blit(image1, (130 + 150 * z[1] + 20 * z[1], 100 + 150 * z[0] + 20 * z[0]))  # нахождение картинки


ap = []
print(picture)
flag = False


def button():
    screen.fill((100, 150, 200))
    size = [190, 45]
    text = 'Старт'
    rect_button = pygame.Rect(350, 300, size[0], size[1])


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Найдите пару')
    screen = pygame.display.set_mode((600, 650))
    screen.fill((100, 150, 200))

    back = pygame.image.load('tree.jpg')
    screen.blit(back, (0, 0))
    pygame.display.update()

    running = True
    lo_f, lo_s = False, False
    for i in range(2):  # расположение карточек
        for j in range(3):
            picture[i, j] = 1
            image = load_image("short.png")
            image1 = pygame.transform.scale(image, (150, 150))  # размер картинки
            screen.blit(image1, (130 + 150 * i + 20 * i, 100 + 150 * j + 20 * j))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                z1 = proverka_cc(x, y)
                st = pygame.time.get_ticks()
                if z1:
                    look(z1)
                    if z1 not in ap:
                        ap.append(z1)

                if len(ap) == 3:
                    print(ap)
                    if p_n[ap[0][1]][ap[0][0]] == p_n[ap[1][1]][ap[1][0]]:
                        print('Right')
                        if finish(ap[0], ap[1]):
                            break
                        ap = [ap[-1]]
                    else:
                        print('NOO')
                        st = pygame.time.get_ticks()
                        while st + 1000 > pygame.time.get_ticks():
                            image = load_image("short.png")
                            image1 = pygame.transform.scale(image, (150, 150))  # размер картинки
                            screen.blit(image1, (130 + 150 * ap[0][1] + 20 * ap[0][1], 100 + 150 * ap[0][0] + 20 * ap[0][0]))
                            screen.blit(image1, (130 + 150 * ap[1][1] + 20 * ap[1][1], 100 + 150 * ap[1][0] + 20 * ap[1][0]))
                        ap = [ap[-1]]
                elif len(ap) > 3:
                    ap = []
                elif len(ap) == 2:
                    if finish(ap[0], ap[1]):
                        flag = True
                        break
        pygame.display.flip()
        pygame.time.wait(10)
        if flag:
            pygame.time.wait(2200)
            end_screen()

        pygame.display.flip()
        pygame.time.wait(10)
    pygame.quit()
