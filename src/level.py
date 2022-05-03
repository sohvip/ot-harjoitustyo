import sys
import pygame
from game_over import End
from objects import Background, Starie, Spike


class Play:
    '''Luokka, joka vastaa pelin peliosuudesta.'''

    def __init__(self):
        '''Luokan konstruktori. Alustaa pelinäkymän.'''
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
        '''Kutsuu jatkuvasti funktioita, jotka vastaavat näkymästä ja pelin toiminnallisuudesta.'''
        pygame.init()
        while True:
            self.clock.tick(200)
            self.get_events()
            self.draw()
            self.starie_action()
            self.collide()

    def get_events(self):
        '''Vastaanottaa käyttäjän syötteitä ja toimii niiden mukaan.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.starie_jump()

    def starie_jump(self):
        '''Mahdollistaa pelihahmon hypyn, kun se on maantasolla.'''
        if self.starie.s_y == 318:
            self.starie.jump = 1

    def draw(self):
        '''Kutsuu pelinäkymän piirtäviä funktioita.'''
        self.draw_bg()
        self.draw_starie()
        self.draw_spikes()
        self.draw_score()

        pygame.display.flip()

    def draw_bg(self):
        '''Piirtää pelin taustan näkymään.'''
        self.screen.blit(self.background.background,
                         (self.background.bg_x-640, 0))
        self.screen.blit(self.background.background, (self.background.bg_x, 0))
        self.screen.blit(self.background.background,
                         (self.background.bg_x+640, 0))
        self.background.bg_x -= 0.5
        if self.background.bg_x <= -640:
            self.background.bg_x = 0

    def draw_starie(self):
        '''Piirtää pelihahmon näkymään.'''
        self.starie_r = self.screen.blit(
            self.starie.starie, (40, self.starie.s_y))

    def draw_score(self):
        '''Piirtää pelaajan senhetkisen pistemäärän näkymään.'''
        font = pygame.font.SysFont('suruma', 20)
        color = (255, 255, 255)
        text = font.render(f'score: {str(self.score)}', False, color)
        self.screen.blit(text, (550, 10))

    def starie_action(self):
        '''Vastaa siitä, miten pelihahmo hyppy etenee.'''
        if self.starie.s_y < 318:
            self.starie.s_y += self.starie.fall
        if self.starie.jump == 1:
            self.starie.s_y -= 5
            self.starie.jumping += 1
            if self.starie.jumping > 40:
                self.starie.jumping = 0
                self.starie.jump = 0

    def draw_spikes(self):
        '''Piirtää estepiikit näkymään'''
        self.spike_r = self.screen.blit(
            self.spike.spike, (self.spike.sp_x, 361))
        self.spike.sp_x -= self.spike.speed
        if self.spike.sp_x < -50:
            self.spike.sp_x = 650
            self.score += 1
            self.speed()

    def collide(self):
        '''Tarkistaa törmääkö pelihahmo estepiikkiin.
        Jos näin käy, nykyinen näkymä suljetaan ja game over -näkymä aukeaa.'''
        if self.starie_r.colliderect(self.spike_r):
            end = End(self.score)
            end.end_screen()
            pygame.display.quit()

    def speed(self):
        '''Säätelee pelihahmon vauhtia pistemäärän mukaan.'''
        if self.score != 0 and self.score % 5 == 0:
            self.spike.speed += 0.1
