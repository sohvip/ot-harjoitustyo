import pygame

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Starkour')

def level():

    bg = pygame.image.load('assets/background.png')
    bg_x = 0

    starie = pygame.image.load('assets/starie.png')
    starie = pygame.transform.rotozoom(starie,0,0.6)  
    starie_y = 318
    jump = 0
    fall = 1
    jumping = 0

    spike = pygame.image.load('assets/spike.png')
    spike = pygame.transform.rotozoom(spike,0,0.7)
    spike_x = 700
    spike_speed = 1.3

    spike_2 = pygame.image.load('assets/spike.png')
    spike_2 = pygame.transform.rotozoom(spike_2,0,0.7)
    spike_x2 = 1300

    goal = pygame.image.load('assets/goal.png')
    goal = pygame.transform.rotozoom(goal,0,1.1)
    goal_x = 1700

    while True:
        screen.blit(bg,(bg_x-640,0))
        screen.blit(bg,(bg_x,0))
        screen.blit(bg,(bg_x+640,0))
        bg_x -= 0.5
        if bg_x <= -640:
            bg_x = 0

        screen.blit(starie,(40,starie_y))
        if starie_y < 318:
            starie_y += fall
        if jump == 1:
            starie_y -= 4
            jumping += 1
            if jumping > 40:
                jumping = 0
                jump = 0

        screen.blit(spike,(spike_x,351))
        spike_x -= spike_speed

        spike_rect2 = screen.blit(spike_2,(spike_x2,351))
        spike_x2 -= spike_speed

        screen.blit(goal,(goal_x,270))
        goal_x -= spike_speed
        if goal_x < -25:
            pygame.display.quit()
            exit()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if starie_y == 318:
                        jump = 1

if __name__=="__main__":
    level()