global gameobjects
gameobjects = {}
class gameobject:
    def __init__(self,name,description,location):
        self.name = name
        self.description = description

    def describe(self):
        print("{} is a {}".format(self.name,self.description))


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




#player
class player(gameobject):
    def __init__(self,name,description,location):
        self.name = name
        self.description = description
        self.interactables = []
        self.location = location
        self.knowlage = []
    def whereami(self):
        gameobjects[self.location].describe()

    def cur_pos_exits(self):
        gameobjects[self.location].describe_exits()

    def move(self, key):
        if key in gameobjects[self.location].conntections:
            self.location = key
            print("You have moved to {}!".format(key))

    def describe_visible(self):
        print("me:")
        self.describe()
        print("where i am:")
        self.whereami()
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

gameobjects = {
"johns room":room("johns room","room in which john lives",["hallway"],["key"]),
"hallway":room("hallway","corridor that connects to different parts of the house",["johns room"],[]),
"john":player("john", "representation of you in this world", "johns room"),
"key":carrable("key", "tool to open something", "johns room")
}
