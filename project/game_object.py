import random

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
        gameobjects[self.reward].attach(player.name)
        print("You have received {}!".format(self.reward))

class gameobject(A_object):
    def __init__(self,name,description,location):
        self.name = name
        self.description = description

    def describe(self):
        print("{}".format(self.description))

class dialog_purchase(dialog):
    def __init__(self, knowlage_req, knowlage_given, player_dialog, response, item, price):
        super().__init__(knowlage_req, knowlage_given, player_dialog, response)
        self.item = item
        self.price = price
    def purchase(self, player):
        if "bags of rice" in player.interactables:
            if gameobjects["bags of rice"].quantity > self.price:
                gameobjects["bags of rice"].quantity -= self.price
                gameobjects[self.item].attach(player.name)
                print("You have received {}!".format(self.item))
            else:
                print("You do not have enough rice to purchase this item.")



#interactables
class interactables(gameobject):
    def __init__(self,name,description,location):
        self.name = name
        self.description = description

class person(interactables):
    def __init__(self,name,description,location,dialog,interactables,health):
        self.name = name
        self.description = description
        self.location = location
        self.dialog = dialog
        self.interactables = interactables
        self.health = health

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

    def move_(self, object):
        gameobjects[self.location].interactables.remove(self.name)
        gameobjects[object].interactables.append(self.name)
        self.location = object

    def death(self):
        for item in self.interactables:
            gameobjects[item].attach(self.location)
        self.move_("afterlife")
        print("{} has died".format(self.name))
        
    
    def check_health(self):
        if self.health <= 0:
            self.death()

class combatent(person):
    def __init__(self,name,description,location,dialog,health,interactables, punishment,reward):
        self.name = name
        self.description = description
        self.location = location
        self.dialog = dialog
        self.health = health
        self.interactables = interactables
        self.punishment = punishment
        self.reward = reward

    def attack(self):
        total_damage = 0
        for item in self.interactables:
                if type(gameobjects[item]) is weapon:
                    total_damage += gameobjects[item].attack
        return total_damage

    def defend(self):
        total_damage = 0
        for item in self.interactables:
                if type(gameobjects[item]) is armor:
                    total_damage += gameobjects[item].defence
        return total_damage
    

class art_minigame(interactables):
    def __init__(self,name,description,location,propmt1,choices1,correct1,propmt2,choices2,correct2,propm3,choices3,correct3):
        self.name = name
        self.description = description
        self.location = location
        self.part1 = (propmt1,choices1,correct1)
        self.part2 = (propmt2,choices2,correct2)
        self.part3 = (propm3,choices3,correct3)
        self.played = False

        

    def play(self,player):
        if self.played == False:
            print("You are about to play minigame about making art. You will be given three questions. \nYou will be given a score at the end. \nYour art peices quality will be determined by your choices \nGood luck!")
            score = 0
            for part in [self.part1,self.part2,self.part3]:
                print("{}".format(part[0]))
                for count,choice in enumerate(part[1]):
                    print("{}: {}".format(count,choice))
                answer = input(">")
                if answer == part[2]:
                    score += 1
                input("Press Enter to continue \n>")
            score = score*2 + random.randint(0,4)
            print("you show your painting to a nearby traveler and he says its a {}/10".format(score))
            
            if "bags of rice" in player.interactables:
                if score == 10:
                    print("You have received 4 bags of rice!")
                    gameobjects["bags of rice"].change_amount(4)
                elif score >= 7:
                    print("You have received 3 bags of rice!")
                    gameobjects["bags of rice"].change_amount(3)
                elif score > 4:
                    print("You have received 2 bags of rice!")
                    gameobjects["bags of rice"].change_amount(2)
                else:
                    print("You have received 1 bag of rice!")
                    gameobjects["bags of rice"].change_amount(1)
            else:
                print("You forgot your rice carrier, he can't pay you for the painting!")
            self.played = True
        else:
            print("You have already played this minigame.")

class carrable(interactables):
    def __init__(self,name,description,location):
        self.name = name
        self.description = description
        self.location = location

    def attach(self, object):
        gameobjects[self.location].interactables.remove(self.name)
        gameobjects[object].interactables.append(self.name)
        self.location = object

class stackable(carrable):
    def __init__(self,name,description,location,amount):
        self.name = name
        self.description = description
        self.location = location
        self.amount = amount
    
    def describe(self):
        print("{} {}".format(self.amount,self.description))

    def change_amount(self, change):
        self.amount += change

class weapon(carrable):
    def __init__(self,name,description,location,attack):
        self.name = name
        self.description = description
        self.location = location
        self.attack = attack

