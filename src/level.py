import sys
import pygame
from assets_route import BG_FILE_PATH, STARIE_FILE_PATH, SPIKE_FILE_PATH
from game_over import End


class Background():
    def __init__(self):
        self.background = pygame.image.load(BG_FILE_PATH)
        self.x = 0


class Starie():
    def __init__(self):
        self.starie = pygame.image.load(STARIE_FILE_PATH)
        self.starie = pygame.transform.rotozoom(self.starie, 0, 0.6)
        self.y = 318
        self.jump = 0
        self.fall = 1
        self.jumping = 0


class Spike():
    def __init__(self):
        self.spike = pygame.image.load(SPIKE_FILE_PATH)
        self.spike = pygame.transform.rotozoom(self.spike, 0, 0.6)
        self.x = 700
        self.speed = 1.5


class Play():
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Starkour')

        self.background = Background()
        self.starie = Starie()
        self.spike = Spike()
        self.clock = pygame.time.Clock()
        self.fps = 200
        self.score = 0

    def gameloop(self):
        pygame.init()
        while True:
            self.clock.tick(self.fps)
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
        if self.starie.y == 318:
            self.starie.jump = 1

    def draw(self):
        self.draw_bg()
        self.draw_starie()
        self.draw_spikes()
        self.draw_score()

        pygame.display.flip()

    def draw_bg(self):
        self.screen.blit(self.background.background,
                         (self.background.x-640, 0))
        self.screen.blit(self.background.background, (self.background.x, 0))
        self.screen.blit(self.background.background,
                         (self.background.x+640, 0))
        self.background.x -= 0.5
        if self.background.x <= -640:
            self.background.x = 0

    def draw_starie(self):
        self.starie_r = self.screen.blit(
            self.starie.starie, (40, self.starie.y))

    def draw_score(self):
        font = pygame.font.SysFont('suruma', 20)
        color = (255, 255, 255)
        text = font.render(f'score: {str(self.score)}', False, color)
        self.screen.blit(text, (550, 10))

    def starie_action(self):
        if self.starie.y < 318:
            self.starie.y += self.starie.fall
        if self.starie.jump == 1:
            self.starie.y -= 5
            self.starie.jumping += 1
            if self.starie.jumping > 40:
                self.starie.jumping = 0
                self.starie.jump = 0

    def draw_spikes(self):
        self.spike_r = self.screen.blit(self.spike.spike, (self.spike.x, 361))
        self.spike.x -= self.spike.speed
        if self.spike.x < -50:
            self.spike.x = 650
            self.score += 1
            self.speed()

    def collide(self):
        if self.starie_r.colliderect(self.spike_r):
            end = End()
            end.end_screen()

    def speed(self):
        if self.score != 0 and self.score % 5 == 0:
            self.spike.speed += 0.1
