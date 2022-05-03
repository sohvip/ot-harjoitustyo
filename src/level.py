import sys
import pygame
from game_over import End
from objects import Background, Starie, Spike


class Play:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Starkour')

        self.background = Background()
        self.starie = Starie()
        self.spike = Spike()
        self.clock = pygame.time.Clock()
        self.score = 0
        self.starie_r = 0
        self.spike_r = 0

    def gameloop(self):
        pygame.init()
        while True:
            self.clock.tick(200)
            self.get_events()
            self.draw()
            self.starie_action()
            self.collide()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.starie_jump()

    def starie_jump(self):
        if self.starie.s_y == 318:
            self.starie.jump = 1

    def draw(self):
        self.draw_bg()
        self.draw_starie()
        self.draw_spikes()
        self.draw_score()

        pygame.display.flip()

    def draw_bg(self):
        self.screen.blit(self.background.background,
                         (self.background.bg_x-640, 0))
        self.screen.blit(self.background.background, (self.background.bg_x, 0))
        self.screen.blit(self.background.background,
                         (self.background.bg_x+640, 0))
        self.background.bg_x -= 0.5
        if self.background.bg_x <= -640:
            self.background.bg_x = 0

    def draw_starie(self):
        self.starie_r = self.screen.blit(
            self.starie.starie, (40, self.starie.s_y))

    def draw_score(self):
        font = pygame.font.SysFont('suruma', 20)
        color = (255, 255, 255)
        text = font.render(f'score: {str(self.score)}', False, color)
        self.screen.blit(text, (550, 10))

    def starie_action(self):
        if self.starie.s_y < 318:
            self.starie.s_y += self.starie.fall
        if self.starie.jump == 1:
            self.starie.s_y -= 5
            self.starie.jumping += 1
            if self.starie.jumping > 40:
                self.starie.jumping = 0
                self.starie.jump = 0

    def draw_spikes(self):
        self.spike_r = self.screen.blit(
            self.spike.spike, (self.spike.sp_x, 361))
        self.spike.sp_x -= self.spike.speed
        if self.spike.sp_x < -50:
            self.spike.sp_x = 650
            self.score += 1
            self.speed()

    def collide(self):
        if self.starie_r.colliderect(self.spike_r):
            end = End(self.score)
            end.end_screen()
            pygame.display.quit()

    def speed(self):
        if self.score != 0 and self.score % 5 == 0:
            self.spike.speed += 0.1
