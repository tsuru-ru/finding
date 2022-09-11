import os
import sys
import pygame
import random

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


def finish(one, two, n):
    if n == 3:
        picture_1[one] = 1
        picture_1[two] = 1
        print(picture_1)
        if len(picture_1) == 6:
            print("FINISH")
            return True
    if n == 2:
        if one not in picture_1 and two not in picture_1:
            if len(picture_1) == 4:
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


class Player(pygame.sprite.Sprite):
    def __init__(self, columns, rows, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.cut_sheet(pygame.image.load('butter1.png'), columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.image = pygame.image.load('butter1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (w, h)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player1 = Player(10, 1, 80, 85, 450, 365)
player2 = Player(10, 1, 80, 85, 930, 365)
player3 = Player(10, 1, 80, 85, 450, 120)
player4 = Player(10, 1, 80, 85, 930, 120)
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(player3)
all_sprites.add(player4)
ap = []
print(picture)
flag = False


def button():
    screen.fill((100, 150, 200))
    size = [190, 45]
    text = 'Старт'
    rect_button = pygame.Rect(350, 300, size[0], size[1])


def beginning():
    pygame.display.set_caption('Найдите пару')
    screen = pygame.display.set_mode((600, 650))
    screen.fill((200, 255, 200))
    back = pygame.image.load('tree.jpg')
    screen.blit(back, (0, 0))
    button = pygame.draw.rect(screen, (100, 255, 200), (190, 450, 200, 50))
    pygame.draw.rect(screen, (200, 255, 200), (40, 100, 530, 300))
    pygame.draw.rect(screen, (150, 255, 150), (40, 100, 530, 300), 8)
    description1 = 'В нашей игре вам нужно будет найти пару '
    description2 = 'каждому фрукту, чтобы собрать их с дерева'
    font_button = pygame.font.Font(None, 65)
    font_description = pygame.font.Font(None, 34)
    text = font_button.render("Старт!", True, (0, 255, 0))
    desk_text1 = font_description.render(description1, True, (255, 0, 255))
    desk_text2 = font_description.render(description2, True, (255, 0, 255))
    text_b = text.get_rect()
    text_b.center = button.center

    screen.blit(text, text_b)
    screen.blit(desk_text1, (55, 200))
    screen.blit(desk_text2, (50, 240))


if __name__ == '__main__':
    tab = False
    pygame.init()
    pygame.mixer.init()
    beginning()
    pygame.display.update()
    run = True
    while run:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                if 190 <= x <= 390 and 450 <= y <= 500:
                    print('yes')
                    tab = True
                if tab:

                    pygame.init()
                    pygame.mixer.init()
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
                                        if finish(ap[0], ap[1], 3):
                                            break
                                        ap = [ap[-1]]
                                    else:
                                        print('NOO')
                                        st = pygame.time.get_ticks()
                                        while st + 1000 > pygame.time.get_ticks():
                                            image = load_image("short.png")
                                            image1 = pygame.transform.scale(image, (150, 150))  # размер картинки
                                            screen.blit(image1, (
                                            130 + 150 * ap[0][1] + 20 * ap[0][1], 100 + 150 * ap[0][0] + 20 * ap[0][0]))
                                            screen.blit(image1, (
                                            130 + 150 * ap[1][1] + 20 * ap[1][1], 100 + 150 * ap[1][0] + 20 * ap[1][0]))
                                        ap = [ap[-1]]
                                elif len(ap) > 3:
                                    ap = []
                                elif len(ap) == 2:
                                    if finish(ap[0], ap[1], 2):
                                        flag = True
                                        break

                        pygame.display.flip()
                        pygame.time.wait(10)
                        if flag:
                            pygame.time.wait(500)
                            end_screen()
                            all_sprites.update()
                            all_sprites.draw(screen)

                        pygame.display.flip()
                        pygame.time.wait(100)
    pygame.quit()
