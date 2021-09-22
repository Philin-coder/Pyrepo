# импорт плагина pygame
import pygame

pygame.init()
# установка размеров окна
win = pygame.display.set_mode((500, 500))
# изменение названия окна
pygame.display.set_caption('Cubes Game')
# установка позиций игрока по x и y
x = 50
y = 50
# установка ширины
width = 40
# установка высоты
height = 60
# установка скорости передвижения
speed = 5
#
run = True
# создание цикла для остановки игры
while run:
    # установка времени через которое будет перезапускаться цикл
    pygame.time.delay(100)

    # установка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # передвижение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    # создание персонажа
    # цвет
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    # чтобы заработало обьязательно прописываем модуль update
    pygame.display.update()

pygame.quit()
