import os
import  pygame
fext = 'mp3'
for i in os.listdir(os.getcwd()):
    if i.endswith(fext):
        playlist.append(i)
        print('список песен равен')
        print(playlist)
        for i in range(len(playlist)):
            pygame.init()
            wnd = pygame.display.set_mode((640, 640))
            pygame.mixer.music.load(playlist[i])
            pygame.mixer.music.play(-1, 0.0)
            circule = pygame.draw.circle(wnd, (50, 30, 90), (90, 30), 16, 5)
            wnd.blit(wnd, circule)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
