from sys import exit

#0
def start():

    print("You are sitting on straw bed in a dank and grimy dungeon cell. ")
    print("You hear a guard in heavy armour plod towards your cell. ")
    print("As he huffs and puffs past, you notice a slip of paper drop through")
    print("the bars of your cell.")
    inp = input("> ")
    sing(inp)
    if inp == ("Pick up paper"):
        the_message()
    else:
        dead("The paper blows away and you live the rest of your miserable"
              + " life in prison.")

#1.1
def the_message():

    print("You pick up the paper. It reads...")
    print("Cover your ears.")
    inp = input("> ")
    if inp == ("Cover ears"):
        cover_ears()
    else:
        not_cover_ears()

#1.2
def gig():
    print("You get teleported out of whatever shit you're doing. " +
          "You are David Bowie now. Do whatever the fuck you want.")

#2.1
def cover_ears():

    print("A loud explosion knocks you to the floor.")

#2.2
def not_cover_ears():

    print("A loud explosion knocks onto the floor and stuns you.")


#Function section

def dead(description):
    print(description, "Congrats.")
    exit()

def sing(inp):
    if inp == "sing":
        print("There's a star man waiting in the sky!")
        gig()
        exit()




#start

start()
