from game_object import *


def textparser(player,textparser_):
    if textparser_[0] != False:
        talkto = textparser_[1]
    if textparser_[0] == True:
        responses = []
        for num,response in enumerate(player.talk(talkto)[0]):
            responses.append(response)
            print("{}: {}".format(num,response))
        playerinput = input(">").split(" ")
        try:
            playerinput = int(playerinput[0])
        except:
            print("Please enter a number!")
        else:
            gameobjects[player.talk(talkto)[1]].respond(player,responses[playerinput])
        if playerinput == 0:
            return [False,'']
    else:
        playerinput = input(">").split(" ")
    if textparser_[0] == True:
        pass
    elif playerinput[0].lower() == "describe" and len(playerinput)>1:
        newstr = ""
        for num,word in enumerate(playerinput[1:]):
            newstr += word
            if num+2 < len(playerinput):

                newstr += " "
        if newstr in gameobjects:
            gameobjects[newstr].describe()
        else:
            print("Not sure what {} is!".format(newstr))
    #describe game_object use describe

    elif playerinput[0].lower() == "lookaround":
        player.describe_visible()
    #list game_objects use describe_visible

    elif playerinput[0].lower() == "whereami":
        player.whereami()

    elif playerinput[0].lower() == "exits":
        player.cur_pos_exits()
    #describe_exits use cur_pos_exits

    elif playerinput[0].lower() == "goto":
        newstr = ""
        for num,word in enumerate(playerinput[1:]):
            newstr += word
            if num+2 < len(playerinput):
                newstr += " "
        player.move(newstr)
    #go through use move
    elif playerinput[0].lower() == "grab":
        newstr = ""
        for num,word in enumerate(playerinput[1:]):
            newstr += word
            if num+2 < len(playerinput):
                newstr += " "
        player.grab(newstr)
    #interactables grab use grab
    elif playerinput[0].lower() == "drop":
        newstr = ""
        for num,word in enumerate(playerinput[1:]):
            newstr += word
            if num+2 < len(playerinput):
                newstr += " "
        player.drop(newstr)

    #interactables drop use drop
    elif playerinput[0].lower() == "lusio" and playerinput[1].lower() == "gaming":
        print("Addicted to short stupid science moron man and should leave!")
        print("AHHHHHH THE SWEET SMELL OF SCIENCE!!!!!!!!!!")


    elif playerinput[0].lower() == "talk":
        talkto = ""
        for num,word in enumerate(playerinput[1:]):
            talkto += word
            if num+2 < len(playerinput):
                talkto += " "
        return [True,talkto]





    elif playerinput[0].lower() == "help":
        if len(playerinput) == 1:
            print("""Describe <gameobject>
WhereAmI
LookAround
Exits
Goto <room>
Grab <carrable>
Drop <carrable>
Talk <person>
Help <command>
NEVER INCLUDE ANGLE BRACKETS IN COMMANDS""")
        elif playerinput[1].lower() == "describe":
            print("Useage: Describe <gameobject> i.e. Describe John -> John is a cool guy")
        elif playerinput[1].lower() == "whereami":
            print("Useage: WhereAmI i.e. WhereAmI -> Marys house is a place wher Mary lives")
        elif playerinput[1].lower() == "lookaround":
            print("Useage: LookAround i.e. LookAround -> A list containing all visible game objects")
        elif playerinput[1].lower() == "exits":
            print("Useage: Exits i.e. Exits -> Street is a place where cars drive")
        elif playerinput[1].lower() == "goto":
            print("Useage: Goto <room> i.e. Goto Street -> You have moved to Street!")
        elif playerinput[1].lower() == "grab":
            print("Useage: Grab <carrable> i.e. Grab Key -> you picked up key")
        elif playerinput[1].lower() == "drop":
            print("Useage: Drop <carrable> i.e. Drop Key -> you dropped key")
        elif playerinput[1].lower() == "talk":
            print("Useage: Talk <person> i.e. Talk josh -> opens up dialog options with josh")
        elif playerinput[1].lower() == "help":
            print("Useage: Help i.e. Help -> A list of all commands")
            print("Useage: Help <Command> i.e. Help Help -> A description of the help command")
    return [False,'']
