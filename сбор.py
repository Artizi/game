import pygame
import sys
import random

'''Куча переменных для игры'''
wightlap, heightlap = 900, 500
window = pygame.display.set_mode((900, 500))
wightlap, heightlap = 1000, 500
pygame.display.set_caption("Догонялки")
screen = pygame.Surface((1000, 500))
fon = pygame.image.load('фон.jpg')
zadergka_of_cactus = 0
x_fon = 0
x_of_bird = wightlap
x_of_oblako = wightlap
count_of_animation = 0
count_of_animation_of_object = 0
count_of_animation_of_bird = 0
count_of_animation_of_bird2 = 0
count_of_animation_of_yoj = 0
count_of_animation_of_oblako = 0
state_copy = []

'''данные из фалов (рекорды)'''
with open('statistic\\statistic.txt', mode='r', encoding="utf8") as stat:
    state_of_nomer = str(stat.read()).split('\n')
    state_of_nomer[0] = state_of_nomer[0]
    print(state_of_nomer)
    rec1 = float(state_of_nomer[0])
    rec2 = float(state_of_nomer[1])
    rec3 = float(state_of_nomer[2])


run_1 = False
running_1 = False
run_2 = False
running_2 = False
run_3 = False
running_3 = False
'''Шрифты'''
pygame.font.init()

pygame.mixer.init()
mus_of_menu = pygame.mixer.Sound('sound//555.wav')
mus_of_1 = pygame.mixer.Sound('sound//111.wav')
mus_of_2 = pygame.mixer.Sound('sound//222.wav')
mus_of_3 = pygame.mixer.Sound('sound//3333.wav')

mus_of_jump = pygame.mixer.Sound('sound//jump.wav')
musik = True


class Meny:
    def __init__(self, punkts=[120, 140, u'Punkt,(255,255,30),(255,30,255)),0']):
        global musik
        self.musik = musik
        self.punkts = punkts
        self.punkts_level = [(60, 40, u'Level 1', (255, 255, 30), (0, 255, 25), 0),
                             (60, 80, u'Level 2', (255, 255, 30), (0, 255, 25), 1),
                             (60, 120, u'Level 3', (255, 255, 30), (0, 255, 25), 2),
                             (60, 160, u'Back', (255, 255, 30), (0, 255, 25), 3)]
        self.punkts_records = [(60, 40, 'Record of 1 level - ' + str(rec1), (255, 255, 30), (0, 255, 25), 0),
                               (60, 80, 'Record of 2 level - ' + str(rec2), (255, 255, 30), (0, 255, 25), 1),
                               (60, 120, 'Record of 3 level - ' + str(rec3), (255, 255, 30), (0, 255, 25), 2),
                               (60, 160, 'Back', (255, 255, 30), (0, 255, 25), 3)]

    def rander_records(self, poverhnost, font, num_punkt):
        for i in self.punkts_records:
            if num_punkt == i[5]:
                if not i[2] == 'Back':
                    poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
                else:
                    poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def rander(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def meny(self):
        done = True
        font_meny = pygame.font.SysFont('calibri', 32)
        punkt = 0
        mus_of_menu.play(-1)
        while done:
            screen.blit(fon, (x_fon - 50, 0))
            screen.blit(fon, (x_fon + 850, 0))
            np = pygame.mouse.get_pos()
            for i in self.punkts:
                if np[0] > i[0] - 100 and np[0] < i[0] + 2000 and np[1] > i[1] and np[1] < i[1] + 50:
                    punkt = i[5]
            self.rander(screen, font_meny, punkt)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if event.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if punkt == 0:
                        done = False
                        Meny(self.punkts_level).meny_2()
                    elif punkt == 1:
                        done = False
                        Meny(self.punkts_level).meny_records()
                    elif punkt == 2:
                        sys.exit()
                    elif punkt == 3:
                        musik = False
                        Meny(punkts).meny()
                    elif punkt == 4:
                        musik = False
                        Meny(punkts).meny()
            window.blit(screen, (0, 0))
            pygame.display.flip()

    def meny_2(self):
        global running_1, run_1
        global running_2, run_2
        global running_3, run_3
        done = True
        font_meny = pygame.font.SysFont('calibri', 32)
        punkt = 0
        while done:
            screen.blit(fon, (x_fon - 50, 0))
            screen.blit(fon, (x_fon + 850, 0))

            np = pygame.mouse.get_pos()
            for i in self.punkts_level:
                if np[0] > i[0] - 100 and np[0] < i[0] + 2000 and np[1] > i[1] and np[1] < i[1] + 50:
                    punkt = i[5]
            self.rander(screen, font_meny, punkt)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if event.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if punkt == 0:
                        running_1 = True
                        run_1 = True
                        mus_of_1.play(-1)
                        mus_of_menu.stop()
                        done = False
                    elif punkt == 1:
                        running_2 = True
                        run_2 = True
                        mus_of_2.play(-1)
                        mus_of_menu.stop()
                        done = False
                    elif punkt == 2:
                        running_3 = True
                        run_3 = True
                        mus_of_3.play(-1)
                        mus_of_menu.stop()
                        done = False
                    elif punkt == 3:
                        done = False
                        mus_of_menu.stop()
                        Meny(punkts).meny()
            window.blit(screen, (0, 0))
            pygame.display.flip()

    def meny_records(self):
        done = True
        font_meny = pygame.font.SysFont('calibri', 32)
        punkt = 0
        while done:
            screen.blit(fon, (x_fon - 50, 0))
            screen.blit(fon, (x_fon + 850, 0))

            np = pygame.mouse.get_pos()
            for i in self.punkts_records:
                if np[0] > i[0] - 100 and np[0] < i[0] + 2000 and np[1] > i[1] and np[1] < i[1] + 50:
                    punkt = i[5]
            self.rander_records(screen, font_meny, punkt)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if event.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if punkt == 0:
                        pass
                    elif punkt == 1:
                        pass
                    elif punkt == 2:
                        pass
                    elif punkt == 3:
                        done = False
                        mus_of_menu.stop()
                        Meny(punkts).meny()
            window.blit(screen, (0, 0))
            pygame.display.flip()


size = wightlap, heightlap = 900, 500
screen = pygame.display.set_mode(size)
pygame.display.set_icon(pygame.image.load('icon_whitefon.png'))
fps_of_snar = 5
min_of_smen_of_fps_of_snar = 600
pygame.display.set_caption("Догонялки")
max_of_snaryad = 1000
MAX_of_snaryad = max_of_snaryad
max_of_cactus = (int(wightlap / 125)) * 0 + 3
xlmin, xrmin, yumin, ydmin = 5, 5, 5, 5
wighthero = 60
heighthero = 71
wightobject = 60
heightobject = 80
wight_cuctus = 60
height_cuctus = 100
radius_of_snar = 5
color_of_snar = (255, 0, 0)
know_of_moving = "right"
zadergka_min = 4
zadergka = 10
delta_x = 0
pos_x_of_stoped = (wightlap / 2) - (wighthero / 2) - 100
are_win = False
are_lose = False
couch_of_win = 0
zadergka_of_cactus = 0

veroyatnosty_cactusa = [0, 0, 1]

move_right_image = [pygame.image.load('pygame_right_1.png'), pygame.image.load('pygame_right_2.png'),
                    pygame.image.load('pygame_right_3.png'),
                    pygame.image.load('pygame_right_4.png'), pygame.image.load('pygame_right_5.png'),
                    pygame.image.load('pygame_right_6.png')]
move_left_image = [pygame.image.load('pygame_left_1.png'), pygame.image.load('pygame_left_2.png'),
                   pygame.image.load('pygame_left_3.png'),
                   pygame.image.load('pygame_left_4.png'), pygame.image.load('pygame_left_5.png'),
                   pygame.image.load('pygame_left_6.png')]
notmove_state = pygame.image.load('pygame_idle.png')

cactus_image = pygame.image.load('cactus.png')

not_move_state_object = pygame.image.load('pygame_idle_object.png')

move_bird = [pygame.image.load('bird_1.png'),
             pygame.image.load('bird_2.png'),
             pygame.image.load('bird_3.png'),
             pygame.image.load('bird_4.png'),
             pygame.image.load('bird_5.png'),
             pygame.image.load('bird_6.png')]

move_joh = [pygame.image.load('bird_1.png'),
            pygame.image.load('bird_2.png'),
            pygame.image.load('bird_3.png'),
            pygame.image.load('bird_4.png'),
            pygame.image.load('bird_5.png'),
            pygame.image.load('bird_6.png')]

move_right_image_object = [pygame.image.load('pygame_right_1_malish.png'),
                           pygame.image.load('pygame_right_2_malish.png'),
                           pygame.image.load('pygame_right_3_malish.png'),
                           pygame.image.load('pygame_right_4_malish.png'),
                           pygame.image.load('pygame_right_5_malish.png'),
                           pygame.image.load('pygame_right_6_malish.png')]

fon = pygame.image.load('фон.jpg')
clock = pygame.time.Clock()
x = 50
y = (heightlap - heighthero) - ydmin
speed = 6
dooble_speed = 12
SPEED = speed
hero_jump = False
jump_hero_count = 10
x_object = 250
y_object = (heightlap - heightobject) - ydmin
delta_speed = int(speed / 5)
zadergka_of_cactus_min = random.randint(10, 20) * 6 / speed
left = False
right = False
count_of_animation = 0
count_of_animation_of_object = 0
count_of_animation_of_bird = 0
count_of_animation_of_bird2 = 0
count_of_animation_of_yoj = 0
count_of_animation_of_oblako = 0

wight_bird = 70
height_bird = 50
wight_yoj = 70
height_yoj = 50
wight_oblako = 70
height_oblako = 50
x_of_bird = wightlap
y_of_bird = heightlap - ydmin - height_bird - 100
x_of_bird2 = wightlap
y_of_bird2 = heightlap - ydmin - height_bird - 170
x_of_yoj = wightlap
y_of_yoj = heightlap - ydmin - height_yoj
x_of_oblako = wightlap
y_of_oblako = heightlap - ydmin - height_oblako - 300
x_fon = 0

fps_of_bird = 0
fps_of_bird2 = 150
fps_of_yoj = 150
fps_of_oblako = 125
are_bird = False
are_bird2 = False
are_yoj = False
are_oblako = False
speed_of_bird = 0
SPEED_of_bird = speed_of_bird
speed_of_bird2 = 0
SPEED_of_bird2 = speed_of_bird
speed_of_yoj = 0
SPEED_of_yoj = speed_of_yoj
speed_of_oblako = 0
SPEED_of_oblako = speed_of_oblako


class snaryad():
    def __init__(self, x, y, radius, color, travell, speed_of_hero):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.travell = travell
        self.speed_snar = int(1.6 * travell * speed_of_hero)

    def draw_snar(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + 22, self.y + 15), self.radius)


