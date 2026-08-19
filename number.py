import random
guess=random.randint(1,100)
while True:
    try:
        number=int(input("Enter the number between 1 to 100 : "))

        if number<1 or number>100:
            print("You know there should be number between 1 to 100 then why are you doing like that...")
            continue

        if number>guess:
            print("value Too High")
        elif number<guess:
            print("Value Too Low")
        else:
            print("congraulation!!!!!")
            break
    except ValueError:
        print("Please Enter the Number..")
