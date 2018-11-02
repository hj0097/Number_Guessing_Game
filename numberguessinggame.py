print("hey welcome to our game number guess :test ur luck")

import random

number = random.randrange(1, 100)
tries = 0
num2 = 0

p = str(input("pls select if u wanna play or not [y,n] : "))

if p == "n":
    print("well have a nice time ,goodbye")

elif p == "y":
    print(" lets start")


    while num2 != number:
        while True:
            try:
                num2 = int(input("pls enter a number between 1 and 100 : "))
                break
            except Exception:
                print("enter a number : ")
        tries = tries + 1

        if num2 > number:
            print("guess lower")
        elif num2 < number:
            print("guess higher")
        else:
            print("hurrey ! u won")




    print(" u tried :", tries, "times" )

else:
    print("wrong input typed. restart the game")





