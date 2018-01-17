import pygame
import random
import math

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Pyramid"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
RED = (255, 0, 0)
GREEN = (0, 125, 0)
BLUE = (91, 154, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 242, 0)
DUST = (255, 125, 0)
SAND = (255, 213, 61)
            
    # Drawing code
''' sky '''
screen.fill(BLACK)
''' sun '''
pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])


rain = []
for i in range (1000):
    x = random.randrange(0,800)
    y = random.randrange(50,500)
    r = random.randrange(1,5)
    n = (x, y, r, r)
    rain.append(n)
    
def draw_clouds(loc):
    x, y = loc
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])
    
    

def draw_grass():
    pygame.draw.rect(screen, SAND, [50, 100, 300, 200])
    pygame.draw.rect(screen, YELLOW, [50, 100, 300, 200])
    
def draw_fence(y) :
    
    y = 520
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40],[x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 530], [800, 530], 5)
    pygame.draw.line(screen, WHITE, [0, 550], [800, 550], 5)

def house():
    pygame.draw.rect(screen, SAND, [1, 500, 800, 100])
    pygame.draw.line(screen, SAND, [1, 1], [1,1], 10)
    pygame.draw.rect(screen, DUST, [1, 480, 500, 70])
    pygame.draw.rect(screen, DUST, [1, 410, 400, 70])
    pygame.draw.rect(screen, DUST, [1, 340, 300, 70])
    pygame.draw.rect(screen, DUST, [1, 270, 200, 70])
    pygame.draw.rect(screen, DUST, [1, 200, 100, 70]) 
    pygame.draw.polygon(screen,DUST
                        ,[[0,125], [-140,200], [100,200]])
   

clouds_locs = []
for i in range (20):
    x = random.randrange (0,600)
    y = random.randrange (0,50)
    loc = [x, y]
    clouds_locs.append(loc)

    
        
   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # Game logic

 



    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)
    for n in rain:
        pygame.draw.ellipse(screen, BLUE, n)
    for loc in clouds_locs:
        draw_clouds(loc)
    house()
    draw_fence(100)        


# Close window and quit
pygame.quit()

