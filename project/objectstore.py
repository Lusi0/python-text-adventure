from game_object import A_object, dialog, gameobject, interactables, person, carrable, room, locked_room, player





gameobjects = {
"sleeping quarters":room("sleeping quarters","your sleeping quarters are well kept, the drapes are drawn and light shines in. The door is open to the upper floor stairway",["upper floor stairway"],["key"]),
"upper floor stairway":room("upper floor stairway","the second floor of the stairway. The door is open to your sleeping quarters",["sleeping quarters","lower floor stairway"],[]),
"lookout":room("lookout","the lookout is a large and well maintained lookout, it is well lit and you can see the garden and much of the land that lies beyond the gate",["upper floor stairway"],[]),
"lower floor stairway":room("lower floor stairway","the first floor of the stairway",["armory","upper floor stairway"],[]),
"armory":room("armory","the armory is a place where you can find weapons and armor",["lower floor stairway"],[]),
"entrance":room("entrance","the entrance to the castle",["lower floor stairway","inner sanctum"],[]),
"inner sanctum":room("inner sanctum","you find yourself surrounded by the castles many amenities",["entrance", "garden", "swordsmith"],[]),
"garden":room("garden","the garden is a large and well maintained garden, you can see many plants and animals. The light in the lookout is visiable from here",["inner sanctum", "tea room"],[]),
"tea room":room("tea room","the tea room is a place where you can find tea and water",["garden"],[]),
"swordsmith":room("swordsmith","the swordsmith is a place where you can find weapons and armor",["inner sanctum"],[]),
"me":player("me", "me is you, silly!", "sleeping quarters", ["0"]),
"kate":person("kate","person who lives in your home","kates room",[dialog("0","1","who are you?","I am kate, I live in this room!")])
}