class armor(carrable):
    def __init__(self,name,description,location,defence):
        self.name = name
        self.description = description
        self.location = location
        self.defence = defence


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

class combat_room(room):
    def __init__(self, name, description, conntections, interactables, enemy):
        self.name = name
        self.description = description
        self.conntections = conntections
        self.interactables = interactables
        self.enemy = enemy
        self.finished = False
    def combat_start(self, player):
        print("You have encountered {}!".format(gameobjects[self.enemy].name))
        while gameobjects[self.enemy].health > 0 and player.health > 0:
            print("{} health: {}".format(gameobjects[self.enemy].name, gameobjects[self.enemy].health))
            print("{} health: {}".format(player.name, player.health))
            print("What will you do? ")
            armor = 0
            player_choice = None
            while player_choice not in ["attack", "defend", "exit"]:
                player_choice = input(">")
                if player_choice == "attack":
                    damage = player.attack()
                    gameobjects[self.enemy].health -= damage
                    print("You attacked {} for {}!".format(gameobjects[self.enemy].name, damage))
                elif player_choice == "defend":
                    armor = player.defend()
                elif player_choice == "exit":
                    print("You have exited the combat")
                    if "bags of rice" in player.interactables:
                        if gameobjects["bags of rice"].amount-gameobjects[self.enemy].punishment > 0:
                            gameobjects["bags of rice"].change_amount(-gameobjects[self.enemy].punishment)
                        else:
                            gameobjects["bags of rice"].change_amount(-gameobjects["bags of rice"].amount)
                        print("You have lost {} bags of rice".format(gameobjects[self.enemy].punishment))
                    else:
                        print("You forgot to grab the rice by the front gate! Now what will you pay the shogun with?")
                    self.finished = True
                    break
                elif player_choice == "help":
                    print("attack - attack the enemy")
                    print("defend - defend yourself")
                    print("exit - exit combat")
                else:
                    print("Invalid input")
            if self.finished:
                break
            if gameobjects[self.enemy].health >= 1:
                attack = gameobjects[self.enemy].attack()
                if attack - armor > 0:
                    player.health -= attack - armor
                    print("{} attacked you for {}!".format(gameobjects[self.enemy].name, attack))
                else:
                    print("{} tried to attack you but their attacks bounced off your armor!".format(gameobjects[self.enemy].name))
            if gameobjects[self.enemy].health <= 0:
                print("You have defeated {}!".format(gameobjects[self.enemy].name))
                gameobjects[self.enemy].death()
                self.finished = True
                if player.health < 50:
                    player.health = 50
                if "bags of rice" in player.interactables:
                    gameobjects["bags of rice"].change_amount(gameobjects[self.enemy].reward)
                    print("You have gained {} bags of rice!".format(gameobjects[self.enemy].reward))
                else:
                    print("You forgot your rice bundle at home and don't have a way to carry the rice you found on him")
                break
            else:
                if player.health <= 0:
                    print("You have been defeated!")
                    self.finished = True
                    player.health = 50
                    if "bags of rice" in player.interactables:
                        if gameobjects["bags of rice"].amount-gameobjects[self.enemy].punishment > 0:
                            gameobjects["bags of rice"].change_amount(-gameobjects[self.enemy].punishment)
                        else:
                            gameobjects["bags of rice"].change_amount(-gameobjects["bags of rice"].amount)
                        print("You have lost {} bags of rice".format(gameobjects[self.enemy].punishment))
                    else:
                        print("You forgot to grab the rice by the front gate! Now what will you pay the shogun with?")
                    break

