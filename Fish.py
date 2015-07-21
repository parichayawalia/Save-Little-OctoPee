import pygame, random
import sys, math
import time
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN=(85,107,47)
L_GREEN=(45, 51, 22)
YELLOW=(255, 250, 0)
SEA=(0,78,133)
color_lst=[RED, BLUE, GREEN, YELLOW]
flag,dist= 0,0
tt=0
const_dimension=20
bool_list=[0,1,1]
tag_list=[1,2,3,4]      #Stands for 1st 2nd 3rd 4th quadrants
#TIME ELAPSED za
t0=pygame.time.get_ticks()
level=1
level_up=False
c=1

def blit_alpha(screen, source, location):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(screen, (-x, -y))
        temp.blit(source, (0, 0))
               
        screen.blit(temp, location)
#Text on Screen
def text_to_screen(screen, text, x,y, size):
    text=str(text)
    font =pygame.font.SysFont("comicsansms",size)
    text=font.render(text, True, BLACK)
    screen.blit(text, (x,y))

def Intermediate():
        def __init__(self):
                super().__init__()
                self.image = pygame.Surface([200, 150])
                self.image.set_alpha(190)  
                self.image.fill(WHITE)
                self.rect = self.image.get_rect()
                pygame.draw.circle(self.image, self.color,(int(self.rect.x+3), int(self.rect.y)+self.radius), self.radius, 0)
                pygame.time.wait(1000)
def over():
    blast=pygame.image.load("blast.png").convert_alpha()
    screen.blit(blast, (player.rect.x-7, player.rect.y-10))
    
    print("GAME OVER.")
    monster=pygame.image.load("monster.gif").convert_alpha()
    screen.blit(monster, (screen_width/2-180, screen_height/2-100 ))
    screen.blit(gameover, (int(screen_width/2-100),int(screen_height/2-30)))
    pygame.display.flip()
    pygame.time.wait(900)
           
    pygame.quit()
    sys.exit()

# --- Classes


        
class Bubble(pygame.sprite.Sprite):
        
    def __init__(self, color):
# Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([8, 8])
        self.radius=4
        self.color=color
        self.tag=random.choice(tag_list)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, color,(int(self.rect.x)+self.radius, int(self.rect.y)+self.radius), self.radius, 0)
        
    def update(self):
        self.rect.y+=1

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.tag=random.choice(tag_list)
        #s = pygame.Surface([20,20])  # <----- this one is different!
        self.image=pygame.image.load("enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,0,255))
        self.rect.x= random.randint(10, screen_width-10)
        self.rect.y = random.randint(10, screen_height-10)
         
        
 
         
class Player(pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__()
         
        self.images = []
        self.images.append(pygame.image.load("oo1.png").convert_alpha())
        self.images.append(pygame.image.load("oo2.png").convert_alpha())
        self.images.append(pygame.image.load("oo3.png").convert_alpha())
        self.images.append(pygame.image.load("oo4.png").convert_alpha())
        
        self.index = 0
        self.image = self.images[self.index].convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x= random.randint(10, screen_width-10)
        self.rect.y = random.randint(10, screen_height-10)
     
    def move(self):
        pos = pygame.mouse.get_pos()
       
        self.rect.x = pos[0]-20
        self.rect.y=pos[1]-23
        
            #FOR MOTION
    '''def update(self):
        pos = pygame.mouse.get_pos()
       
        self.rect.x = pos[0]-20
        self.rect.y=pos[1]-23'''
         
        
    def update(self):
        self.index += 1    
         
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


         
# Initialize Pygame
pygame.init()

#XXXXXXXXXXXXXX Creating New Blocks       
def create_new_sprites():
   
    bubble = Bubble(BLUE)
     
    bubble.rect.x = random.randint(10, screen_width-10)
    bubble.rect.y = random.randint(10, screen_height-10)
    
    bubble_list.add(bubble)
    collective_list.add(bubble)
    all_sprites_list.add(bubble)
def create_enemy():
    bubble = Enemy(RED)
     
    bubble.rect.x = random.randint(10, screen_width-10)
    bubble.rect.y = random.randint(10, screen_height-10)
    enemy_list.add(bubble)
    collective_list.add(bubble)
    all_sprites_list.add(bubble)

      
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
gameover=pygame.image.load("gameover.png").convert_alpha()
background=pygame.image.load("ocean.jpg").convert()
#XXXX

# --- Sprite lists

all_sprites_list = pygame.sprite.Group()
bubble_list = pygame.sprite.Group()
enemy_list=pygame.sprite.Group()
collective_list=pygame.sprite.Group()


# --- Create the sprites
for i in range(4):
     create_new_sprites()
enemy=Enemy()
 
enemy_list.add(enemy)
collective_list.add(enemy)
all_sprites_list.add(enemy)


   
# Create player block

#all_sprites_list.add(player)
player = Player()
 
player_list=pygame.sprite.Group()
player_list.add(player)
done = False
clock = pygame.time.Clock()
score = 0
player.rect.y = random.randint(10, screen_height)

# -------- Main Program Loop -----------
while not done:
    t1=pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
          
           
        elif event.type == pygame.USEREVENT + 1:
            create_new_sprites()
            level+=1
            tt=0
            if level==2:        #8 Bubbles 1Enemy. 
                for j in range(8):
                    create_new_sprites()
                 
            elif level==3:
                j=0
                for j in range (10):  #8 bubbles 1 Enemy Fast
                    create_new_sprites()
                c+=0.5
            elif level==4:
                j=0
                for j in range (10):  #10 bubbles 1 Enemy Faster
                    create_new_sprites()
                c+=0.5
            elif level==5:
                j=0
                for j in range (5):  #5 bubbles 2 Enemies
                    create_new_sprites()
                c-=1
                enemy=Enemy()
                enemy_list.add(enemy)
                collective_list.add(enemy)
                all_sprites_list.add(enemy)
            elif level==6:
                 for j in range (8):  #5 bubbles 2 Enemies
                    create_new_sprites()
            elif level==7:
                for j in range (8):  #8 bubbles 2 enemies Faast
                    create_new_sprites()
                c+=0.5
            elif level==8:
                for j in range (8):  #8 bubbles 2 enemies Faast
                    create_new_sprites()
                c+=0.5
            elif level==9:
                j=0
                for j in range (5):  #5 bubbles 3 Enemies
                    create_new_sprites()
                c-=1
                enemy=Enemy()
                enemy_list.add(enemy)
                collective_list.add(enemy)
                all_sprites_list.add(enemy)
            elif level==10:
                 for j in range (8):  #8 bubbles 3 Enemies
                    create_new_sprites()
            elif level==11:
                for j in range (8):  #8 bubbles 3 enemies Faast
                    create_new_sprites()
                c+=0.5
            elif level==12:
                for j in range (8):  #8 bubbles 3 enemies Faast
                    create_new_sprites()
                c+=0.5
            elif level==13:
                j=0
                for j in range (5):  #5 bubbles 4 Enemies
                    create_new_sprites()
                c-=1
                enemy=Enemy()
                enemy_list.add(enemy)
                collective_list.add(enemy)
                all_sprites_list.add(enemy)
            elif level==14:
                 for j in range (8):  #8 bubbles 4 Enemies
                    create_new_sprites()
            elif level==15:
                for j in range (8):  #8 bubbles 4 enemies Faast
                    create_new_sprites()
                c+=0.5
            else:
                text_to_screen(screen,"Game Complete!" , screen_width/2-80,screen_height/2, 28)
                pygame.time.wait(1000)
                pygame.quit()
                sys.exit()
        elif event.type == pygame.USEREVENT + 2:
            player_list.update()
                                 
                
    for bubble in collective_list:
        if bubble.tag==1:
            dist_x, dist_y= c,-c
        elif bubble.tag==2:
            dist_x, dist_y=-c,-c
        elif bubble.tag==3:
            dist_x, dist_y=-c,c
        elif bubble.tag==4:
            dist_x, dist_y=c,c
        
        ##IN CASE OF BOUNDARY COLLISONS:
        if bubble.rect.x<=0:
            if bubble.tag==2:
                bubble.tag=1
            elif bubble.tag==3:
                bubble.tag=4
            #clock.tick(200)
        if bubble.rect.x>=screen_width:
            if bubble.tag==4:
                bubble.tag=3
            elif bubble.tag==1:
                bubble.tag=2
        if bubble.rect.y<=0:
            if bubble.tag==1:
                bubble.tag=4
            elif bubble.tag==2:
                bubble.tag=3
        if bubble.rect.y>=screen_height:
            if bubble.tag==4:
                bubble.tag=1
            elif bubble.tag==3:
                bubble.tag=2
        bubble.rect.x+=dist_x           #Update new posiitons
        bubble.rect.y+=dist_y
     

    bubble_hit_list = pygame.sprite.spritecollide(player, bubble_list, True)
           
# For each bubble collision , remove and generate a new one somewhere else
    for bubble in bubble_hit_list:
        bubble_list.remove(bubble)
        all_sprites_list.remove(bubble)
        score += 1
        choice=random.choice(bool_list)
        if choice==1:
            
            create_new_sprites()
        #print(score)
         
    enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
    if len(enemy_hit_list)>0:
        over()


    ###IF BUBBLES ARE OVER, LEVEL UP!
    if len(bubble_list)==0:
        level_up=True
                 
        
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    player.move()
    screen.blit(enemy.image, enemy.rect)
    
    bubble_list.draw(screen)
    collective_list.draw(screen)
    text_to_screen(screen,score, 30,30, 20)
   
    if level_up==True:
        green= pygame.image.load("green2.png").convert_alpha()
        screen.blit(green, (0,0))
        clock.tick(200)
        text_to_screen(screen,"LEVEL UP!" , screen_width/2-80,screen_height/2, 28)
        tt+=1
        if tt>70:       #Total TIme for level up display
            next_level=pygame.USEREVENT+1
            next_level_event=pygame.event.Event(next_level)
            pygame.event.post(next_level_event)
            tt=0
            level_up=False
          #level increase
    text_to_screen(screen, "Level :"+str(level) , screen_width-60,12, 16)
    #sec_list.update()            ##
    dt=t1-t0
     
    if dt>300:
        #Image time for each Octopus Sprite
        flap=pygame.USEREVENT+2
        flap_event=pygame.event.Event(flap)
        pygame.event.post(flap_event)
        t0=t1
        clock.tick(200) 
    clock.tick(200)
    blit_alpha(screen, player.image, player.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
  
pygame.quit()
 
