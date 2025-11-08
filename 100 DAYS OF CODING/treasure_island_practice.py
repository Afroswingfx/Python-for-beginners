print("Welcome to treasure Island. Your mission is to find the treasure")
direction=input("Left or Right?")
Right="right" or "RIGHT" or "Right"
Left="Left" or "LEFT" or "left"
if direction=="Left":
     print("Lucky you, you proceed safely.")
     decision = input("Do you choose to swim or wait for the boat?")
     if decision == "swim":
         print("Crocodiles attack you. Game over")
     else:
         print("A boat arrives to take you to the island."
                     "You have safely arrived and see a house with three doors. "
                     "One red, one blue and one yellow.")
         door=input("Which door do you open?")
         if door == "red":
          print("Burned by fire. Game over")
         elif door=="blue":
          print("Eaten by beats. Game over")
         elif door=="yellow":
            print("You win")
         else:
            print("Game over")

if direction=="Right":
      print("You fall into a hole. Game over")





