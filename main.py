import pygame
# reference tutorial: https://www.youtube.com/watch?v=FfWpgLFMI7w&t=414s&ab_channel=freeCodeCamp.org
# VVVVV THIS right here initalizes pygame, this is importanto everytime
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

def player(x, y):
  # VVV this should take 2 parameters: thing to draw, and tuple of x and y coords, .blit basically means to draw; we
  # are drawing img of carrot on our screen (aka surface)
  gameScreen.blit(carrotImg, (x, y))

# VVVVV so ik replit doesnt close window but its suggested so python doesnt automatically end the code/window
# aka * Game Loop *
active = True
inverse = True
while active:
  if inverse:
    playerY -= 0.1
  else:
    playerY += 0.1
  if playerY > 500 or playerY < 0:
    inverse = not inverse
  gameScreen.fill((50, 50, 50)) # background fill, ensure its in a tuple: .fill((R, G, B))
  # P2: game.Screen should be filled BEFORE any blits! because pygame is drawing them in order!
  for event in pygame.event.get(): # we need a function to close the window!!!!
    if event.type == pygame.QUIT: # so basically pygame.QUIT is the closing window event thing and we chec
      print('Active went false! Code should be terminated')
      active = False # window should be closed as well as the code

  # also gameScreen.fill can be above for event, to prevent any miss-conceptions!

  player(playerX, playerY) # We want it to update (carrot) everytime!
  pygame.display.update() # without this, any changes wouldnt occur as the display isnt updating!!



