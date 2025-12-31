import random

def game(comp, user):
    if comp == user:
        return None

    if comp == 's':
        if user == 'w':
            return False
        elif user == 'g':
            return True

    if comp == 'w':
        if user == 'g':
            return False
        elif user == 's':
            return True

    if comp == 'g':
        if user == 's':
            return False
        elif user == 'w':
            return True


print("Computer turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'

user = input("Your turn: Snake(s) Water(w) or Gun(g)? ")

result = game(comp, user)

print("Computer chose:", comp)
print("You chose:", user)

if result is None:
    print("🤝 Game Tie!")
elif result:
    print("🎉 You Win!")
else:
    print("😢 You Lose!")
