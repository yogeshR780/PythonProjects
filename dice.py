import random
while True:
    chance = input("Enter the choice:(y/n)").lower()
    if chance == 'y':
        dice1 =random.randint(1,6)
        dice2= random.randint(1,6)
        print(f'({dice1},{dice2})')
    elif chance == 'n':
        print("thanks for visiting")
        break 
    else:
        print("Invalid Index")