from text_parser import *
import art 
#gameLoop
print(art.text2art("carry the rice", font="colossal"))
print("delever the rice to the shogun! type help to begin.")
textparserreturn = [False,'']
player = gameobjects['me']
saved_game_objects = gameobjects
while True:
    textparserreturn = textparser(player,textparserreturn)

    #the owen contingingecy
    if textparserreturn[0] == True:
        print(textparserreturn[1], textparserreturn[1] in gameobjects, player.location, player.location != gameobjects[textparserreturn[1]].location)
        if textparserreturn[1] not in gameobjects or player.location != gameobjects[textparserreturn[1]].location:
            textparserreturn[0] = False
            print("I don't know who {} is!".format(textparserreturn[1]))

    #death contingency
    if player.health <= 0:
        print("You are dead!, play again? (y/n)")
        input(">")
        if input(">") == "y":
            player = gameobjects['me']
            saved_game_objects = gameobjects
            print("you are back!")
        else:
            break

    #edo palace contingency
    if player.location == gameobjects['edo palace'].location:
        print("Once inside the palace the personal guard of the shogun greet you and ask them to let them lead you through the palace press enter to coninute")
        input(">")
        print("They lead you through the castle until you make it to the tea room where they stop abruptly signaling for you to go inside press enter to continue")
        input(">")
        print("You enter the tea room by bowing your head. The shogun is seated at a stout table. You sit down and he pours your tea into a simple clay bowl, in stark contrast to the rest of the castle, this whole room is meant to be simple and lowly, to humble. press enter to continue")
        input(">")
        print("The shogun then says to you, 'My boy, it has been some time since I have seen you, since before the war, look how you have grown. Thank you for coming and bringing the rice, it is hard building a new reign, and we need all the support we can get. press enter to continue'")
        input(">")
        if "bags of rice" in player.interactables and gameobjects["bags of rice"] > 7:
            print("you win!, play again?")
            input(">")
            if input(">") == "y":
                player = gameobjects['me']
                saved_game_objects = gameobjects
                print("you are back!")
            else:
                break
        else:
            print("you lose!, play again?")
            input(">")
            if input(">") == "y":
                player = gameobjects['me']
                saved_game_objects = gameobjects
                print("you are back!")
            else:
                break

