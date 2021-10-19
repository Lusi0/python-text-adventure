from game_object import *
from text_parser import textparser

#gameLoop
while True:
    print("here")
    textparser()
gameobjects['john'].grab('key')
gameobjects['john'].describe_visible()
gameobjects['john'].drop('key')
gameobjects['john'].describe_visible()