#player
class player(gameobject):
    def __init__(self,name,description,location,knowlage):
        self.name = name
        self.description = description
        self.interactables = []
        self.location = location
        self.knowlage = knowlage
        self.health = 100
        self.devmode = False

    def paint(self, key):
        if key in gameobjects[self.location].interactables and "art supplies" in self.interactables:
            gameobjects[key].play(self)
        else:
            print("You don't have the tools to paint that")

    def cur_pos_exits(self):
        gameobjects[self.location].describe_exits()

    def whereami(self):
        gameobjects[self.location].describe()

    def health(self):
        print("{} health: {}".format(self.name, self.health))

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
        if type(gameobjects[self.location]) == combat_room and gameobjects[self.location].finished == False:
            gameobjects[self.location].combat_start(self)

    def forcemove(self, key):
        if key in gameobjects:
            self.location = key
            gameobjects[key].describe()
            print("You have moved to {}!".format(key))
        if type(gameobjects[self.location]) == combat_room and gameobjects[self.location].finished == False:
            gameobjects[self.location].combat_start(self)



    def describe_visible(self):
        if len(gameobjects[self.location].interactables) > 0:
            print("You see,")
            for item in gameobjects[self.location].interactables:
                print(item)
        else:
            print("You see nothing of interest")
        
    def inventory(self):
        if len(self.interactables) > 0:
            print("You have:")
            for item in self.interactables:
                print(item)
        else:
            print("You have nothing")


    def grab(self, key):
        if key in gameobjects[self.location].interactables:
            if type(gameobjects[key]) is carrable or type(gameobjects[key]) is weapon or type(gameobjects[key]) is armor or type(gameobjects[key]) is stackable: 
                gameobjects[key].attach(self.name)
                print("you picked up {}".format(key))
            else:
                print("cannot pick up {}".format(key))

    def forcegrab(self, key):
        if key in gameobjects:
            if type(gameobjects[key]) is carrable or type(gameobjects[key]) is weapon or type(gameobjects[key]) is armor or type(gameobjects[key]) is stackable:
                gameobjects[key].attach(self.name)
                print("you picked up {}".format(key))


    def drop(self, key):
        if key in self.interactables:
            gameobjects[key].attach(self.location)
            "you dropped {}".format(key)

    def talk(self, key):
        if key in gameobjects[self.location].interactables:
            if type(gameobjects[key]) == person:
                return gameobjects[key].listresponses(self.name)

    def attack(self):
        total_damage = 0
        for item in self.interactables:
                if type(gameobjects[item]) is weapon:
                    total_damage += gameobjects[item].attack
        return total_damage

    def defend(self):
        total_damage = 0
        for item in self.interactables:
                if type(gameobjects[item]) is armor:
                    total_damage += gameobjects[item].defence
        return total_damage

    def hostile_action(self, key):
        if key in gameobjects[self.location].interactables:
            if type(gameobjects[key]) == person:
                gameobjects[key].health -= self.attack()
                gameobjects[key].check_health()


    
    


