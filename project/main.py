from game_object import *
from text_parser import textparser

#gameLoop
print("Your goal is to drop a key in the hallway! Type help to get started.")
while True:
    textparser(gameobjects['john'])
    if "key" in gameobjects["hallway"].interactables:
        input("You Win! <PRESS ENTER TO EXIT>")
        break
