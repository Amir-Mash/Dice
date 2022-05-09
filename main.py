import random

def roll_dice():
    while True:
        # we want this function to work 3 times before we get the "again?" message
        for i in range(3):
            dice = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    
            # we set the user's output to None so we can have a while loop. this way we can set a condition for the rest of the operation:)
            roll_request = None
            while roll_request != "":
                roll_request = input("Press [ENTER] to Throw The dice: ")
            else:
                rolled_dice = random.choice(dice)
                
                # here we say the index + 1 because indexes brgin from 0 
                print(f"{rolled_dice} => {(dice.index(rolled_dice))+1}")
      
        throw_again = input("Do you want to Throw the dice again?(y/n): ").lower()
        if throw_again == "n":
            break

roll_dice()