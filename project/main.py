from text_parser import *
import art 
#gameLoop
print(art.text2art("carry the rice", font="colossal"))
print("delever the rice to the shogun! type help to begin.")
textparserreturn = [False,'']
player = gameobjects['me']
while True:
    textparserreturn = textparser(player,textparserreturn)

    #the owen contingingecy
    if textparserreturn[0] == True:
        if textparserreturn[1] not in gameobjects or player.location != gameobjects[textparserreturn[1]].location:
            textparserreturn[0] = False
            print("I don't know who {} is!".format(textparserreturn[1]))
