import os
import sys
import pygame

play_list = list()
f_ext = 'mp3'
for i in os.listdir(os.getcwd()):
    if i.endswith(f_ext):
        play_list.append(i)
        print(f'список песен равен')
        # print(play_list)
        # for i in range(len(play_list)):
        #     pygame.init()
        #     wnd = pygame.display.set_mode((640, 640))
        #     pygame.mixer.music.load(play_list[i])
        #     pygame.mixer.music.play(-1, 0.0)
        #     mc_ = pygame.draw.circle(wnd, (50, 30, 90), (90, 30), 16, 5)
        #     wnd.blit(wnd, mc)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # pygame.display.update()