gameobjects = {
"sleeping quarters":room("sleeping quarters","your sleeping quarters are well kept, the drapes are drawn and light shines in. The door is open to the stairway",["stairway"],["note"]),
"stairway":room("stairway","the second floor of the stairway. there are stairs leading down to the landing and up to the lookout. the door to your sleeping quarters is open.",["sleeping quarters","landing","lookout"],[]),
"lookout":room("lookout","the lookout is a large and well maintained lookout, it is well lit and you can see the garden and much of the land that lies beyond the gate",["stairway","garden"],["art supplies"]),
"landing":room("landing","the first floor of the castle",["armory","stairway","inner sanctum"],[]),
"armory":locked_room("armory","the armory is a place where you can find weapons and armor",["landing"],["armor"],"armory key"),
"inner sanctum":room("inner sanctum","you find yourself surrounded by the castles many amenities",["landing", "garden", "smith", "front gate"],[]),
"garden":room("garden","The garden has been planned to look unplanned. A babbling brook cuts through, its water flowing peacefully. The light from the lookout is visiable from here",["inner sanctum", "tea room"],[]),
"tea room":room("tea room","the tea room is a place where you can find tea and water",["garden"],["father"]),
"smith":room("smith","the smith is a place where you can find the swordsmith",["inner sanctum"],["swordsmith", "sword"]),
"me":player("me", "me is you, silly!", "sleeping quarters", ["0"]),
"swordsmith":person("swordsmith","the swordsmith is a person who sells swords","smith",[dialog("0","0","who are you?","I am the swordsmith, I sell swords!"), dialog_reward("1","0","Where is my armor?", "Your armor is stored in the armory here use this key!","armory key")], ["armory key"],5),
"father":person("father","Your father is an honorable Dainmyo he looks like he is prepared to talk with you","tea room",[dialog_reward("0","1","You called for me?","As the shogun has most generously gifted us this domain from the defeated, I would like you to personally deliver our first rice tax to Edo. Collect your armor, sword, and art supplies and meet the rest of the party at the front gate of the castle. You will take the Tokaido route past Mt. Fuji.","another note")], ["another note"],5),
"note":carrable("note","A summons from your father, the Daimyo, to meet him in the tea room.","sleeping quarters"),
"another note":carrable("another note","supply list sword is currently with the swordsmith and the art supplies are currently in the lookout","father"),
"god sword":weapon("god sword","a god sword","afterlife",50),
"afterlife":room("afterlife","this is where the souls that have been claimed rest",[],["god sword"]),
"armory key":carrable("armory key","the key to the armory","swordsmith"),
"sword":weapon("sword","the sword","smith",10),
"art supplies":carrable("art supplies","the art supplies","lookout"),
"front gate":room("front gate","the front gate is a large gate that leads to the castle",["inner sanctum", "trail head"],["bags of rice","servent"]),
"servent":person("servent","the servant is a person who sells horses and carts","front gate",[dialog("0","0","who are you?","I am the servant, I am here to see you off!"), dialog_reward("1","0","Unlock the gate.", "As you wish here is the key to the gate.","front gate key")], ["front gate key"],5),
"front gate key":carrable("front gate key","the key to the front gate","servent"),
"trail head":locked_room("trail head","the trail head is a place where you can find the supplies needed to complete the quest",["front gate", "outskirts of nayoya"],[],"front gate key"),
"armor":armor("armor","the armor","armory",10),
"bandit sword":weapon("bandit sword","the bandit sword","bandit",10),
"bandit armor":armor("bandit armor","the bandit armor","bandit",3),
"bandit":combatent("bandit","you have the feeling this individual is not worthy of blind trust","outskirts of nayoya",[], 30, ["bandit sword", "bandit armor"],2,1),
"outskirts of nayoya":combat_room("outskirts of nayoya","The newly rebuilt Castle Nagoya stands in the distance. But outside of the walls of the city, shady figures lurk along the trail.",["trail head","city of nayoya"],["bandit"],"bandit"),
"bags of rice":stackable("bags of rice","bags of rice","front gate",10),
"city of nayoya":room("city of nayoya","The city of Nagoya is a large city, with many buildings and a large marketplace",["outskirts of nayoya","marketplace of nayoya", "seaside passage"],["nayoyian guard"]),
"marketplace of nayoya":room("marketplace of nayoya","The marketplace is a large marketplace, with many shops",["city of nayoya"],["nayoyian swordsmith", "nayoyian armorsmith"]),
"nayoyian swordsmith":person("nayoyian swordsmith","the nayoyian swordsmith is a person who sells swords","marketplace of nayoya",[dialog_purchase(0,0,"purchase nayoyian sword for 2 bages of rice","right! here you are", "nayoyian sword", 2)], ["nayoyian sword"],5),
"nayoyian sword":weapon("nayoyian sword","the nayoyian sword","nayoyian swordsmith",12),
"nayoyian armorsmith":person("nayoyian armorsmith","the nayoyian armorsmith is a person who sells armor","marketplace of nayoya",[dialog_purchase(0,0,"purchase nayoyian armor for 2 bages of rice","right! here you are", "nayoyian armor", 2)], ["nayoyian armor"],5),
"nayoyian armor":armor("nayoyian armor","the nayoyian armor","nayoyian armorsmith",12),
"seaside passage":room("seaside passage","You find yourself by a beautiful view of the sea. The waves crash rhythmically against the shore, wild horses graze on the grass just by the shore. You are inspired to make an ink painting of this scene!",["city of nayoya", "gate of edo"],["view of ocean"]),
"view of ocean":art_minigame("view of ocean","art making minigame","seaside passage","the first thing you notice about the view is the fishing vessels in the water",["paint them fighting against the waves","paint them sitting on tranqil water", "paint them being flipped overboard"], "0", "next you look to the great mountain fuji", ["paint it to fill the entire background", "have it tucked nicely under the incoming waves", "don't inculde it as it"], "1","the last thing you see it the way the waves crash", ["have the waves use a pattern to indicate the movement of the foam", "use solid white shapes at the top of the waves to indicate foam", "do not include foam int the final painting"],"0"),
"gate of edo":room("gate of edo","You have arrived at Edo, proceed to the palace and you will meet the shogun himself!",["seaside passage", "edo palace"],[]),
"edo palace":room("edo palace","You have arrived at the edo palace, you will meet the shogun here!",["gate of edo"],[]),
}


# guarded_cities = {"city of nayoya":combat_room("city of nayoya","The main square is now flooded with gaurds you should've condsidered the consiquences of your actions",["outskirts of nayoya","marketplace of nayoya","seaside passage"],[],"bandit")}
# "nayoyian guard":combatent("nayoyian","a strong a suitable warrior that will defend the people of nayoya","city of nayoya",[dialog(0,0,"who are you?","I am apart of the proud nayoyian guard")], 30, ["nayoyian guard sword", "nayoyian guard armor"],2,1),
# "nayoyian guard armor":armor("nayoyian guard armor","the nayoyian guard armor","nayoyian guard",12),
# "nayoyian guard sword":weapon("nayoyian guard sword","the nayoyian guard sword","nayoyian guard",12),