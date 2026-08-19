import random

choices=('r','p','s')
emoji = {'r':'🪨','s':'✂️','p':'📃'}

while True:
 user_choice=input("Rock, Paper , Scissors(r,p,s) : ").lower()
 if user_choice not in choices:
   print("Please Enter a valid option..")
   continue
 
 computer_choice = random.choice(choices)
 print(f"You choose : {emoji[user_choice]}")
 print(f'Computer Choose : {emoji[computer_choice]}')

 if user_choice == computer_choice:
   print("Tied")
 elif (
    (user_choice == 'r' and computer_choice == 's') or
    (user_choice == 's' and computer_choice == 'p') or 
    (user_choice == 'p' and computer_choice == 'r')):
    print("You win!!!!")
 else:
    print("You Lost..")

 continue_game = input("Do You Want TO Continue(y/n) : ").lower()
 if continue_game == 'y':
   print("Okk I Gotuuu 😁..")
 elif continue_game == 'n':
    print("Bye bro...🙋🏽‍♂️")
    break
 else:
   print("Common Bro It's Just Yes & No 🤷‍♂️")
   print("I'll Consider it as no.🙋🏽‍♂️")
   break

