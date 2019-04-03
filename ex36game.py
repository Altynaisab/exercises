from sys import exit

def final_scene():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def duel_scene():
    print("Now, you have to defend yourself ! ")
    print("You must to beat your enemy to go furter .")
    print("How are you going to overcome him ?")
    duel_end = False

    while True:
        choice = input("> ")

        if choice == "hit in the arm":
            dead("Your enemy will beat you at all. ")
        elif choice == "give a blow to the chest":
            final_scene()
        else:
            print("Sorry, you didn't beat him at all.")

def hunting_scene():
    print("We are in the forest.")
    print("You have to catch your prey.")
    print("Who can you catch ?")

    choice = input("> ")

    if "Wolf" in choice:
        start()
    elif("Rabbit") in choice:
        dead("Well, it gonna take so much time.. You died.")
    else:
        hunting_scene()
def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("Hello, now you should take a weapon for pretect yourself. ")
    print("There are two types on weapon : SWORD and BOW.")
    print("Which one you will choose ?")

    choice = input ("> ")

    if choice == "SWORD":
        duel_scene()
    elif choice == "BOW":
        hunting_scene()
    else:
        dead("Soory, but without weapon you gonna die..(")

start()
