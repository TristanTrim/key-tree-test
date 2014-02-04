import charSets
import pygame
from pygame.locals import *

## OMG THIS IS FUCKKKKED!!
## HOW CAN THE BEST WAY TO GET KEYSTATES IN PYTHON
## BE TO USE A FUXKEN PYGAME DISPLAY WINDOW???

## FUCK IT IM DONE>

## THIS IS DUMB


pygame.init()
pygame.display.set_mode((200,200))


typedstuff = ""

while True:

  space = False
  u = False
  eight = False
  nine = False
  p = False

  keyDown = True
  while keyDown: 
    keyDown = False
  
  ## Key checking
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
  
    if(keys[K_q]):
      break

    if(keys[K_SPACE]):
      space = True
      keyDown = True
  
    if(keys[K_u]):
      u = True
      keyDown = True

    if(keys[K_8]):
      eight = True
      keyDown = True

    if(keys[K_9]):
      nine = True
      keyDown = True

    if(keys[K_p]):
      p = True
      keyDown = True

  keyValue = -1

  if p:
    keyValue+=1
  if nine:
    keyValue+=2
  if eight:
    keyValue+=4
  if u:
    keyValue+=8
  if space:
    keyValue+=16

  if(keyValue>-1):
    typedstuff+=charSets.charSets.normal[keyValue]
    print("\n\n\n\n\n")
    print(typedstuff)

print(charSets.charSets.normal[0])





