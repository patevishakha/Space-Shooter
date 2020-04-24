import pygame
import random
import math
#initialise whenever opening the new window of game
pygame.init()
# to create window
screen = pygame.display.set_mode((800,600))

#to change the name and icon  of pygame window
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load('space2.png')
pygame.display.set_icon(icon)

#to add background image
bg_img = pygame.image.load('Image4.jpg')
bg_img = pygame.transform.scale(bg_img,(800,600))

#shooter
player_img = pygame.image.load('space3.png')
player_x = 380
player_y = 510
p_dx = 0

#enemies coming
enemy_img = []
enemy_x = []
enemy_y = []
e_dx = []
e_dy = []
enemy_no = 6

for i in range(enemy_no):
    enemy_img.append(pygame.image.load('alien.png'))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(40,200))
    e_dx.append(3) # no need of append as simple variable e_dx=3
    e_dy.append(40)# no need of append e_dy=40
    
#bullet
bullet_img = pygame.image.load('bullet1.jpg')
bullet_img = pygame.transform.scale(bullet_img,(12,12))
bullet_x = 0 
bullet_y = 510
b_dy = 10
b_state="steady_state" # we can not see bullet on screen 

#score
score=0 # to print score on terminal
score_val = 0 #to print score on pygame window
font = pygame.font.Font('freesansbold.ttf', 32)# pygame font
game_over_font = pygame.font.Font('freesansbold.ttf',70)
text_x = 10
text_y = 10

def show_score(x,y):
    # for displaying text we have to render first then blit
    player_score = font.render(f"YOUR SCORE : {score_val}",True,(110,200,80))
    screen.blit(player_score,(x,y))

def game_over():
    text = game_over_font.render("GAME OVER",True,(250,250,250))
    screen.blit(text,(170,250))
    
def player(x,y):
    #to display spaceship on window
    screen.blit(player_img,(x,y)) # blit for image

def enemy(x,y,i):
    #to display enemy alien on window
    screen.blit(enemy_img[i],(x,y))
    
def bullet_fire(x,y):
    global b_state
    b_state="fire"
    screen.blit(bullet_img,(x+25 ,y+10))

def is_collision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = math.sqrt((math.pow(enemy_x-bullet_x,2))+(math.pow(enemy_y-bullet_y,2)))
    if distance<25:
        return True
    else:
        return False

#game loop
running = True
while running:
    screen.fill((10,10,40))# setting RGB color
    screen.blit(bg_img,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            
            '''print("we are done")'''
            running = False

        # if key is pressed to check whether it is -> or <-
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("left arrow is pressed\n")
                p_dx = -4# x co-ordinate should decrease for spaceship
            elif event.key==pygame.K_RIGHT:
                print("Right key is pressed\n")
                p_dx = 4 # x co-ordinate should increase  for spaceship
            elif event.key==pygame.K_SPACE:
                if b_state=="steady_state":
                    bullet_x=player_x
                    bullet_fire(bullet_x,bullet_y)
                

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                print("left arrow is released\n")
                p_dx = 0
            elif event.key==pygame.K_RIGHT:
                print("Right key is released\n")
                p_dx = 0 

    player_x = player_x + p_dx
    #boundary condition for x co-ordinate for spaceship
    if player_x <=0:
         player_x = 0
    elif player_x >=736:
        player_x = 736

    #movement of enemy
        
    for i in range(enemy_no):
        # game over
        if enemy_y[i]>440:
            for j in range(enemy_no):
                enemy_y[j]=1200
            game_over()
            break
        
        enemy_x[i] = enemy_x[i] + e_dx[i]
        if enemy_x[i] <=0:
            e_dx[i] = 4 #when reached to 0 then start moving in opposite(forward) direction
            enemy_y[i] = enemy_y[i]+e_dy[i] # then move down by 30 pixel as e_dy=30
        elif enemy_x[i] >=736:
            e_dx[i] = -4 #when reached to 736 then start moving in opposite(backward) direction
            enemy_y[i] = enemy_y[i]+e_dy[i] # then move down by 30 pixel as e_dy=30

        #collision of bullet with enemies
        collision = is_collision(enemy_x[i],enemy_y[i],bullet_x,bullet_y)
        if collision==True:
            bullet_y=510
            b_state="steady_state" #as enemy is shooted bullet should dis-appear
            score+=1
            print(score)
            score_val+=1
            enemy_x[i] = random.randint(0,736)
            enemy_y[i] = random.randint(40,150)
            
        enemy(enemy_x[i],enemy_y[i],i)#calling function for enemies 
        
    #bullet firing 
    if bullet_y <=0:
        bullet_y = 510
        b_state="steady_state"
        
    if b_state=="fire":
        bullet_fire(bullet_x,bullet_y)# continuosly appearing bullet 
        bullet_y=bullet_y - b_dy # when fired it will go up

   

        
    player(player_x,player_y)#calling function for player for spaceship
    show_score(text_x,text_y)# calling show function 
    pygame.display.update()#for updating window
                
  
