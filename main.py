import random
'''
s for snake
w for water
g for gun

'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w":-1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"you choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer == -1 and you == 1):
        print("you win!")

    elif(computer == -1 and you == 0):
        print("you lose!")

    elif(computer == 1 and you == -1):
        print("you lose")

    elif(computer == 1 and you == 0):
        print("you win!")

    elif(computer == 0 and you == -1):
        print("you win!")

    elif(computer == 0 and you == 1):
        print("you lose!")

    else:
        print("something went wrong!")

    