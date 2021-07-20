import webbrowser
import random
def stats():
    print("Name:" + name)
    print("Breed:" + breed)
    print("Class:" + gameclass)
    print("Intelligence:", intel)
    print("Stealth:" , stealth)
    print("Inventory:", inventory)

inventory = ["nothing"]
#list.remove, list.append
 #setup starts here   
text = "CHARACTER"
from PIL import Image, ImageDraw, ImageFont
import numpy as np
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getsize(text)
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ','#'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print( "\n".join(strings))
gameclass = "none"
breed = "none"
print("You wake in a dark room. The only thing in the nearby area is a glowing form, speaking to you from the void.")
print("--Greetings, traveler. I'm here to only ask you a few questions.--")
print("You don't answer. It doesn't need you to.")
print("This adventure runs largely off dice rolls and stat checks. To get a bonus to rolls or checks, you can pick a class")
print("To choose, type the letter in front of your choice.")
print("Available classes are [A] Warrior, which gives you a +2 to all dice rolls but -1 to all stat checks, [B] Wizord, which gives the enemy -1 to all rolls, [C] Computer Programmer, which gives +2 to Intelligence checks, and [D] Theif, a class that adds +2 to stealth but -1 to Intelligence since the class name is misspelled. ")
gameclass = input("Which class would you like?")
print(gameclass)
if gameclass == "A" or gameclass == "a":
    gameclass = "Warrior"
    intel = 0
    stealth = 0
    health = 100
elif gameclass == "B" or gameclass =="b":
    gameclass = "Wizord"
    intel = 1
    stealth = 1
    health = 80
elif gameclass == "C" or gameclass =="c":
    gameclass = "Programmer"
    intel = 3
    stealth = 1
    health = 100
else:
    gameclass= "Theif"
    intel = 0
    stealth = 3
    health = 80

print("Your Class has been set to " + gameclass + ".")

print("Next you need to pick a race/species for your character! The options are:")
print("[A] Boring. They're humans. No change. This is a very boring race.")
print("[B] Catfolk. You are fluffy and pretty. You also have claws and go purr purrrr.")
print("[C] Horse. You are an intelligent horse that for some reason has hands.")
print("[D] Walmart cashier. You're a being from another reality, which is what Walmart is.")
print("[E] Rat with a greataxe. Its a rat with a greataxe")
print(["[F] Basketball Player. As is common knowledge, all basketball players are secretly rabbits."])
breed = input("Pick!")
if breed == "A" or breed == "a":
    breed = "human"
elif breed == "B" or breed =="b":
    breed = "catfolk"
elif breed == "C" or breed =="c":
    breed = "horse"
elif breed == "D" or breed =="d":
    breed = "cashier"
elif breed == "E" or breed =="e":
    breed = "rat"
else:
    breed = "basketball player"

print("At any time you can type 'stats' to see your stats.")

print("More stuff! Setup is hard.")

gender = input("Are you [A] a male [B] a female or [C] I TRANSCEND ALL GENDER")
if gender == "A" or gender == "a":
    print("Poggers.")
    gender = "male"
    p1 = "he"
    p2 = "him"
elif gender == "B" or gender =="b":
    print("OwO")
    gender = "female"
    p1 = "she"
    p2 = "her"
else:
    print("ASCENSION")
    gender = "other"
    p1 = "they"
    p2 = "them"

print("Hm. That may be it for setup! ")
nextthing = input("Now you need to imput a picture of your lovely character!")
if nextthing == "no" or nextthing == "No":
    print("I get it.")
elif nextthing == "stats" or nextthing == "Stats":
    print("Breed:" + breed)
    print("Class:" + gameclass)
    print("Intelligence:",  intel)
    print("Stealth:", stealth)
else:
    print("No problem. You don't have to.")
    print("I'll draw them FOR you! ;)")
    if breed == "human":
        webbrowser.open("https://preview.redd.it/6n8cjy03q5z21.png?auto=webp&s=bc215154b02ca2ace9d4096320c4c4a9f7db1e40")
        print("You look beautiful!")
    elif breed == "catfolk":
        webbrowser.open("https://c8.alamy.com/comp/X0WFHF/white-cat-standing-on-two-legs-X0WFHF.jpg")
        print("You look beautiful!")
    elif breed == "horse":
        webbrowser.open("https://i.pinimg.com/originals/b0/1a/56/b01a56473801953acff4e2a1caeec20a.jpg")
        print("What a lovely face!")
    elif breed == "cashier":
        webbrowser.open("https://townsquare.media/site/71/files/2021/02/Newburgh-Walmart.jpg?w=980&q=75")
        print("Lovely!")
    elif breed == "rat":
        webbrowser.open("https://as1.ftcdn.net/jpg/03/19/64/60/500_F_319646061_jo3en7bXk8IeKiCh8E3WwO1vfsmtBKHl.jpg")
        print("Powerful!")
    else:
        webbrowser.open("https://shop.wilson.com/media/catalog/product/cache/38/image/9df78eab33525d08d6e5fb8d27136e95/c/7/c7dd204a5c8de77cfa036eb232a5e64659c7b2e1_WTB0516_Evolution_v2.jpg")
        print("Your best friend.")

print("Time to do the finisher for your lovely character.")
name = input("Now, what's the name of your lovely traveler?")
if name == "bronzewing":
    print("HEY! THATS... you know what, go ahead")
else: 
    print("A lovely name.")

print("Your final stats are as follows.")
stats()

import webbrowser
import random
text = "WELCOME"
from PIL import Image, ImageDraw, ImageFont
import numpy as np
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getsize(text)
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ','#'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print( "\n".join(strings))

#game starts here
print("You end up in a dark forest. Nothing is around as far as the eye can see.")
print("Except trees.")
nexthing = input("You can [A] Punch the tree or [B] Walk around.")

    



