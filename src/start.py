import sys
import pygame
from level import Play
from objects import Starie, SignOut
from assets_route import PLAY_FILE_PATH


class Start:
    '''Luokka, joka vastaa pelin aloitusnäkymästä.'''

    def __init__(self, user):
        '''Luokan konstruktori, joka alustaa näkymän.'''
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((125, 60, 152))
        self.button = pygame.image.load(PLAY_FILE_PATH)
        self.button = pygame.transform.rotozoom(self.button, 0, 0.15)
        self.button_x = 320-(self.button.get_width()/2)
        self.button_y = 240-(self.button.get_height()/2)
        self.starie = Starie()
        self.user = user

    def start(self):
        '''Kutsuu jatkuvasti funktioita, jotka vastaavat näkymästä ja tapahtumista.'''
        pygame.init()
        pygame.display.set_caption('Starkour')
        while True:
            self.draw_screen()
            self.get_events()

    def draw_screen(self):
        '''Piirtää näkymään ja kutsuu funktiota, joka myös piirtää näkymään.'''
        self.screen.blit(self.button, (self.button_x, self.button_y))
        self.screen.blit(self.starie.starie, (170, 60))
        self.title()
        self.sign_out()
        pygame.display.update()

    def title(self):
        '''Muodostaa ja piirtää näkymän otsikkotekstin.'''
        font = pygame.font.SysFont('suruma', 90, True)
        color = (250, 253, 15)
        text = font.render('ST', False, color)
        text_2 = font.render('RKOUR', False, color)
        self.screen.blit(text, (60, 80))
        self.screen.blit(text_2, (270, 80))

    def sign_out(self):
        '''Piirtää uloskirjautumisnapin näkymään.'''
        sign_out = SignOut()
        self.screen.blit(sign_out.sign_out, (580, 420))

    def get_events(self):  # pylint: disable=R0801
        '''Vastaanottaa käyttäjän syötteitä ja toimii niiden mukaan.
        Siirtää pelinäkymään, jos nappia painetaan.'''
        for event in pygame.event.get():  # pylint: disable=R0801
            if event.type == pygame.QUIT:  # pylint: disable=R0801
                pygame.display.quit()  # pylint: disable=R0801
                sys.exit()  # pylint: disable=R0801
            if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=R0801
                if (event.pos[0] in
                    range(int(self.button_x), int(self.button_x+self.button.get_width())) and
                    event.pos[1] in
                        range(int(self.button_y), int(self.button_y+self.button.get_height()))):
                    play = Play(self.user)
                    play.gameloop()
                    pygame.display.quit()
                elif (event.pos[0] in range(580, 637) and
                        event.pos[1] in range(420, 477)):
                    import index
                    pygame.display.quit()
                    index.main()
