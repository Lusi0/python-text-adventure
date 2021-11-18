

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
class dialog_reward(dialog):
    def __init__(self, knowlage_req, knowlage_given, player_dialog, response, reward):
        super().__init__(knowlage_req, knowlage_given, player_dialog, response)
        self.reward = reward
    def give_reward(self, player):
        player.interactables.append(self.reward)
        gameobjects[self.reward].attach(player.name)
        print("You have received {}!".format(self.reward))

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
                if type(dialog) == dialog_reward:
                    dialog.give_reward(player)
                print("here")

class carrable(interactables):
    def __init__(self,name,description,location):
        self.name = name
        self.description = description
        self.location = location

    def attach(self, object):
        gameobjects[self.location].interactables.remove(self.name)
        gameobjects[object].interactables.append(self.name)
        self.location = object
class combatent(person):
    def __init__(self,name,description,location,dialog,health,attack):
        self.name = name
        self.description = description
        self.location = location
        self.dialog = dialog
        self.health = health
        self.attack = attack
        self.defense = defense
    def attack(self, player):
        player.health -= self.attack

#rooms
class room(gameobject):
    def __init__(self,name,description,conntections,interactables):
        self.name = name
        self.description = description
        self.conntections = conntections
        self.interactables = interactables
    def describe_exits(self):
        for room in self.conntections:
            print(room)
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
        self.health = 100

    def cur_pos_exits(self):
        gameobjects[self.location].describe_exits()

    def whereami(self):
        gameobjects[self.location].describe()

    def move(self, key):
        if key in gameobjects[self.location].conntections:
            if type(gameobjects[key]) == locked_room:
                if gameobjects[key].key in self.interactables:
                    self.location = key
                    gameobjects[key].describe()
                    print("You have moved to {}!".format(key))
                else:
                    print("You need a key to get in there!")
            else:
                self.location = key
                gameobjects[key].describe()
                print("You have moved to {}!".format(key))
        else:
            print("You can't go there!")



    def describe_visible(self):
        if len(gameobjects[self.location].interactables) > 0:
            print("You see,")
            for item in gameobjects[self.location].interactables:
                print(item)
        else:
            print("You see nothing of interest")
        
        


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
    
    def damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("You have died")
            exit()
        else:
            print("You have {} health left".format(self.health))


gameobjects = {
"sleeping quarters":room("sleeping quarters","your sleeping quarters are well kept, the drapes are drawn and light shines in. The door is open to the stairway",["stairway"],["note"]),
"stairway":room("stairway","the second floor of the stairway. there are stairs leading down to the landing and up to the lookout. the door to your sleeping quarters is open.",["sleeping quarters","landing","lookout"],[]),
"lookout":room("lookout","the lookout is a large and well maintained lookout, it is well lit and you can see the garden and much of the land that lies beyond the gate",["stairway","garden"],["art supplies"]),
"landing":room("landing","the first floor of the castle",["armory","stairway","inner sanctum"],[]),
"armory":locked_room("armory","the armory is a place where you can find weapons and armor",["landing"],[],["armory key"]),
"inner sanctum":room("inner sanctum","you find yourself surrounded by the castles many amenities",["landing", "garden", "smith", "the front gate"],[]),
"garden":room("garden","The garden has been planned to look unplanned. A babbling brook cuts through, its water flowing peacefully. The light from the lookout is visiable from here",["inner sanctum", "tea room"],[]),
"tea room":room("tea room","the tea room is a place where you can find tea and water",["garden"],["father"]),
"smith":room("smith","the smith is a place where you can find the swordsmith",["inner sanctum"],["swordsmith", "sword"]),
"me":player("me", "me is you, silly!", "sleeping quarters", ["0"]),
"the front gate":room("the front gate","the front gate is a large gate that leads to the castle",["inner sanctum","the castle courtyard"],[]),
"swordsmith":person("swordsmith","the swordsmith is a person who sells swords","smith",[dialog("0","0","who are you?","I am the swordsmith, I sell swords!"), dialog_reward("1","0","Where is my armor?", "Your armor is stored in the armory here use this key!","armory key")]),
"father":person("father","Your father is an honorable Dainmyo he looks like he is prepared to talk with you","tea room",[dialog_reward("0","1","You called for me?","As the shogun has most generously gifted us this domain from the defeated, I would like you to personally deliver our first rice tax to Edo. Collect your armor, sword, and art supplies and meet the rest of the party at the front gate of the castle. You will take the Tokaido route past Mt. Fuji.","another note")]),
"note":carrable("note","A summons from your father, the Daimyo, to meet him in the tea room.","sleeping quarters"),
"another note":carrable("another note","supply list sword is currently with the swordsmiht and the art supplies are currently in the lookout","floatingroom"),
"floatingroom":room("floatingroom","the floating room is a place where you can find the supplies needed to complete the quest",[],["another note", "armory key","front gate key","armory key"]),
"armory key":carrable("armory key","the key to the armory","floatingroom"),
"sword":carrable("sword","the sword","smith"),
"art supplies":carrable("art supplies","the art supplies","lookout"),
"the front gate":room("the front gate","the front gate is a large gate that leads to the castle",["inner sanctum"],["horse and cart","servent"]),
"servent":person("servent","the servant is a person who sells horses and carts","the front gate",[dialog("0","0","who are you?","I am the servant, I am here to see you off!"), dialog_reward("1","0","Unlock the gate.", "As you wish here is the key to the gate.","front gate key")]),
"front gate key":carrable("front gate key","the key to the front gate","floatingroom"),
"trail head":locked_room("trail head","the trail head is a place where you can find the supplies needed to complete the quest",["the front gate"],[],["front gate key"]),
"armor":carrable("armor","the armor","armory"),
}

