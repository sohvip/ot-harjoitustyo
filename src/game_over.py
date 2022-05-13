import sys
import pygame
from assets_route import RESTART_FILE_PATH, HOME_FILE_PATH
from accounts import Account
from objects import SignOut


class End:
    '''Luokka, joka vastaa game over -näkymästä.'''

    def __init__(self, score, user):
        '''Luokan konstruktori, joka alustaa näkymän.

        Args:
            score: Pelaajan pistemäärä pelin loppuessa.
        '''
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((15, 15, 15))
        self.score = score
        self.restart = pygame.image.load(RESTART_FILE_PATH)
        self.restart = pygame.transform.rotozoom(self.restart, 0, 0.15)
        self.home = pygame.image.load(HOME_FILE_PATH)
        self.home = pygame.transform.rotozoom(self.home, 0, 0.15)
        self.width = self.restart.get_width()
        self.user = user
        self.sign_out = SignOut()

    def end_screen(self):
        '''Kutsuu jatkuvasti funktioita, jotka vastaavat näkymästä ja tapahtumista.'''
        pygame.init()
        pygame.display.set_caption('Starkour')
        while True:
            self.draw_endscreen()
            self.get_events()

    def draw_endscreen(self):
        '''Piirtää näkymän.'''
        self.title()
        self.final_score()
        self.draw_buttons()
        self.highscore()
        pygame.display.update()

    def draw_buttons(self):
        '''Piirtää napit.'''
        self.screen.blit(self.restart, (310-self.width, 260))
        self.screen.blit(self.home, (330, 260))
        self.screen.blit(self.sign_out.sign_out, (292, 302+self.width))

    def title(self):
        '''Määrittelee ja piirtää tekstin näkymään.'''
        font = pygame.font.SysFont('suruma', 60, True)
        color = (250, 253, 15)
        text = font.render('GAME OVER', False, color)
        self.screen.blit(text, (130, 80))

    def final_score(self):
        '''Määrittelee ja piirtää pelaajan lopullisen pistemäärän näkymään.'''
        font = pygame.font.SysFont('suruma', 30)
        color = (250, 253, 15)
        sentence = f'final score: {str(self.score)}'
        text = font.render(sentence, False, color)
        self.screen.blit(text, (240, 160))

    def highscore(self):
        '''Määrittelee ja piirtää pelaajan ennätyspisteet näkymään.'''
        account = Account()
        highscore = account.check_highscore(self.score, self.user)
        font = pygame.font.SysFont('suruma', 30)
        color = (250, 253, 15)
        sentence = f'highscore: {str(highscore)}'
        text = font.render(sentence, False, color)
        self.screen.blit(text, (240, 200))

    def get_events(self):  # pylint: disable=R0801 # pragma: no cover
        '''Vastaanottaa käyttäjän syötteitä ja toimii niiden mukaan.
        Siirtää näkymästä toiseen, jos nappia painetaan.'''
        for event in pygame.event.get():  # pylint: disable=R0801
            if event.type == pygame.QUIT:  # pylint: disable=R0801
                pygame.display.quit()  # pylint: disable=R0801
                sys.exit()  # pylint: disable=R0801
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] in range(310-self.width, 310) and
                        event.pos[1] in range(260, 260+self.width)):
                    from level import Play
                    play = Play(self.user)
                    play.gameloop()
                    pygame.display.quit()
                elif (event.pos[0] in range(330, 330+self.width) and
                        event.pos[1] in range(260, 260+self.width)):
                    from start import Start
                    start = Start(self.user)
                    start.start()
                    pygame.display.quit()
                elif (event.pos[0] in range(292, 292+self.sign_out.size) and
                        event.pos[1] in range(302+self.width, 302+self.width+self.sign_out.size)):
                    import index
                    pygame.display.quit()
                    index.main()
