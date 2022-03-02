import random
print("\nCreated by \"Reza Rafiee\".05-Feb-22")
print("""This is a \"Hand Game\" called \"Rock,Paper,Scissors\"
Allowed movements : \n\"Rock\"\n\"Paper\"\n\"Scissors\"
Whoever \"beats the opponent for 3 Times\",Wins.""")
RandomNumber = random.randint(0, 2)
if RandomNumber == 0:
    ComputerMove = "Rock"
elif RandomNumber == 1:
    ComputerMove = "Paper"
elif RandomNumber == 2:
    ComputerMove = "Scissors"
Player_1_Name = input("\nEnter your name please : ").capitalize()
Player_2_Name = "System"
Answer = "Y"
while Answer == "Y":
    cp1 = 0
    cp2 = 0
    Go = input(f"""\nHey {Player_1_Name}
If you are ready,Type \"Go\" :\n""").capitalize()
    while Go != "Go":
        Go = input("Type \"Go\" please :\n").capitalize()
    while cp1 or cp2 != 3:
        print(f"\n{Player_1_Name} : {cp1}   |   {Player_2_Name} : {cp2}")
        Player_1 = input(f"{Player_1_Name} , Make your move : ").capitalize()
        print(f"{Player_2_Name} , Make your move : {ComputerMove}")
        Player_2 = ComputerMove
        if Player_1 == Player_2:
            print("DRAW...!!!\nTry again")
        elif Player_1 == "Rock":
            if Player_2 == "Paper":
                cp2 += 1
            elif Player_2 == "Scissors":
                cp1 += 1
        elif Player_1 == "Paper":
            if Player_2 == "Rock":
                cp1 += 1
            elif Player_2 == "Scissors":
                cp2 += 1
        elif Player_1 == "Scissors":
            if Player_2 == "Rock":
                cp2 += 1
            elif Player_2 == "Paper":
                cp1 += 1
        else:
            print("You didn't make an \"ALLOWED\" movement!!!\nTry again")
        if cp1 == 3:
            print(f"""\nFinal scores :
{Player_1_Name} : {cp1}   |   {Player_2_Name} : {cp2}""")
            print(f"\n{Player_1_Name} Wins...!!!")
            break
        elif cp2 == 3:
            print(f"""\nFinal scores :
{Player_1_Name} : {cp1}   |   {Player_2_Name} : {cp2}""")
            print(f"\n{Player_2_Name} Wins...!!!")
            break
    print("\nThanks for playing \U0001f60a\u2764\ufe0f")
    print("-----------------------")
    Answer = input("""Would you like to play again?
If YES,Type \"Y\"\nIf NOT,Type \"N\"\n""").capitalize()
    while Answer not in ("Y", "N"):
        Answer = input("Type \"Y\" or \"N\" please :\n").capitalize()
    if Answer == "N".capitalize():
        print("Thanks for playing , BYE \U0001f609\u2764\ufe0f")
