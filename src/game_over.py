import sys
import pygame


class End():
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((15, 15, 15))

    def end_screen(self):
        pygame.init()
        pygame.display.set_caption('Starkour')
        while True:
            self.draw_screen()
            self.get_events()

    def draw_screen(self):
        # pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(260,220,60,60))
        # pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(340,220,60,60))
        self.title()
        # self.final_score()
        pygame.display.update()

    def title(self):
        font = pygame.font.SysFont('suruma', 60, True)
        color = (250, 253, 15)
        text = font.render('GAME OVER', False, color)
        self.screen.blit(text, (130, 80))

    # def final_score(self):
        # font=pygame.font.SysFont('suruma',30)
        # color=(250,253,15)
        #text=font.render(f'final score: {str(self.play.score)}',False,color)
        # self.screen.blit(text,(240,220))

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            # if event.type==pygame.MOUSEBUTTONDOWN:
                # if event.pos[0] in range(340,400) and event.pos[1] in range(220,280):
                # pygame.display.quit()
                # sys.exit()
