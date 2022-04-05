import pygame

class Bg():
    def __init__(self):
        self.bg=pygame.image.load('assets/background.png')
        self.x=0

class Starie():
    def __init__(self):
        self.starie=pygame.image.load('assets/starie.png')
        self.starie=pygame.transform.rotozoom(self.starie,0,0.6)
        self.y=318
        self.jump=0
        self.fall=1    
        self.jumping=0

class Spike():
    def __init__(self):
        self.spike=pygame.image.load('assets/spike.png')
        self.spike=pygame.transform.rotozoom(self.spike,0,0.7)
        self.x=700
        self.x2=1300
        self.speed=1.3

class Goal():
    def __init__(self):
        self.goal=pygame.image.load('assets/goal.png')
        self.goal=pygame.transform.rotozoom(self.goal,0,1.1)
        self.x=1700
        self.speed=1.3

class Play():
    def __init__(self):
        pygame.init()

        self.screen=pygame.display.set_mode((640,480))
        pygame.display.set_caption('Starkour')

        self.bg=Bg()
        self.starie=Starie()
        self.spike=Spike()
        self.goal=Goal()
        self.clock=pygame.time.Clock()
        #self.fps=60

        self.gameloop()

    def gameloop(self):
        while True:
            #self.clock.tick(self.fps)
            self.get_events()
            self.draw()

    def get_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if self.starie.y==318:
                        self.starie.jump=1

    def draw(self):
        self.draw_bg()
        self.draw_starie()
        self.draw_spikes()
        self.draw_goal()

        pygame.display.flip()

    def draw_bg(self):
        self.screen.blit(self.bg.bg,(self.bg.x-640,0))
        self.screen.blit(self.bg.bg,(self.bg.x,0))
        self.screen.blit(self.bg.bg,(self.bg.x+640,0))
        self.bg.x-=0.5
        if self.bg.x<=-640:
            self.bg.x=0

    def draw_starie(self):
        self.screen.blit(self.starie.starie,(40,self.starie.y))
        if self.starie.y<318:
            self.starie.y+=self.starie.fall
        if self.starie.jump==1:
            self.starie.y-=4
            self.starie.jumping+=1
            if self.starie.jumping>40:
                self.starie.jumping=0
                self.starie.jump=0
    
    def draw_spikes(self):
        self.screen.blit(self.spike.spike,(self.spike.x,351))
        self.spike.x-=self.spike.speed

        self.screen.blit(self.spike.spike,(self.spike.x2,351))
        self.spike.x2-=self.spike.speed

    def draw_goal(self):
        self.screen.blit(self.goal.goal,(self.goal.x,270))
        self.goal.x-=self.goal.speed
        if self.goal.x<-25:
            pygame.display.quit()
            exit()
        
if __name__=="__main__":
    Play()
    