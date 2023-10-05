#guess the number project in python
import random


while True:
    print('In this game you need to guess the mystery number, You will be given clues to find the number, You have three tries, ALL THE BEST!!')
    mystery_number = random.randint(1, 100)
    print(mystery_number)
    x = 0
    z = 3
    while x < z:
        num = int(input("Try: "))
        if num == mystery_number:
            print("Congratulations you have found the right number")
            break
        elif num < mystery_number:
            print("The number is higher ")
        elif num > mystery_number:
            print("The number is lower")
        x=x+1
        if x == z:
            print(f"Sorry you ran out of tries, The number was {mystery_number}")
    y = int(input("Write 1 to continue or 0 to exit\n"))
    if y == 1:
        continue
    if y == 0:
        quit()
