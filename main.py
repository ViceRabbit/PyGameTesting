import pygame

# VVVVV THIS right here initalizes pygame, this is importanto everytime
pygame.init()

# VVVVV this right here is the screen -- REMEMBER you gotta set like a tuple inside parameters: set_mode((like, this))
gameScreen = pygame.display.set_mode((500, 500))

# VVVV titles and stuff lo -- DONT inherit from gameScreen, just pygame.display
pygame.display.set_caption("Pygame Playground")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# VVVVV so ik replit doesnt close window but its suggested so python doesnt automatically end the code/window
# aka * Game Loop *
active = True
while active:
  for event in pygame.event.get(): # we need a function to close the window!!!!
    if event.type == pygame.QUIT: # so basically pygame.QUIT is the closing window event thing and we chec
      print('Active went false! Code should be terminated')
      active = False # window should be closed as well as the code