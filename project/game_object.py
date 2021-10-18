class gameobject:
    def __init__(self,identifier,name,description):
        self.identifier = identifier
        self.name = name
        self.description = description

    def describe(self):
        print("{} is a {}".format(self.name,self.description))


#interactables
class interactables(gameobject):
    def __init__(self,identifier,name,description):
        self.identifier = identifier
        self.name = name
        self.description = description

class person(interactables):
    def __init__(self,identifier,name,description,dialog):
        pass

class carrable(interactables):
    def __init__(self,identifier,name,description):
        pass


#rooms
class room(gameobject):
    def __init__(self,identifier,name,description,exits,interactables):
        pass


#player
class player(gameobject):
    pass
