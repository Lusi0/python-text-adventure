from game_object import *
from text_parser import textparser
#gameLoop
print("talk to kate! type help to begin.")
textparserreturn = [False,'']
player = gameobjects['john']
while True:
    textparserreturn = textparser(player,textparserreturn)

    #the owen conditingecy
    if textparserreturn[0] == True:
        if textparserreturn[1] not in gameobjects or player.location != gameobjects[textparserreturn[1]].location:
            textparserreturn[0] = False
            print("I don't know who {} is!".format(textparserreturn[1]))
    if "1" in gameobjects["john"].knowlage:
        input("You Win! <PRESS ENTER TO EXIT>")
        break
