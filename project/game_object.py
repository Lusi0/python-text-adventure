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
        self.description = location
        self.location = location


#rooms
class room(gameobject):
    def __init__(self,name,description,passages,interactables):
        self.name = name
        self.description = description
        self.passages = passages
        self.interactables = interactables
    def describe_exits(self):
        for exit in self.passages:
            print(gameobjects[gameobjects[exit].end].describe())


#passage
class passage(gameobject):
    def __init__(self,name,description,start,end):
        self.name = name
        self.description = description
        self.start = start
        self.end = end

#player
class player(gameobject):
    def __init__(self,name,description,location,inventory,knowlage):
        self.name = name
        self.description = description
        self.inventory = []

gameobjects = {
0:room("johns room","room in which john lives",[2],[]),
1:room("hallway","corridor that connects to different parts of the house",[3],[]),
2:passage("john_hallway_connector", "connects johns room to hallway", 0,1),
3:passage("hallway_john_connector", "connects hallway to johns room", 1,0)


}
