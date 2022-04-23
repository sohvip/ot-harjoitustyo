import sys
import pygame
from level import Play, Starie
from assets_route import PLAY_FILE_PATH


class Start:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((125, 60, 152))
        self.button = pygame.image.load(PLAY_FILE_PATH)
        self.button = pygame.transform.rotozoom(self.button, 0, 0.15)
        self.x = 320-(self.button.get_width()/2)
        self.y = 240-(self.button.get_height()/2)
        self.starie = Starie()

    def start(self):
        pygame.init()
        pygame.display.set_caption('Starkour')
        while True:
            self.draw_screen()
            self.get_events()

    def draw_screen(self):
        self.screen.blit(self.button, (self.x, self.y))
        self.screen.blit(self.starie.starie, (170, 60))
        self.title()
        pygame.display.update()

    def title(self):
        font = pygame.font.SysFont('suruma', 90, True)
        color = (250, 253, 15)
        text = font.render('ST', False, color)
        text_2 = font.render('RKOUR', False, color)
        self.screen.blit(text, (60, 80))
        self.screen.blit(text_2, (270, 80))

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] in range(int(self.x), int(self.x+self.button.get_width())) and
                        event.pos[1] in range(int(self.y), int(self.y+self.button.get_height()))):
                    play = Play()
                    play.gameloop()
                    pygame.display.quit()
