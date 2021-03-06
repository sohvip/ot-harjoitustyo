import pygame
from assets_route import BG_FILE_PATH, STARIE_FILE_PATH, SPIKE_FILE_PATH, SIGN_OUT_FILE_PATH


class Background:
    '''Luokka, joka määrittelee pelin taustakuvan.'''

    def __init__(self):
        '''Luokan konstruktori. Lataa kuvan ja antaa sille x-koordinaatin.'''
        self.background = pygame.image.load(BG_FILE_PATH)
        self.bg_x = 0


class Starie:
    '''Luokka, joka määrittelee pelihahmon.'''

    def __init__(self):
        '''Luokan konstruktori.
        Lataa kuvan ja muuttaa sen kokoa, sekä antaa tarvittavia muuttuja-arvoja.'''
        self.starie = pygame.image.load(STARIE_FILE_PATH)
        self.starie = pygame.transform.rotozoom(self.starie, 0, 0.6)
        self.s_y = 318
        self.jump = 0
        self.fall = 1
        self.jumping = 0


class Spike:
    '''Luokka, joka määrittelee pelin esteet.'''

    def __init__(self):
        '''Luokan konstruktori.
        Lataa kuvan ja muuttaa sen kokoa, sekä antaa tarvittavia muuttuja-arvoja.'''
        self.spike = pygame.image.load(SPIKE_FILE_PATH)
        self.spike = pygame.transform.rotozoom(self.spike, 0, 0.6)
        self.sp_x = 700
        self.speed = 1.5


class SignOut:
    '''Luokka, joka määrittelee uloskirjautumisnapin.'''

    def __init__(self):
        '''Luokan konstruktori.
        Lataa kuvan ja muuttaa sen kokoa, sekä tallentaa kuvan leveyden muuttujaan.'''
        self.sign_out = pygame.image.load(SIGN_OUT_FILE_PATH)
        self.sign_out = pygame.transform.rotozoom(self.sign_out, 0, 0.11)
        self.size = self.sign_out.get_width()
