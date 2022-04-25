import sys
import pygame
from assets_route import RESTART_FILE_PATH, HOME_FILE_PATH


class End:
    def __init__(self, score):
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((15, 15, 15))
        self.score = score
        self.restart = pygame.image.load(RESTART_FILE_PATH)
        self.restart = pygame.transform.rotozoom(self.restart, 0, 0.15)
        self.home = pygame.image.load(HOME_FILE_PATH)
        self.home = pygame.transform.rotozoom(self.home, 0, 0.15)
        self.width = self.restart.get_width()

    def end_screen(self):
        pygame.init()
        pygame.display.set_caption('Starkour')
        while True:
            self.draw_screen()
            self.get_events()

    def draw_screen(self):
        self.title()
        self.final_score()
        self.draw_buttons()
        pygame.display.update()

    def draw_buttons(self):
        self.screen.blit(self.restart, (310-self.width, 260))
        self.screen.blit(self.home, (330, 260))

    def title(self):
        font = pygame.font.SysFont('suruma', 60, True)
        color = (250, 253, 15)
        text = font.render('GAME OVER', False, color)
        self.screen.blit(text, (130, 80))

    def final_score(self):
        font = pygame.font.SysFont('suruma', 30)
        color = (250, 253, 15)
        sentence = f'final score: {str(self.score)}'
        text = font.render(sentence, False, color)
        self.screen.blit(text, (240, 180))

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] in range(310-self.width, 310) and
                event.pos[1] in range(260, 260+self.width)):
                    from level import Play
                    play = Play()
                    play.gameloop()
                    pygame.display.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] in range(330, 330+self.width) and
                event.pos[1] in range(260, 260+self.width)):
                    from start import Start
                    start = Start()
                    start.start()
                    pygame.display.quit()
