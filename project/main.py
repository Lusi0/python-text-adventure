from game_object import *
from text_parser import textparser

#gameLoop
print("Your goal is to drop a key in the hallway!")
while True:
    textparser(gameobjects['john'])
    if "key" in gameobjects["hallway"].interactables:
        print("You Win!")
        break
