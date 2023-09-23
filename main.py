import pygame
import random
import math

# initializing pygame
pygame.init()

# creating game screen
screen = pygame.display.set_mode([1425,800])

# Title & icon
pygame.display.set_caption("Night Walkers")
icon = pygame.image.load('city-2.png')
pygame.display.set_icon(icon)

#background
bg = pygame.image.load("background.png")

#player
playerImg = pygame.image.load('player.png')
playerX = 25
playerY = 500
move = 3
changeX = 0
changeY = 0

#drawing player to screen
def player(x,y):
    screen.blit(playerImg, (x, y))

#detecting collisions
def collision(objX1, objY1, objX2, objY2):
    dist = math.sqrt(math.pow(objX2-objX1, 2) + math.pow(objY2-objY1, 2))
    if (dist < 75) :
        return True
    
    return False

#enemy
enemyImg = pygame.image.load('man.png')
enemyX = random.randint(300,1200)
enemyY = random.randint(300,600)
enemyMove = 3
enemyChangeX = random.randint(-3, 3)
enemyChangeY = random.randint(-2, 3)
eMoveList = [-2, -1, 1, 2]


#drawing enemy to screen
def enemy(x,y):
    screen.blit(enemyImg, (x, y))

# game loop
running = True
while running: 
    #background colour
    screen.fill((4,7,36))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # checking whether arrow keys pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX -= move
            if event.key == pygame.K_RIGHT:
                changeX += move
            if event.key == pygame.K_UP:
                changeY -= move
            if event.key == pygame.K_DOWN:
                changeY += move
        # checking if arrow key no longer being pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changeY = 0
    playerX += changeX
    playerY += changeY

    if playerY >= 600:
        playerY = 600
    elif playerY <= 300:
        playerY = 300
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1200:
        playerX = 1200
    
    # checking boundary of enemy movement
    #enemyChangeX = random.randint(-3, 3)
    #enemyChangeY = random.randint(-2, 3)
    
    enemyX += enemyChangeX
    enemyY += enemyChangeY

    if enemyY >= 600:
        enemyY = 600
        enemyChangeY -= enemyMove
        enemyChangeX = random.choice(eMoveList)
        enemyChangeY = random.choice(eMoveList)
    elif enemyY <= 300:
        enemyY = 300
        enemyChangeY += enemyMove
        enemyChangeX = random.choice(eMoveList)
        enemyChangeY = random.choice(eMoveList)
    if enemyX <= 0:
        enemyX = 0
        enemyChangeX += enemyMove
        enemyChangeX = random.choice(eMoveList)
        enemyChangeY = random.choice(eMoveList)
    elif enemyX >= 1200:
        enemyX = 1200
        enemyChangeX -= enemyMove
        enemyChangeX = random.choice(eMoveList)
        enemyChangeY = random.choice(eMoveList)

    if (collision(playerX, playerY, enemyX, enemyY)):
        enemyChangeX = 0
        enemyChangeY = 0
        changeX = 0
        changeY = 0

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    #pygame.draw.rect(screen, (255,0,0), pygame.Rect(30, 30, 200, 200))
    pygame.display.update()