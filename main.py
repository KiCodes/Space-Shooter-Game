# 1. two required lines for creating any pygame
import math
import random

import pygame
from pygame import mixer

# 0. to initialize the pygame
# 34. for music
pygame.init()
mixer.init()

# background music
mixer.music.load('background music.mp3')
# play music continuously
mixer.music.play(-1)

# 4. game screen (width,height)
screen = pygame.display.set_mode((800, 600))
# 5. adding icon to window
icon = pygame.image.load('spaceship (1).png')
pygame.display.set_icon(icon)

# 6. loading bg image
bg_Image = pygame.image.load('bg_1.JPG')

# 9. loading bg player image
spaceshipImg = pygame.image.load('spaceship (3).png')

# 15. loading invader image
invaderImg = pygame.image.load('invader.png')

# 19. loading bullet image
bulletImg = pygame.image.load('bullet.png')

spaceshipX = 370
spaceshipY = 480
changeX = 0
changeY = 0


# function to load bullet\

def bullet():
    screen.blit(bulletImg, (bulletX, bulletY))


bulletX = spaceshipX + 17
bulletY = spaceshipY - 37
check = False


# 10. function to blit player
def player():
    screen.blit(spaceshipImg, (spaceshipX, spaceshipY))


# 16. function to blits invader
# def invader():
#     screen.blit(invaderImg, (invaderX, invaderY))


# intial invader movements for making one
# invaderX = random.randint(0, 736)
# invaderY = random.randint(30, 150)
# invaderSpeedX = -.5
# invaderSpeedY = 5


pygame.display.set_caption('Space Shooter MAX')# 3. changing title of title bar

# counter
score = 0

# 2. screen will close of code stops in the above unless we loop
running = True

# 25. to display score on screen
font = pygame.font.SysFont('Arial', 32, 'bold')

# 29. game over font
gameOver_font = pygame.font.SysFont('Arial', 65, 'bold')


# 26. create function to display score in white color and blits on screen, "true" to make text smooth
def display_score():
    img = font.render(f'score: {score}', True, 'white')
    screen.blit(img, (10, 10))


# 30. function for gameover display
def gameOver():
    img_o = gameOver_font.render('GAME OVER', True, 'white')
    screen.blit(img_o, (200, 250))


# def collision():
#     # 23. using a formula to calculate the x and y coords of bullet and x and y coords of the enemy
#     distance = math.sqrt(math.pow(bulletX - invaderX, 2) + math.pow(bulletY - invaderY, 2))
#
#     if distance < 27:
#         return True


# 31. creating more invaders
invaderImg = []
invaderX = []
invaderY = []
invaderSpeedX = []
invaderSpeedY = []

no_of_invaders = 7

for i in range(no_of_invaders):
    # 32. loop through to create multiple invaders at once.
    # using append to add information for each item in the list
    invaderImg.append(pygame.image.load('invader.png'))
    invaderX.append(random.randint(0, 736))
    invaderY.append(random.randint(30, 150))
    invaderSpeedX.append(-.6)
    invaderSpeedY.append(2)

while running:
    # 7. running the background image using the blit function which draw the image unto the window and sets dimensions
    screen.blit(bg_Image, (-120, -270))
    for event in pygame.event.get():
        # QUIT for making the close button to exit the loop
        if event.type == pygame.QUIT:
            running = False
        # 12. event to move player along x axis when arrow key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                changeX = -1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                changeX = 1
        if event.type == pygame.KEYUP:
            changeX = 0

        # 13. for Y movement of player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                changeY = -1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                changeY = 1
        if event.type == pygame.KEYUP:
            changeY = 0

        # 20. bullet movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 22. if false to ensure the bullet always starts from the spaceship x
                if check is False:
                    # laserSound = mixer.Sound('laser.mp3')
                    # laserSound.play()
                    check = True
                    bulletX = spaceshipX + 17


    spaceshipY += changeY  # spaceshipX = spaceshipX - changeX
    spaceshipX += changeX  # spaceshipX = spaceshipX - changeX

    # 18. automating the movement of the alien so it reaches the end of the window and down 10px before going in the
    # opposite direction
    # invaderX += invaderSpeedX
    # if invaderX <= 0:
    #     invaderSpeedX += .1
    #     invaderY += invaderSpeedY
    # if invaderX >= 736:
    #     invaderSpeedX -= .1
    #     invaderY += invaderSpeedY

    # invaders loop
    for i in range(no_of_invaders):  # 32.  making loop to replace the code for moving one invader
        # 33. game OVER rule for all
        if invaderY[i] > 380:
            # to make sure the other invaders disappear when one reaches 380px
            for j in range(no_of_invaders):
                invaderY[j] = 2000
            # 34. CALL GAME OVER FUNCTION
            gameOver()
            break

        invaderX[i] += invaderSpeedX[i]
        if invaderX[i] <= 0:
            invaderSpeedX[i] += .1
            invaderY[i] += invaderSpeedY[i]
        if invaderX[i] >= 736:
            invaderSpeedX[i] -= .1
            invaderY[i] += invaderSpeedY[i]

            # 35. extract collision fucntion to run directly in for loop in initial method
        distance = math.sqrt(math.pow(bulletX - invaderX[i], 2) + math.pow(bulletY - invaderY[i], 2))

        if distance < 27:
            exploSound = mixer.Sound('explosion.mp3')
            exploSound.play()
            bulletY = spaceshipY - 37
            # if bullet hits enemy it should stop running in a loop which makes it to continuously shoot
            check = False
            invaderX[i] = random.randint(0, 736)
            invaderY[i] = random.randint(30, 150)
            # adding score value to count for anytime there is a collision
            score += 1
        screen.blit(invaderImg[i], (invaderX[i], invaderY[i]))

    # 14. to prevent player from going out of bounds
    if spaceshipY >= 480:
        spaceshipY = 480
    elif spaceshipY <= 400:
        spaceshipY = 400

    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 736:
        spaceshipX = 736

    #  21. bullet function
    # brings bullet back to original position anytime it reaches the top
    if bulletY <= 0:
        bulletY = spaceshipY - 37
        check = False

    if check is True:
        bullet()
        bulletY -= 2

    # # 28. game OVER rule for initally one invader
    # if invaderY > 380:
    #     invaderY = 2000
    #     # 30. CALL GAME OVER FUNCTION
    #     gameOver()

    # 11. call player function
    player()
    # 17. invader function for displaying on window
    # invader()

    # # 24. call collision function
    # collision_occurred = collision()
    #
    # if collision_occurred:
    #     bulletY = spaceshipY - 37
    #     # if bullet hits enemy it should stop running in a loop which makes it to continuously shoot
    #     check = False
    #     invaderX = random.randint(0, 736)
    #     invaderY = random.randint(30, 150)
    #     # adding score value to count for anytime there is a collision
    #     score += 1

    display_score()
    # 27. call display score function above
    # 8. update display to see background img # on each creation of the loop an updating will take place
    pygame.display.update()
