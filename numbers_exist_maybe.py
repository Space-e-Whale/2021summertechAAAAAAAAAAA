from random import randint

name = randint(1,100)
print(name)
print("oh no i dropped the answer")
guessed = "no"
smart = "yes"
turns = 0

while guessed == "no":
    guess = int(input("number pls 1-100\n"))
    if guess == name:
        turns += 1
        print("u good")
        guessed = "yes"
        print("it took u", turns , "turns")
        if smart == "yes":
            print("you get trophy")
        if smart == "no way":
            print("but ur still bad haha")
    elif guess > 100:
        print("NO!!!!!!!!!!!")
        turns += 1
        smart = "no way"
    elif guess < 0:
        print("WHAT NO THATS NOT IT")
        smart = "no way"
    elif guess > name:
        print("thats too high")
        turns += 1
    elif guess < name:
        print("thats too low")
        turns += 1
    
        
    else:
        print(":(")
        print("how did you even get here")

