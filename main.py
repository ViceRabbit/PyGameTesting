import pygame
import os
import numpy as np
# reference tutorial: https://www.youtube.com/watch?v=FfWpgLFMI7w&t=414s&ab_channel=freeCodeCamp.org
# VVVVV THIS right here initalizes pygame, this is importanto everytime
os.environ['SDL_AUDIODRIVER'] = 'disk'
pygame.init()

# VVVVV this right here is the screen -- REMEMBER you gotta set like a tuple inside parameters: set_mode((like, this))
gameScreen = pygame.display.set_mode((500, 500))

# VVVV titles and stuff lo -- DONT inherit from gameScreen, just pygame.display
pygame.display.set_caption("Pygame Playground")
icon = pygame.image.load('icon.png') # how u load images (pygame.image.load())
pygame.display.set_icon(icon)

# P2 - Defining Player Object (for now i kept as carrot lo)
carrotImg = pygame.image.load('carrot.png') # here im loading my carrot as its an image
playerX = 210 # we dont know size of img well, 250 is half of screen size, so lowered it to 220
playerY = 250 # close to 500, as we want it below
playerXChange = 5
playerYChange = 5
definiteX = 1
definiteY = 1

rectX = 139
rectY = 287
rectXChange = 0
rectYChange = 0


clock = pygame.time.Clock()

gamefont = pygame.font.SysFont('monospace', 14)

def player(x, y):
  # VVV this should take 2 parameters: thing to draw, and tuple of x and y coords, .blit basically means to draw; we
  # are drawing img of carrot on our screen (aka surface)
  gameScreen.blit(carrotImg, (x, y))
def rectangle(x, y):
  pygame.draw.rect(gameScreen, (255, 0, 0), pygame.Rect(x, y, 50, 50))

def gameTextCoordinates(fontp, textp, color, loc):
  gametext = fontp.render(textp, False, color)
  gameScreen.blit(gametext, loc)


# Concept; picks 2 random int from 1-10, one being x and one being y. the rect increments by the specific int given within the x or the y. if the rect hits the boundary, 
# the random int does a respin, vice-versa with left/right/up/down  

# Boundary; X (LEFT): -4, X (RIGHT): 469, Y (UP): -6, Y (DOWN): 460
BoundXLeft = -4
BoundXRight = 469
BoundYUp = -6
BoundYDown = 460

# make so it doesnt auto close code
# aka * Game Loop * 225 281
active = True
while active:
  gameScreen.fill((50, 50, 50)) # background fill, ensure its in a tuple: .fill((R, G, B))
  playerX += playerXChange
  playerY += playerYChange
  if playerX + playerXChange < BoundXLeft or playerX + playerXChange > BoundXRight:
    print(f'Hit boundary!; XChange = {playerXChange}')
    definiteX *= -1
    randomints = np.sort(np.array([1*definiteX, 10*definiteX]))
    playerXChange = np.random.randint(low=randomints[0], high=randomints[1])
  if playerY + playerYChange < BoundYUp or playerY + playerYChange > BoundYDown:
    print(f'Hit boundary!; YChange = {playerYChange}')
    definiteY *= -1
    randomints = np.sort(np.array([1*definiteY, 10*definiteY]))
    playerYChange = np.random.randint(low=randomints[0], high=randomints[1])

    # generate two np randoms, so like np.random.randint(1, 10) for right but liek for left its like (-1, -10)

  # P2: game.Screen should be filled BEFORE any blits! because pygame is drawing them in order!
  for event in pygame.event.get(): # we need a function to close the window!!!!
    if event.type == pygame.QUIT: # so basically pygame.QUIT is the closing window event thing and we chec
      print('Active went false! Code should be terminated')
      active = False # window should be closed as well as the code
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        rectXChange -= 10
      if event.key == pygame.K_RIGHT:
        rectXChange += 10
      if event.key == pygame.K_UP:
        rectYChange -= 10
      if event.key == pygame.K_DOWN:
        rectYChange += 10
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        rectXChange = 0
      if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        rectYChange = 0

  # also gameScreen.fill can be above for event, to prevent any miss-conceptions!
  if rectX + rectXChange < 469 and rectX + rectXChange > -4:
   rectX += rectXChange
  if rectY + rectYChange > -6 and rectY + rectYChange < 460:
    rectY += rectYChange

  player(playerX, playerY) # We want it to update (carrot) everytime!
  rectangle(rectX, rectY)
  gameTextCoordinates(gamefont, f"Loc: x:{rectX}, y:{rectY}", (0, 255, 0), (29, 477))

  #pygame.draw.rect(gameScreen, (0, 255, 0), pygame.Rect())
  # x, y = pygame.mouse.get_pos()
  # print(x, y, flush=False, end='\r')
  pygame.display.update() # 139 287 without this, any changes wouldnt occur as the display isnt updating!!
  clock.tick(60)
  # 199 4877