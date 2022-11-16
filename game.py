from random import randint
import pygame
from pygame.draw import *

# background_image = pygame.image.load('C:\Users\Ilia\PycharmProjects\infa_filatov1\infa_2022_filatov/forest.jpg')
#
# while True:
#     screen.blit(background_image, (0, 0))
#     pygame.display.update()
#     clock.tick(60)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLOR = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
points = 0

def distruction(act_lst , mouse_click , mouse_coord) :
    '''
    Решает , пора ли очередному актеру покинуть пьесу
    :param act_lst: список актеров
    :param mouse_click: состояние мыши
    :param mouse_coord:  координаты клика
    :return: базу данных только с нужными актерами
    '''
    for i in range(len(act_lst)-1, -1, -1):
        distance = (act_lst[i].coord[0] - mouse_coord[0])**2 + (act_lst[i].coord[1] - mouse_coord[1])**2

        if distance <= act_lst[i].rds ** 2:
            global points
            points += act_lst[i].points
            del act_lst[i]

    return act_lst

class Ball :
    def __init__(self, scr):
        '''
        Создает обьект класса Ball, создает шарик
        :param scr: экоран на котором будет играть актер шарик
        '''
        self.color =  (randint(0,255), randint(0,255), randint(0,255))
        self.screen = screen
        self.points = 1
        self.rds = randint(20, 100)
        self.coord = [randint(100, 1200), randint(100, 700)]
        self.x_speed = randint(2, 7)
        self.y_speed = randint(2, 7)
        self.life_time = 0
    def draw(self):
        '''
        Просто рисует обьект
        :return: -
        '''
        circle(self.screen, self.color, self.coord,self.rds)

    def move(self, tic):
        '''
        Рассчитывает новые координаты обьекта , учитывая соударения, для определенного тика
        :param tic: текущий номер тика
        :return: -
        '''
        self.coord[0] += self.x_speed
        self.coord[1] += self.y_speed

        self.life_time += 1
        if tic % (2 * fps) == 0:
            self.x_speed = randint(2, 7) * randint(0, 1)
            self.y_speed = randint(2, 7) * randint(0, 1)
        if self.coord[0] <= self.rds:
            self.x_speed = -self.x_speed * randint(0, 1)
            self.y_speed = -self.y_speed * randint(0, 1)
        if self.coord[1] >= 800 - self.rds:
            self.x_speed = -self.x_speed * randint(0, 1)
            self.y_speed = -self.y_speed * randint(0, 1)
        if self.coord[1] <= self.rds:
            self.x_speed = -self.x_speed * randint(0, 1)
            self.y_speed = -self.y_speed * randint(0, 1)
        if self.coord[0] >= 1500 - self.rds:
            self.x_speed = -self.x_speed * randint(0, 1)
        if self.x_speed == 0:
            if self.coord[0] <= self.rds:
                self.x_speed = 2
            else:
                self.x_speed = -2
        elif self.y_speed == 0:
            if self.coord[1] <= self.rds:
                self.y_speed = 2
            else:
                self.y_speed = -2
        elif self.life_time == 500:
            global act_lst

            del act_lst[i]
class Cross :
    def __init__(self,scr):
        '''
        Создает обьект класса Cross , создает крест
        :param scr:  экран на которой он создается 
        '''
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.screen = screen
        self.points = 5
        self.rds = randint(20, 100)
        self.coord = [randint(300, 1200), randint(300, 700)]
        self.x_speed = randint(-1, 7)
        self.y_speed = randint(-1, 7)
        self.rds = 30
        self.life_time = 0
    def move(self, tic):
        '''
        Рассчитывает новые координаты обьекта , учитывая соударения, для определенного тика
        :param tic: текущий номер тика
        :return: -
        '''
        self.coord[0] += self.x_speed
        self.coord[1] += self.y_speed

        self.life_time += 1
        if tic % (2 * fps) == 0:
            self.x_speed = randint(2, 7) * randint(0,1)
            self.y_speed = randint(2, 7) * randint(0,1)
        if self.coord[0] <= self.rds:
            self.x_speed = -self.x_speed * randint(0,1)
            self.y_speed = -self.y_speed * randint(0,1)
        if self.coord[1] >= 800 - self.rds:
            self.x_speed = -self.x_speed * randint(0,1)
            self.y_speed = -self.y_speed * randint(0,1)
        if self.coord[1] <= self.rds:
            self.x_speed = -self.x_speed * randint(0,1)
            self.y_speed = -self.y_speed * randint(0,1)
        if self.coord[0] >= 1500 - self.rds:
            self.x_speed = -self.x_speed * randint(0,1)
        if self.x_speed == 0 :
            if self.coord[0] <= self.rds :
                self.x_speed = 2
            else :
                self.x_speed = -2
        elif self.y_speed == 0 :
            if self.coord[1] <= self.rds :
                self.y_speed = 2
            else :
                self.y_speed = -2
        elif self.life_time == 500:
            global act_lst

            del act_lst[i]
    def draw(self):
        '''
        Просто рисует обьект
        :return: -
        '''
        rct1 = [self.coord[0] - 5 , self.coord[1] - 30, 10 , 60]
        rct2 = [self.coord[0] - 30 , self.coord[1] - 5, 60, 10]
        rect(self.screen, self.color, rct1)
        rect(self.screen, self.color, rct2)
pygame.init()
pygame.font.init()
fps = 60
screen = pygame.display.set_mode([1500,800])
pygame.display.update()

finished = False
clock = pygame.time.Clock()
act_lst = []
tick = 0
points = 0
while not finished:
    clock.tick(fps)
    '''
    начало логического блока , проверяем все события 
    '''
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 27:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN :
            mouse_click = event.button
            mouse_coord = list(event.pos)
            act_lst = distruction(act_lst, mouse_click, mouse_coord)
    '''
    Создает новые шарики
    '''
    if tick % (1 * fps) == 0:
        act_lst.append(Ball(screen))
    '''
    Создает новые крестики
    '''
    if tick % (2 * fps) == 0:
        act_lst.append(Cross(screen))

    screen.fill((0,0,0))

    '''
    Теперь в цикле будем заускать методы для создания и передвижения обьектов
    '''
    for i in range(len(act_lst) - 1, -1, -1):
        act_lst[i].move(tick)
        act_lst[i].draw()
    '''
       Отвечает за показ количества очков на экране
       '''
    font = pygame.font.Font(None, 40)
    text = font.render("POINTS:" + str(points), True, (200, 0, 100))
    place = text.get_rect(center=(150, 100))
    screen.blit(text, place)
    pygame.display.update()
    tick += 1