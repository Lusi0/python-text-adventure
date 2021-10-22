global gameobjects
gameobjects = {}

#A_object
class A_object:
    def __init__(self):
        pass
class dialog(A_object):
    def __init__(self, knowlage_req, knowlage_given, player_dialog, response):
        self.knowlage_req = knowlage_req
        self.player_dialog = player_dialog
        self.response = response
        self.knowlage_given =knowlage_given
class gameobject(A_object):
    def __init__(self,name,description,location):
        self.name = name
        self.description = description

    def describe(self):
        print("{}".format(self.description))


#interactables
class interactables(gameobject):
    def __init__(self,name,description,location):
        self.name = name
        self.description = description
class person(interactables):
    def __init__(self,name,description,location,dialog):
        self.name = name
        self.description = description
        self.location = location
        self.dialog = dialog

    def listresponses(self,player):
        responses = ["exit"]
        for dialog in self.dialog:
            if dialog.knowlage_req in gameobjects[player].knowlage:
                responses.append(dialog.player_dialog)
        return responses,self.name

    def respond(self,player,string):
        for dialog in self.dialog:
            if dialog.player_dialog == string:
                input("{} Press Enter to continue \n>".format(dialog.response))
                player.knowlage.append(dialog.knowlage_given)
class carrable(interactables):
    def __init__(self,name,description,location):
        self.name = name
        self.description = description
        self.location = location

    def attach(self, object):
        gameobjects[self.location].interactables.remove(self.name)
        gameobjects[object].interactables.append(self.name)
        self.location = object


#rooms
class room(gameobject):
    def __init__(self,name,description,conntections,interactables):
        self.name = name
        self.description = description
        self.conntections = conntections
        self.interactables = interactables
    def describe_exits(self):
        for room in self.conntections:
            print(gameobjects[room].describe())
class locked_room(room):
    def __init__(self,name,description,conntections,interactables,key):
        self.name = name
        self.description = description
        self.conntections = conntections
        self.interactables = interactables
        self.key = key
    def key_lock_check(self,player):
        if key in gameobjects[player].interactables:
            return True
        else:
            return False


#player
class player(gameobject):
    def __init__(self,name,description,location,knowlage):
        self.name = name
        self.description = description
        self.interactables = []
        self.location = location
        self.knowlage = knowlage

    def cur_pos_exits(self):
        gameobjects[self.location].describe_exits()

    def whereami(self):
        print("You are in:")
        gameobjects[self.location].describe()
        print("The exits around you:")
        gameobjects[self.location].describe_exits()

    def move(self, key):
        if key in gameobjects[self.location].conntections:
            if type(gameobjects[key]) == locked_room:
                if gameobjects[key].key in self.interactables:
                    self.location = key
                    print("You have moved to {}!".format(key))
                else:
                    print("You need a key to get in there!")
            else:
                self.location = key
                print("You have moved to {}!".format(key))



    def describe_visible(self):
        print("me:")
        self.describe()
        print("where i am:")
        self.whereami()
        print("The exits around me:")
        gameobjects[self.location].describe_exits()
        if len(gameobjects[self.location].interactables) >= 1:
            print("the things around me:")
            for interactable in gameobjects[self.location].interactables:
                gameobjects[interactable].describe()
        if len(self.interactables) >= 1:
            print("the things I am carrying:")
            for carrable in self.interactables:
                gameobjects[carrable].describe()


    def grab(self, key):
        if key in gameobjects[self.location].interactables:
            if type(gameobjects[key]) is carrable:
                gameobjects[key].attach(self.name)
                print("you picked up {}".format(key))
            else:
                print("cannot pick up {}".format(key))


    def drop(self, key):
        if key in self.interactables:
            gameobjects[key].attach(self.location)
            "you dropped {}".format(key)

    def talk(self, key):
        if key in gameobjects[self.location].interactables:
            if type(gameobjects[key]) == person:
                return gameobjects[key].listresponses(self.name)

gameobjects = {
"johns room":room("johns room","room in which john lives",["hallway"],["key"]),
"hallway":room("hallway","corridor that connects to different parts of the house",["johns room","kates room"],[]),
"john":player("john", "representation of you in this world", "johns room", ["0"]),
"key":carrable("key", "key to kates room", "johns room"),
"kates room":locked_room("kates room","room in which kate lives",["hallway"],["kate"],"key"),
"kate":person("kate","person who lives in your home","kates room",[dialog("0","1","who are you?","I am kate, I live in this room!")])
}
