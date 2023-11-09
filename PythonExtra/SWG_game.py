import random
import time
from typing import Self

print(
    "We are going to play Snake , Water, Gun game.\nRules :  The gun beats the snake, the water beats the gun, and the snake beats the water.\nRepresentation will be :  \nSnake = 0\nWater  = 1 \nGun = 2 "
)

count = 0
def check():
    global count
    if comp == user:
        print("\nMatch Draw")
    elif comp == 1 and user == 2:
        print("\nComputer Wins")
    elif comp == 2 and user == 1:
        print("\nYou Win")
        count += 1
    elif comp == 0 and user == 1:
        print("\nComputer Wins")
    elif comp == 1 and user == 0:
        print("\nYou Win")
        count = count + 1
    else:
        print("\nYou Lose")


for i in range(5):
    print("-------------------------------------------")
    user = int(input("\nWhat would you choose: "))
    comp = random.randint(0, 2)
    # time.sleep(1)
    print("Computer Chooses :", comp)
    print("You choose:", user)
    check()
print(f"You won {count} out of 5 times")