class cactus():
    def __init__(self, x_cactus, y_cactus):
        self.x_cactus = x_cactus
        self.y_cactus = y_cactus

    def draw_cactus(self, screen):
        screen.blit(cactus_image, (self.x_cactus, self.y_cactus))


def raschet_of_cactus():
    global zadergka_of_cactus, cactusy
    if (len(cactusy) < max_of_cactus) and (zadergka_of_cactus > zadergka_of_cactus_min):
        veroyatnost = random.choice(veroyatnosty_cactusa)
        if veroyatnost == 1:
            cactusy.append(cactus(wightlap - wight_cuctus, heightlap - ydmin - height_cuctus))
            zadergka_of_cactus = 0
    for cactus_one in cactusy:
        if cactus_one.x_cactus >= 0 and cactus_one.x_cactus <= wightlap:
            cactus_one.x_cactus -= speed
        else:
            cactusy.pop(cactusy.index(cactus_one))


def stop_mus():
    mus_of_1.stop()
    mus_of_2.stop()
    mus_of_3.stop()
    mus_of_2.stop()


def draw_win(time):
    global rec1
    global rec2
    global rec3
    font = pygame.font.SysFont('calibri', 50)
    text_of_win = font.render("You win!!!", 0, (0, 255, 0))
    screen.fill((0, 0, 0))
    screen.blit(text_of_win, (wightlap / 2 - 100, heightlap / 2 - 20))
    z = [time // 1000, time % 1000 // 100]
    z[0] = int(z[0])
    z[1] = int(z[1])
    text_of_time = font.render('you time: ' + str(z[0]) + '.' + str(z[1]), 0, (0, 255, 25))
    screen.blit(text_of_time, (wightlap / 2 - 100, heightlap / 2 + 30))
    rtime = float(str(z[0]) + '.' + str(z[1]))
    if run_1:
        if float(str(z[0]) + '.' + str(z[1])) < float(rec1) or float(rec1) == 0:
            state_of_nomer[0] = str(str(z[0]) + '.' + str(z[1]))
            print(state_of_nomer[0])
            rec1 = str(str(z[0]) + '.' + str(z[1]))
    elif run_2:
        if float(str(z[0]) + '.' + str(z[1])) < float(rec2) or float(rec2) == 0:
            state_of_nomer[1] = str(str(z[0]) + '.' + str(z[1]))
            rec2 = str(str(z[0]) + '.' + str(z[1]))
    elif run_3:
        if float(str(z[0]) + '.' + str(z[1])) < float(rec3) or float(rec3) == 0:
            state_of_nomer[2] = str(z[0]) + '.' + str(z[1])
            rec3 = state_of_nomer[0] = str(str(z[0]) + '.' + str(z[1]))
    with open('statistic\\statistic.txt', mode='w', encoding="utf8") as zapis:
        for i in range(len(state_of_nomer)):
            zapis.write(state_of_nomer[i] + '\n')


def draw_lose():
    font = pygame.font.SysFont('calibri', 50)
    text_of_lose = font.render("You lose! :(", 0, (255, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(text_of_lose, (wightlap / 2 - 100, heightlap / 2 - 20))


def rander_time(screen, time):
    font = pygame.font.SysFont('arial', 50)
    z = [time // 1000, time % 1000 // 100]
    z[0] = int(z[0])
    z[1] = int(z[1])
    text_of_win = font.render('time: ' + str(z[0]) + '.' + str(z[1]), 0, (0, 255, 25))
    screen.blit(text_of_win, (wightlap / 2 + 250, heightlap / 2 - 230))


def draw():
    global x_of_bird, x_fon, x_of_bird2, x_of_yoj, x_of_oblako, count_of_animation, count_of_animation_of_object, count_of_animation_of_bird, count_of_animation_of_bird2, count_of_animation_of_yoj, count_of_animation_of_oblako, cactusy
    rander_time(screen, otime)

    count_of_animation_of_bird += 1
    if count_of_animation_of_bird + 1 >= 30:
        count_of_animation_of_bird = 0
    if are_bird == True:
        screen.blit(move_bird[count_of_animation_of_bird // 5], (x_of_bird, y_of_bird))
        count_of_animation_of_bird += 1
        x_of_bird = x_of_bird - SPEED - speed_of_bird

    count_of_animation_of_bird2 += 1
    if count_of_animation_of_bird2 + 1 >= 30:
        count_of_animation_of_bird2 = 0
    if are_bird2 == True:
        screen.blit(move_bird[count_of_animation_of_bird2 // 5], (x_of_bird2, y_of_bird2))
        count_of_animation_of_bird2 += 1
        x_of_bird2 = x_of_bird2 - SPEED - speed_of_bird2

    count_of_animation_of_yoj += 1
    if count_of_animation_of_yoj + 1 >= 30:
        count_of_animation_of_yoj = 0
    if are_yoj == True:
        screen.blit(move_joh[count_of_animation_of_yoj // 5], (x_of_yoj, y_of_yoj))
        count_of_animation_of_yoj += 1
        x_of_yoj = x_of_yoj - SPEED - speed_of_yoj

    count_of_animation_of_oblako += 1
    if count_of_animation_of_oblako + 1 >= 30:
        count_of_animation_of_oblako = 0
    if are_oblako == True:
        screen.blit(move_bird[count_of_animation_of_oblako // 5], (x_of_oblako, y_of_oblako))
        count_of_animation_of_oblako += 1
        x_of_oblako = x_of_oblako - SPEED - speed_of_oblako

    if x_object >= wightlap - wightobject - xrmin:
        count_of_animation = 0
        screen.blit(not_move_state_object, (x_object, y_object))
    else:
        screen.blit(move_right_image_object[count_of_animation_of_object // 5], (x_object, y_object))

    if count_of_animation + 1 >= 30:
        count_of_animation = 0
    if left:
        screen.blit(move_left_image[count_of_animation // 5], (x, y))
        count_of_animation += 1
    elif right:
        screen.blit(move_right_image[count_of_animation // 5], (x, y))
        count_of_animation += 1
    else:
        screen.blit(notmove_state, (x, y))

    for snaryad_one in snaryady:
        snaryad_one.draw_snar(screen)
    for cactus_one in cactusy:
        cactus_one.draw_cactus(screen)
    if are_win:
        draw_win(otime)
    if are_lose:
        draw_lose()
    pygame.display.update()


snaryady = []
cactusy = []

otime = 0

'''Создание меню'''
punkts = [(60, 40, u'Levels', (255, 255, 30), (0, 255, 25), 0),
          (60, 80, u'Records', (255, 255, 30), (0, 255, 25), 1),
          (60, 120, u'Exit', (255, 255, 30), (0, 255, 25), 2)]
game = Meny(punkts)
game.meny()

'''Подготовка к запуску игры'''
done = True
snaryady = []
cactusy = []
running = True
run = True
'''Игровой цикл'''
while run:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.meny()
            screen.fill((50, 50, 50))
            window.blit(screen, (0, 0))
            pygame.display.flip()
        while run_1:
            time = 0
            while running_1:
                clock.tick(30)
                time += 1000 / 30
                otime = time
                screen.blit(fon, (x_fon - 50, 0))
                screen.blit(fon, (x_fon + 850, 0))
                screen.blit(fon, (x_fon + 1750, 0))
                fps_of_bird += 1
                speed_of_bird = SPEED_of_bird

                if are_bird == False and fps_of_bird >= 600:
                    are_bird = True
                    x_of_bird = wightlap
                    speed_of_bird = random.randint(1, 5)
                    SPEED_of_bird = speed_of_bird
                if x_of_bird <= 0 - wight_bird:
                    are_bird = False
                    fps_of_bird = 0
                    x_of_bird = wightlap

                zadergka += 1
                fps_of_snar += 1
                if fps_of_snar >= min_of_smen_of_fps_of_snar and max_of_snaryad != MAX_of_snaryad:
                    max_of_snaryad = MAX_of_snaryad
                    fps_of_snar = 0
                zadergka_of_cactus += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running_1 = False
                        run_1 = False
                        run = False
                        running = False
                        time = 0
                for snaryad_one in snaryady:
                    if snaryad_one.x <= wightlap and snaryad_one.x >= 0:
                        snaryad_one.x += snaryad_one.speed_snar
                    else:
                        snaryady.pop(snaryady.index(snaryad_one))

                cactusy1 = cactusy[:]
                snaryady1 = snaryady[:]
                for cactus_one in cactusy1:
                    for snaryad_one in snaryady1:
                        if snaryad_one.x >= cactus_one.x_cactus and snaryad_one.x <= cactus_one.x_cactus + wight_cuctus and snaryad_one.y >= cactus_one.y_cactus:
                            snaryady.pop(snaryady.index(snaryad_one))
                            try:
                                cactusy.pop(cactusy.index(cactus_one))
                            except:
                                pass

                keys = pygame.key.get_pressed()

                if keys[pygame.K_ESCAPE]:
                    running_1 = False
                    run_1 = False
                    mus_of_1.stop()
                    mus_of_menu.play(-1)
                    otime = 0
                    know_of_moving = "right"
                    delta_x = 0
                    are_win = False
                    are_lose = False
                    couch_of_win = 1
                    x = 50
                    y = (heightlap - heighthero) - ydmin
                    x_object = 250
                    y_object = (heightlap - heightobject) - ydmin
                    left = False
                    right = False
                    count_of_animation = 0
                    count_of_animation_of_object = 0
                    snaryady = []
                    cactusy = []
                    max_of_snaryad = MAX_of_snaryad
                    fps_of_snar = 0
                    fps_of_bird = 0
                    are_bird = False
                    x_of_bird = wightlap
                    fps_of_bird2 = 150
                    are_bird2 = False
                    x_of_bird2 = wightlap
                    fps_of_yoj = 150
                    are_yoj = False
                    x_of_yoj = wightlap
                    fps_of_oblako = 125
                    are_oblako = False
                    x_of_oblako = wightlap
                    Meny(punkts).meny()
                if keys[pygame.K_w]:
                    if know_of_moving == "right":
                        know_of_facing = 1
                    else:
                        know_of_facing = -1

                    if max_of_snaryad == 0:
                        max_of_snaryad = 0 - (MAX_of_snaryad - 1)

                    if (len(snaryady) < max_of_snaryad + (MAX_of_snaryad - 1)) and (zadergka > zadergka_min):
                        snaryady.append(
                            snaryad(round(x + wighthero // 2), round(y + heighthero // 2), radius_of_snar,
                                    color_of_snar,
                                    know_of_facing, SPEED))
                        zadergka = 0
                        max_of_snaryad -= 1

                if keys[pygame.K_LEFT] and x > xlmin:
                    x -= speed
                    left = True
                    right = False
                    know_of_moving = "left"
                    speed_of_bird = SPEED_of_bird - speed
                    speed_of_bird2 = SPEED_of_bird2 - speed
                    speed_of_yoj = SPEED_of_yoj - speed
                    speed_of_oblako = SPEED_of_oblako - speed
                    x_fon += 3
                    if x_fon >= 900:
                        x_fon = 0

                elif keys[pygame.K_RIGHT] and x < ((wightlap - xrmin) - wighthero):
                    x += speed
                    left = False
                    right = True
                    know_of_moving = "right"
                    raschet_of_cactus()
                    speed_of_bird = SPEED_of_bird + speed
                    speed_of_bird2 = SPEED_of_bird2 + speed
                    speed_of_yoj = SPEED_of_yoj + speed
                    speed_of_oblako = SPEED_of_oblako + speed
                    x_fon -= 3
                    if x_fon <= -900:
                        x_fon = 0


                else:
                    left = False
                    right = False
                    count_of_animation = 0
                if not (hero_jump):

                    if keys[pygame.K_SPACE]:
                        hero_jump = True
                        mus_of_jump.play(0)
                else:
                    if couch_of_win == 0 or jump_hero_count == 10:
                        if jump_hero_count >= -10:
                            speed = dooble_speed
                            if jump_hero_count < 0:
                                y += (jump_hero_count ** 2) / 2
                            else:
                                y -= (jump_hero_count ** 2) / 2
                            jump_hero_count -= 1
                        else:
                            hero_jump = False
                            jump_hero_count = 10
                            speed = SPEED
                    else:
                        y = (heightlap - heighthero) - ydmin
                        couch_of_win = 0
                        jump_hero_count = 10

                if (x >= pos_x_of_stoped):
                    delta_x = x - pos_x_of_stoped
                    x_object -= delta_x
                    x = pos_x_of_stoped
                if x_object >= wightlap - wightobject - xrmin:
                    x_object = wightlap - wightobject - xrmin

                if count_of_animation_of_object + 1 >= 30:
                    count_of_animation_of_object = 0
                count_of_animation_of_object += 1
                x_object += speed - delta_speed

                are_win = False

                if x_object - x <= wighthero / 2 and x - x_object <= wighthero / 2 and y + heighthero >= x_object:
                    are_win = True
                    running_1 = False
                for cactus_one in cactusy:
                    if cactus_one.x_cactus - x <= wighthero / 2 and x - cactus_one.x_cactus <= wighthero / 2 and y + heighthero >= cactus_one.y_cactus:
                        are_lose = True
                        running_1 = False

                if hero_jump == True:
                    if x < x_of_bird and x + wighthero > x_of_bird and y + heighthero > y_of_bird and y <= y_of_bird + height_bird:
                        are_lose = True
                        running_1 = False

                    if x > x_of_bird and x + wighthero < x_of_bird and y + heighthero > y_of_bird and y <= y_of_bird + height_bird:
                        are_lose = True
                        running_1 = False

                    if x > x_of_bird and x + wighthero < x_of_bird and y + heighthero > y_of_bird and y <= y_of_bird:
                        are_lose = True
                        running_1 = False
                    if x > x_of_bird and x + wighthero > x_of_bird and y + heighthero < y_of_bird and y >= y_of_bird:
                        are_lose = True
                        running_1 = False

                if hero_jump == True:
                    if x < x_of_bird2 and x + wighthero > x_of_bird2 and y + heighthero > y_of_bird2 and y <= y_of_bird2 + height_bird:
                        are_lose = True
                        running_1 = False

                snaryady1 = snaryady[:]
                for snaryad_one in snaryady1:
                    if snaryad_one.x >= x_of_yoj and snaryad_one.x <= x_of_yoj + wight_yoj and snaryad_one.y >= y_of_yoj:
                        snaryady.pop(snaryady.index(snaryad_one))
                        fps_of_yoj = 150
                        are_yoj = False
                        x_of_yoj = wightlap

                draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_1 = False
                    run_1 = False
                    run = False
                    running = False
                    time = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run_1 = False
                        mus_of_1.stop()
                        mus_of_menu.play(-1)
                        otime = 0
                        running_1 = False
                        know_of_moving = "right"
                        delta_x = 0
                        are_win = False
                        are_lose = False
                        couch_of_win = 1
                        x = 50
                        y = (heightlap - heighthero) - ydmin
                        x_object = 250
                        y_object = (heightlap - heightobject) - ydmin
                        left = False
                        right = False
                        count_of_animation = 0
                        count_of_animation_of_object = 0
                        snaryady = []
                        cactusy = []
                        max_of_snaryad = MAX_of_snaryad
                        fps_of_snar = 0
                        fps_of_bird = 0
                        are_bird = False
                        x_of_bird = wightlap
                        fps_of_bird2 = 150
                        are_bird2 = False
                        x_of_bird2 = wightlap
                        fps_of_yoj = 150
                        are_yoj = False
                        x_of_yoj = wightlap
                        fps_of_oblako = 125
                        are_oblako = False
                        x_of_oblako = wightlap
                        Meny(punkts).meny()
                if event.type == pygame.MOUSEBUTTONUP:  # mus_of_1.stop()
                    # mus_of_1.play(-1)
                    otime = 0
                    running_1 = True
                    know_of_moving = "right"
                    delta_x = 0
                    are_win = False
                    are_lose = False
                    couch_of_win = 1
                    x = 50
                    y = (heightlap - heighthero) - ydmin
                    x_object = 250
                    y_object = (heightlap - heightobject) - ydmin
                    left = False
                    right = False
                    count_of_animation = 0
                    count_of_animation_of_object = 0
                    snaryady = []
                    cactusy = []
                    max_of_snaryad = MAX_of_snaryad
                    fps_of_snar = 0
                    fps_of_bird = 0
                    are_bird = False
                    x_of_bird = wightlap
                    fps_of_bird2 = 150
                    are_bird2 = False
                    x_of_bird2 = wightlap
                    fps_of_yoj = 150
                    are_yoj = False
                    x_of_yoj = wightlap
                    fps_of_oblako = 125
                    are_oblako = False
                    x_of_oblako = wightlap

        while run_2:
            time = 0
            while running_2:
                clock.tick(30)
                time += 1000 / 30
                otime = time
                screen.blit(fon, (x_fon - 50, 0))
                screen.blit(fon, (x_fon + 850, 0))
                screen.blit(fon, (x_fon + 1750, 0))
                fps_of_bird += 1
                speed_of_bird = SPEED_of_bird

                if are_bird == False and fps_of_bird >= 600:
                    are_bird = True
                    x_of_bird = wightlap
                    speed_of_bird = random.randint(1, 5)
                    SPEED_of_bird = speed_of_bird
                if x_of_bird <= 0 - wight_bird:
                    are_bird = False
                    fps_of_bird = 0
                    x_of_bird = wightlap
                fps_of_bird2 += 1
                speed_of_bird2 = SPEED_of_bird

                if are_bird2 == False and fps_of_bird2 >= 300:
                    are_bird2 = True
                    x_of_bird2 = wightlap
                    speed_of_bird2 = random.randint(1, 5)
                    SPEED_of_bird2 = speed_of_bird2
                if x_of_bird2 <= 0 - wight_bird:
                    are_bird2 = False
                    fps_of_bird2 = 0
                    x_of_bird2 = wightlap

                zadergka += 1
                fps_of_snar += 1
                if fps_of_snar >= min_of_smen_of_fps_of_snar and max_of_snaryad != MAX_of_snaryad:
                    max_of_snaryad = MAX_of_snaryad
                    fps_of_snar = 0
                zadergka_of_cactus += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running_2 = False
                        run_2 = False
                        run = False
                        running = False

                for snaryad_one in snaryady:
                    if snaryad_one.x <= wightlap and snaryad_one.x >= 0:
                        snaryad_one.x += snaryad_one.speed_snar
                    else:
                        snaryady.pop(snaryady.index(snaryad_one))

                cactusy1 = cactusy[:]
                snaryady1 = snaryady[:]
                for cactus_one in cactusy1:
                    for snaryad_one in snaryady1:
                        if snaryad_one.x >= cactus_one.x_cactus and snaryad_one.x <= cactus_one.x_cactus + wight_cuctus and snaryad_one.y >= cactus_one.y_cactus:
                            snaryady.pop(snaryady.index(snaryad_one))
                            try:
                                cactusy.pop(cactusy.index(cactus_one))
                            except:
                                pass

                keys = pygame.key.get_pressed()

                if keys[pygame.K_ESCAPE]:
                    running_2 = False
                    run_2 = False
                    mus_of_2.stop()
                    mus_of_menu.play(-1)
                    otime = 0
                    know_of_moving = "right"
                    delta_x = 0
                    are_win = False
                    are_lose = False
                    couch_of_win = 1
                    x = 50
                    y = (heightlap - heighthero) - ydmin
                    x_object = 250
                    y_object = (heightlap - heightobject) - ydmin
                    left = False
                    right = False
                    count_of_animation = 0
                    count_of_animation_of_object = 0
                    snaryady = []
                    cactusy = []
                    max_of_snaryad = MAX_of_snaryad
                    fps_of_snar = 0
                    fps_of_bird = 0
                    are_bird = False
                    x_of_bird = wightlap
                    fps_of_bird2 = 150
                    are_bird2 = False
                    x_of_bird2 = wightlap
                    fps_of_yoj = 150
                    are_yoj = False
                    x_of_yoj = wightlap
                    fps_of_oblako = 125
                    are_oblako = False
                    x_of_oblako = wightlap
                    Meny(punkts).meny()
                if keys[pygame.K_w]:
                    if know_of_moving == "right":
                        know_of_facing = 1
                    else:
                        know_of_facing = -1

                    if max_of_snaryad == 0:
                        max_of_snaryad = 0 - (MAX_of_snaryad - 1)

                    if (len(snaryady) < max_of_snaryad + (MAX_of_snaryad - 1)) and (zadergka > zadergka_min):
                        snaryady.append(
                            snaryad(round(x + wighthero // 2), round(y + heighthero // 2), radius_of_snar,
                                    color_of_snar,
                                    know_of_facing, SPEED))
                        zadergka = 0
                        max_of_snaryad -= 1

                if keys[pygame.K_LEFT] and x > xlmin:
                    x -= speed
                    left = True
                    right = False
                    know_of_moving = "left"
                    speed_of_bird = SPEED_of_bird - speed
                    speed_of_bird2 = SPEED_of_bird2 - speed
                    speed_of_yoj = SPEED_of_yoj - speed
                    speed_of_oblako = SPEED_of_oblako - speed
                    x_fon += 3
                    if x_fon >= 900:
                        x_fon = 0

                elif keys[pygame.K_RIGHT] and x < ((wightlap - xrmin) - wighthero):
                    x += speed
                    left = False
                    right = True
                    know_of_moving = "right"
                    raschet_of_cactus()
                    speed_of_bird = SPEED_of_bird + speed
                    speed_of_bird2 = SPEED_of_bird2 + speed
                    speed_of_yoj = SPEED_of_yoj + speed
                    speed_of_oblako = SPEED_of_oblako + speed
                    x_fon -= 3
                    if x_fon <= -900:
                        x_fon = 0


                else:
                    left = False
                    right = False
                    count_of_animation = 0
                if not (hero_jump):

                    if keys[pygame.K_SPACE]:
                        hero_jump = True
                        mus_of_jump.play(0)
                else:
                    if couch_of_win == 0 or jump_hero_count == 10:
                        if jump_hero_count >= -10:
                            speed = dooble_speed
                            if jump_hero_count < 0:
                                y += (jump_hero_count ** 2) / 2
                            else:
                                y -= (jump_hero_count ** 2) / 2
                            jump_hero_count -= 1
                        else:
                            hero_jump = False
                            jump_hero_count = 10
                            speed = SPEED
                    else:
                        y = (heightlap - heighthero) - ydmin
                        couch_of_win = 0
                        jump_hero_count = 10

                if (x >= pos_x_of_stoped):
                    delta_x = x - pos_x_of_stoped
                    x_object -= delta_x
                    x = pos_x_of_stoped
                if x_object >= wightlap - wightobject - xrmin:
                    x_object = wightlap - wightobject - xrmin

                if count_of_animation_of_object + 1 >= 30:
                    count_of_animation_of_object = 0
                count_of_animation_of_object += 1
                x_object += speed - delta_speed

                are_win = False

                if x_object - x <= wighthero / 2 and x - x_object <= wighthero / 2 and y + heighthero >= x_object:
                    are_win = True
                    running_2 = False
                for cactus_one in cactusy:
                    if cactus_one.x_cactus - x <= wighthero / 2 and x - cactus_one.x_cactus <= wighthero / 2 and y + heighthero >= cactus_one.y_cactus:
                        are_lose = True
                        running_2 = False

                if hero_jump == True:
                    if x < x_of_bird and x + wighthero > x_of_bird and y + heighthero > y_of_bird and y <= y_of_bird + height_bird:
                        are_lose = True
                        running_2 = False

                    if x > x_of_bird and x + wighthero < x_of_bird and y + heighthero > y_of_bird and y <= y_of_bird + height_bird:
                        are_lose = True
                        running_2 = False

                    if x > x_of_bird and x + wighthero < x_of_bird and y + heighthero > y_of_bird and y <= y_of_bird:
                        are_lose = True
                        running_2 = False
                    if x > x_of_bird and x + wighthero > x_of_bird and y + heighthero < y_of_bird and y >= y_of_bird:
                        are_lose = True
                        running_2 = False

                if hero_jump == True:
                    if x < x_of_bird2 and x + wighthero > x_of_bird2 and y + heighthero > y_of_bird2 and y <= y_of_bird2 + height_bird:
                        are_lose = True
                        running_2 = False

                    if x > x_of_bird2 and x + wighthero <= x_of_bird2 and y + heighthero >= y_of_bird2 and y <= y_of_bird2 + height_bird:
                        are_lose = True
                        running_2 = False

                    if x > x_of_bird2 and x + wighthero <= x_of_bird2 and y + heighthero >= y_of_bird2 and y <= y_of_bird2:
                        are_lose = True
                        running_2 = False
                    if x > x_of_bird2 and x + wighthero >= x_of_bird2 and y + heighthero <= y_of_bird2 and y >= y_of_bird2:
                        are_lose = True
                        running_2 = False

                if x <= x_of_yoj and x + wighthero >= x_of_yoj and y + heighthero >= y_of_yoj and y <= y_of_yoj + height_yoj:
                    are_lose = True
                    running_2 = False

                if x >= x_of_yoj and x + wighthero <= x_of_yoj and y + heighthero >= y_of_yoj and y <= y_of_yoj + height_yoj:
                    are_lose = True
                    running_2 = False

                if x >= x_of_yoj and x + wighthero <= x_of_yoj and y + heighthero >= y_of_yoj and y <= y_of_yoj:
                    are_lose = True
                    running_2 = False
                if x >= x_of_yoj and x + wighthero >= x_of_yoj and y + heighthero <= y_of_yoj and y >= y_of_yoj:
                    are_lose = True
                    running_2 = False

                if x <= x_of_oblako and x + wighthero >= x_of_oblako and y + heighthero >= y_of_oblako and y <= y_of_oblako + height_oblako:
                    are_lose = True
                    running_2 = False

                if x >= x_of_oblako and x + wighthero <= x_of_oblako and y + heighthero >= y_of_oblako and y <= y_of_oblako + height_oblako:
                    are_lose = True
                    running_2 = False

                if x >= x_of_oblako and x + wighthero <= x_of_oblako and y + heighthero >= y_of_oblako and y <= y_of_oblako:
                    are_lose = True
                    running_2 = False
                if x >= x_of_oblako and x + wighthero >= x_of_oblako and y + heighthero <= y_of_oblako and y >= y_of_oblako:
                    are_lose = True
                    running_2 = False

                snaryady1 = snaryady[:]
                for snaryad_one in snaryady1:
                    if snaryad_one.x >= x_of_yoj and snaryad_one.x <= x_of_yoj + wight_yoj and snaryad_one.y >= y_of_yoj:
                        snaryady.pop(snaryady.index(snaryad_one))
                        fps_of_yoj = 150
                        are_yoj = False
                        x_of_yoj = wightlap

                draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_2 = False
                    run_2 = False
                    run = False
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run_2 = False
                        mus_of_2.stop()
                        mus_of_menu.play(-1)
                        otime = 0
                        running_2 = False
                        know_of_moving = "right"
                        delta_x = 0
                        are_win = False
                        are_lose = False
                        couch_of_win = 1
                        x = 50
                        y = (heightlap - heighthero) - ydmin
                        x_object = 250
                        y_object = (heightlap - heightobject) - ydmin
                        left = False
                        right = False
                        count_of_animation = 0
                        count_of_animation_of_object = 0
                        snaryady = []
                        cactusy = []
                        max_of_snaryad = MAX_of_snaryad
                        fps_of_snar = 0
                        fps_of_bird = 0
                        are_bird = False
                        x_of_bird = wightlap
                        fps_of_bird2 = 150
                        are_bird2 = False
                        x_of_bird2 = wightlap
                        fps_of_yoj = 150
                        are_yoj = False
                        x_of_yoj = wightlap
                        fps_of_oblako = 125
                        are_oblako = False
                        x_of_oblako = wightlap
                        Meny(punkts).meny()
                if event.type == pygame.MOUSEBUTTONUP:
                    # mus_of_2.stop()
                    # mus_of_2.play(-1)
                    otime = 0
                    running_2 = True
                    know_of_moving = "right"
                    delta_x = 0
                    are_win = False
                    are_lose = False
                    couch_of_win = 1
                    x = 50
                    y = (heightlap - heighthero) - ydmin
                    x_object = 250
                    y_object = (heightlap - heightobject) - ydmin
                    left = False
                    right = False
                    count_of_animation = 0
                    count_of_animation_of_object = 0
                    snaryady = []
                    cactusy = []
                    max_of_snaryad = MAX_of_snaryad
                    fps_of_snar = 0
                    fps_of_bird = 0
                    are_bird = False
                    x_of_bird = wightlap
                    fps_of_bird2 = 150
                    are_bird2 = False
                    x_of_bird2 = wightlap
                    fps_of_yoj = 150
                    are_yoj = False
                    x_of_yoj = wightlap
                    fps_of_oblako = 125
                    are_oblako = False
                    x_of_oblako = wightlap

        while run_3:
            time = 0
            while running_3:
                clock.tick(30)
                time += 1000 / 30
                otime = time
                screen.blit(fon, (x_fon - 50, 0))
                screen.blit(fon, (x_fon + 850, 0))
                screen.blit(fon, (x_fon + 1750, 0))
                fps_of_bird += 1
                speed_of_bird = SPEED_of_bird

                if are_bird == False and fps_of_bird >= 600:
                    are_bird = True
                    x_of_bird = wightlap
                    speed_of_bird = random.randint(1, 5)
                    SPEED_of_bird = speed_of_bird
                if x_of_bird <= 0 - wight_bird:
                    are_bird = False
                    fps_of_bird = 0
                    x_of_bird = wightlap
                fps_of_bird2 += 1
                speed_of_bird2 = SPEED_of_bird

                if are_bird2 == False and fps_of_bird2 >= 300:
                    are_bird2 = True
                    x_of_bird2 = wightlap
                    speed_of_bird2 = random.randint(1, 5)
                    SPEED_of_bird2 = speed_of_bird2
                if x_of_bird2 <= 0 - wight_bird:
                    are_bird2 = False
                    fps_of_bird2 = 0
                    x_of_bird2 = wightlap

                fps_of_yoj += 1
                speed_of_yoj = SPEED_of_yoj

                if are_yoj == False and fps_of_yoj >= 300:
                    are_yoj = True
                    x_of_yoj = wightlap
                    speed_of_yoj = random.randint(1, 5)
                    SPEED_of_yoj = speed_of_yoj
                if x_of_yoj <= 0 - wight_yoj:
                    are_yoj = False
                    fps_of_yoj = 0
                    x_of_yoj = wightlap

                fps_of_oblako += 1
                speed_of_oblako = SPEED_of_oblako

                if are_oblako == False and fps_of_oblako >= 300:
                    are_oblako = True
                    x_of_oblako = wightlap
                    speed_of_oblako = random.randint(1, 5)
                    SPEED_of_oblako = speed_of_oblako
                if x_of_oblako <= 0 - wight_oblako:
                    are_oblako = False
                    fps_of_oblako = 0
                    x_of_oblako = wightlap

                zadergka += 1
                fps_of_snar += 1
                if fps_of_snar >= min_of_smen_of_fps_of_snar and max_of_snaryad != MAX_of_snaryad:
                    max_of_snaryad = MAX_of_snaryad
                    fps_of_snar = 0
                zadergka_of_cactus += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running_3 = False
                        run_3 = False
                        run = False
                        running = False

                for snaryad_one in snaryady:
                    if snaryad_one.x <= wightlap and snaryad_one.x >= 0:
                        snaryad_one.x += snaryad_one.speed_snar
                    else:
                        snaryady.pop(snaryady.index(snaryad_one))

                cactusy1 = cactusy[:]
                snaryady1 = snaryady[:]
                for cactus_one in cactusy1:
                    for snaryad_one in snaryady1:
                        if snaryad_one.x >= cactus_one.x_cactus and snaryad_one.x <= cactus_one.x_cactus + wight_cuctus and snaryad_one.y >= cactus_one.y_cactus:
                            snaryady.pop(snaryady.index(snaryad_one))
                            try:
                                cactusy.pop(cactusy.index(cactus_one))
                            except:
                                pass

                keys = pygame.key.get_pressed()

                if keys[pygame.K_ESCAPE]:
                    running_3 = False
                    run_3 = False
                    mus_of_3.stop()
                    mus_of_menu.play(-1)
                    otime = 0
                    know_of_moving = "right"
                    delta_x = 0
                    are_win = False
                    are_lose = False
                    couch_of_win = 1
                    x = 50
                    y = (heightlap - heighthero) - ydmin
                    x_object = 250
                    y_object = (heightlap - heightobject) - ydmin
                    left = False
                    right = False
                    count_of_animation = 0
                    count_of_animation_of_object = 0
                    snaryady = []
                    cactusy = []
                    max_of_snaryad = MAX_of_snaryad
                    fps_of_snar = 0
                    fps_of_bird = 0
                    are_bird = False
                    x_of_bird = wightlap
                    fps_of_bird2 = 150
                    are_bird2 = False
                    x_of_bird2 = wightlap
                    fps_of_yoj = 150
                    are_yoj = False
                    x_of_yoj = wightlap
                    fps_of_oblako = 125
                    are_oblako = False
                    x_of_oblako = wightlap
                    Meny(punkts).meny()
                if keys[pygame.K_w]:
                    if know_of_moving == "right":
                        know_of_facing = 1
                    else:
                        know_of_facing = -1

                    if max_of_snaryad == 0:
                        max_of_snaryad = 0 - (MAX_of_snaryad - 1)

                    if (len(snaryady) < max_of_snaryad + (MAX_of_snaryad - 1)) and (zadergka > zadergka_min):
                        snaryady.append(
                            snaryad(round(x + wighthero // 2), round(y + heighthero // 2), radius_of_snar,
                                    color_of_snar,
                                    know_of_facing, SPEED))
                        zadergka = 0
                        max_of_snaryad -= 1

                if keys[pygame.K_LEFT] and x > xlmin:
                    x -= speed
                    left = True
                    right = False
                    know_of_moving = "left"
                    speed_of_bird = SPEED_of_bird - speed
                    speed_of_bird2 = SPEED_of_bird2 - speed
                    speed_of_yoj = SPEED_of_yoj - speed
                    speed_of_oblako = SPEED_of_oblako - speed
                    x_fon += 3
                    if x_fon >= 900:
                        x_fon = 0

                elif keys[pygame.K_RIGHT] and x < ((wightlap - xrmin) - wighthero):
                    x += speed
                    left = False
                    right = True
                    know_of_moving = "right"
                    raschet_of_cactus()
                    speed_of_bird = SPEED_of_bird + speed
                    speed_of_bird2 = SPEED_of_bird2 + speed
                    speed_of_yoj = SPEED_of_yoj + speed
                    speed_of_oblako = SPEED_of_oblako + speed
                    x_fon -= 3
                    if x_fon <= -900:
                        x_fon = 0


                else:
                    left = False
                    right = False
                    count_of_animation = 0
                if not (hero_jump):

                    if keys[pygame.K_SPACE]:
                        hero_jump = True
                        mus_of_jump.play(0)
                else:
                    if couch_of_win == 0 or jump_hero_count == 10:
                        if jump_hero_count >= -10:
                            speed = dooble_speed
                            if jump_hero_count < 0:
                                y += (jump_hero_count ** 2) / 2
                            else:
                                y -= (jump_hero_count ** 2) / 2
                            jump_hero_count -= 1
                        else:
                            hero_jump = False
                            jump_hero_count = 10
                            speed = SPEED
                    else:
                        y = (heightlap - heighthero) - ydmin
                        couch_of_win = 0
                        jump_hero_count = 10

                if (x >= pos_x_of_stoped):
                    delta_x = x - pos_x_of_stoped
                    x_object -= delta_x
                    x = pos_x_of_stoped
                if x_object >= wightlap - wightobject - xrmin:
                    x_object = wightlap - wightobject - xrmin

                if count_of_animation_of_object + 1 >= 30:
                    count_of_animation_of_object = 0
                count_of_animation_of_object += 1
                x_object += speed - delta_speed

                are_win = False

                if x_object - x <= wighthero / 2 and x - x_object <= wighthero / 2 and y + heighthero >= x_object:
                    are_win = True
                    running_3 = False
                for cactus_one in cactusy:
                    if cactus_one.x_cactus - x <= wighthero / 2 and x - cactus_one.x_cactus <= wighthero / 2 and y + heighthero >= cactus_one.y_cactus:
                        are_lose = True
                        running_3 = False

                if hero_jump == True:
                    if x < x_of_bird and x + wighthero > x_of_bird and y + heighthero > y_of_bird and y <= y_of_bird + height_bird:
                        are_lose = True
                        running_3 = False

                    if x > x_of_bird and x + wighthero < x_of_bird and y + heighthero > y_of_bird and y <= y_of_bird + height_bird:
                        are_lose = True
                        running_3 = False

                    if x > x_of_bird and x + wighthero < x_of_bird and y + heighthero > y_of_bird and y <= y_of_bird:
                        are_lose = True
                        running_3 = False
                    if x > x_of_bird and x + wighthero > x_of_bird and y + heighthero < y_of_bird and y >= y_of_bird:
                        are_lose = True
                        running_3 = False

                if hero_jump == True:
                    if x < x_of_bird2 and x + wighthero > x_of_bird2 and y + heighthero > y_of_bird2 and y <= y_of_bird2 + height_bird:
                        are_lose = True
                        running_3 = False

                    if x > x_of_bird2 and x + wighthero <= x_of_bird2 and y + heighthero >= y_of_bird2 and y <= y_of_bird2 + height_bird:
                        are_lose = True
                        running_3 = False

                    if x > x_of_bird2 and x + wighthero <= x_of_bird2 and y + heighthero >= y_of_bird2 and y <= y_of_bird2:
                        are_lose = True
                        running_3 = False
                    if x > x_of_bird2 and x + wighthero >= x_of_bird2 and y + heighthero <= y_of_bird2 and y >= y_of_bird2:
                        are_lose = True
                        running_3 = False

                if x <= x_of_yoj and x + wighthero >= x_of_yoj and y + heighthero >= y_of_yoj and y <= y_of_yoj + height_yoj:
                    are_lose = True
                    running_3 = False

                if x >= x_of_yoj and x + wighthero <= x_of_yoj and y + heighthero >= y_of_yoj and y <= y_of_yoj + height_yoj:
                    are_lose = True
                    running_3 = False

                if x >= x_of_yoj and x + wighthero <= x_of_yoj and y + heighthero >= y_of_yoj and y <= y_of_yoj:
                    are_lose = True
                    running_3 = False
                if x >= x_of_yoj and x + wighthero >= x_of_yoj and y + heighthero <= y_of_yoj and y >= y_of_yoj:
                    are_lose = True
                    running_3 = False

                if x <= x_of_oblako and x + wighthero >= x_of_oblako and y + heighthero >= y_of_oblako and y <= y_of_oblako + height_oblako:
                    are_lose = True
                    running_3 = False

                if x >= x_of_oblako and x + wighthero <= x_of_oblako and y + heighthero >= y_of_oblako and y <= y_of_oblako + height_oblako:
                    are_lose = True
                    running_3 = False

                if x >= x_of_oblako and x + wighthero <= x_of_oblako and y + heighthero >= y_of_oblako and y <= y_of_oblako:
                    are_lose = True
                    running_3 = False
                if x >= x_of_oblako and x + wighthero >= x_of_oblako and y + heighthero <= y_of_oblako and y >= y_of_oblako:
                    are_lose = True
                    running_3 = False

                snaryady1 = snaryady[:]
                for snaryad_one in snaryady1:
                    if snaryad_one.x >= x_of_yoj and snaryad_one.x <= x_of_yoj + wight_yoj and snaryad_one.y >= y_of_yoj:
                        snaryady.pop(snaryady.index(snaryad_one))
                        fps_of_yoj = 150
                        are_yoj = False
                        x_of_yoj = wightlap

                draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_3 = False
                    run_3 = False
                    run = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run_3 = False
                        mus_of_3.stop()
                        mus_of_menu.play(-1)
                        otime = 0
                        running_3 = False
                        know_of_moving = "right"
                        delta_x = 0
                        are_win = False
                        are_lose = False
                        couch_of_win = 1
                        x = 50
                        y = (heightlap - heighthero) - ydmin
                        x_object = 250
                        y_object = (heightlap - heightobject) - ydmin
                        left = False
                        right = False
                        count_of_animation = 0
                        count_of_animation_of_object = 0
                        snaryady = []
                        cactusy = []
                        max_of_snaryad = MAX_of_snaryad
                        fps_of_snar = 0
                        fps_of_bird = 0
                        are_bird = False
                        x_of_bird = wightlap
                        fps_of_bird2 = 150
                        are_bird2 = False
                        x_of_bird2 = wightlap
                        fps_of_yoj = 150
                        are_yoj = False
                        x_of_yoj = wightlap
                        fps_of_oblako = 125
                        are_oblako = False
                        x_of_oblako = wightlap
                        Meny(punkts).meny()
                if event.type == pygame.MOUSEBUTTONUP:
                    # mus_of_3.stop()
                    # mus_of_3.play(-1)
                    otime = 0
                    running_3 = True
                    know_of_moving = "right"
                    delta_x = 0
                    are_win = False
                    are_lose = False
                    couch_of_win = 1
                    x = 50
                    y = (heightlap - heighthero) - ydmin
                    x_object = 250
                    y_object = (heightlap - heightobject) - ydmin
                    left = False
                    right = False
                    count_of_animation = 0
                    count_of_animation_of_object = 0
                    snaryady = []
                    cactusy = []
                    max_of_snaryad = MAX_of_snaryad
                    fps_of_snar = 0
                    fps_of_bird = 0
                    are_bird = False
                    x_of_bird = wightlap
                    fps_of_bird2 = 150
                    are_bird2 = False
                    x_of_bird2 = wightlap
                    fps_of_yoj = 150
                    are_yoj = False
                    x_of_yoj = wightlap
                    fps_of_oblako = 125
                    are_oblako = False
                    x_of_oblako = wightlap

pygame.quit()
