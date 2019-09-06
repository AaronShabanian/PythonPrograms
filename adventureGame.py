import random
game=0
attempt=0
wrong=0
print("Welcome to the entrance of the Mansion")
print("""Blueprint
Floor 1: Living room, Kitchen, elevator
Floor 2: Maid Bedroom, Master Bedroom, balcony, elevator
Floor 3: Movie theater, elevator
""")
floor=1
while game==0:
    while floor==1:
        print("You are currently on floor ",floor," of the mansion. You can only go to rooms on your floor as listed in the blueprint. ")
        room=input("Would you like to go to the living room, kitchen or elevator:  ").lower()
        if room=="elevator":
            floor=input("What floor would you like to go to? ")
            floor=int(floor)
        elif room=="kitchen":
            print("Welcome to the kitchen, You were hungry and decided to have a snack")
        elif room=="living room":
                if attempt==0:
                    print("Welcome to the living room. Just kidding. The owner wants you to leave this room immediately. If you come here again you will die ")
                    attempt=attempt+1
                else:
                    print("You were warned. You have been stabbed to your death by the owner of the household. You loose ")
                    floor=4
                    game=1
        else:
            print("That is not a valid room on this floor, You loose ")
            floor=4
            game=1
        death=random.randint(1,100)
        if death==78:
            print("You have fallen and broke your neck dying ")
            game=1
            floor=4
    while floor==2:
        print("You are currently on floor ",floor," of the mansion. You can only go to rooms on your floor as listed in the blueprint. ")
        room=input("Would you like to go the the maid bedroom, master bedroom, balcony or elevator:  ").lower()
        if room=="elevator":
            floor=input("What floor would you like to go to? ")
            floor=int(floor)
        elif room=="maid bedroom":
            print("You find a paper with the code 5321 and wonder what that could mean. ")
        elif room=="master bedroom":
            print("You took a nap on the most comfortable bed you have ever been on")
        elif room=="balcony":
            print("You have found a bomb and see that there is a code to diffuse it and realize that you only have 3 attempts before it self destructs")
            code=input("What is the code to diffuse the bomb")
            if code=="5321":
                print("The bomb has been diffused. You win the game")
                floor=5
                game=1
            else:
                wrong=wrong+1
                if wrong<3:
                    print("wrong code you have been wrong ",wrong," times ")
                else:
                    print("wrong code. The bomb has exploded. You loose! ")
                    game=1
                    floor=4
        death=random.randint(1,100)
        if death==100:
            print("You have randomly fall out of a window")
            floor=4
            game=1
    while floor==3:
        print("You are currently on floor ",floor," of the mansion. You can only go to rooms on your floor as listed in the blueprint. ")
        room=input("Would you like to go to the movie theater or elevator:  ").lower()
        if room=="movie theater":
            "You watch a boring movie that lasts 2 hours and a bomb explodes the mansion killing you with it"
            game=1
            floor=4
        elif room=="elevator":
            floor=input("What floor would you like to go to? ")
            floor=int(floor)
        death=random.randint(1,100)
        if death==100:
            print("An asteroid randomly hits the mansion and you die")
            floor=4
            game=1
if floor==4:
    print("Your a looser")
if floor==5:
    print("YOUR A WINNER!!!")
