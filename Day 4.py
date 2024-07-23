import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
selction_your = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors?\n"))
all_diagram = [rock,paper,scissors]
your_decision = all_diagram[selction_your]
print("You choose\n" +your_decision )
random_computer = random.randint(0,len(all_diagram)-1)
computer_decison = all_diagram[random_computer]
print("Computer choose" + computer_decison)
if(selction_your == random_computer):
    print("Its Draw")
elif selction_your == 0 and random_computer == 1:
    print("computer won")
elif selction_your == 0 and random_computer == 2:
    print("You won")
elif selction_your == 1 and random_computer ==2:
    print("computer won")
elif selction_your == 2 and random_computer == 1:
    print("you won")
elif selction_your == 1 and random_computer == 0:
    print("You won")
else:
    print("wrong entry")
