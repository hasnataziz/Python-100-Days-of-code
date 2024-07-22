print('''          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/''')
print("Welcome to treasure Island!")
print("Your mission is to find the treasure")
left_right = input("You are at a crossroad . where do you want to go? type 'left or right'? ")
if left_right == "left":
    swim_wait = input("you come to lake. There is an island in the middle of the lake.\n type 'wait' to wait for the boat.\n type 'swim' to swim accross ")
    if swim_wait == "wait":
        red_yellow_blue = input("you arrive at the island unharmed.\n There is a house with three doors. one red, one yellow and one blue .\n which color do you choose ?")
        if red_yellow_blue == "yellow":
            print("You win")
        elif red_yellow_blue == "blue":
            print("eaten by beasts game over")
        elif red_yellow_blue == "red":
            print("Burned by fire game over")
        else:
            print("Game over")
    elif swim_wait == "swim":
        print("Attacked by trout Game over")
    else:
        print("Game over")
elif left_right == "right":
    print("fall into hole Game over")
else:
    print("Game over")