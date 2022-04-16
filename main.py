import random

def game(comp,player):
    if comp == 's':
        if player == 'w':
            print("Computer has win...")
        elif player == 'g':
            print("Congratulations, You have won !")
        elif player == 's':
            print("It's a draw")
        else:
            print("Please enter a valid option")
    if comp == 'w':
        if player == 'w':
            print("It's a draw")
        elif player == 'g':
            print("Computer has win...")
        elif player == 's':
            print("Congratulations, You have won !")
        else:
            print("Please enter a valid option")
    if comp == 'g':
        if player == 'w':
            print("Congratulations, You have won !")
        elif player == 'g':
            print("It's a draw.")
        elif player == 's':
            print("Computer wins.....")
        else:
            print("Please enter a valid option")
    
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
print("Computer Turn : Snake(s), Water(w) or Gun(g) ?")
player = input("Your Turn : Snake(s), Water(w) or Gun(g) ?")
print("you choose",player)
print("computer choose",comp)
game(comp,player)

