import random

print("Realistic Lottery Simulator!")
print("You will be assigned 6 random numbers between 1 - 59.")
print("These will remain static.")
print("Numbers will then be drawn over and over until both your numbers, and the drawn numbers are an exact match")
print("You will then be informed of how many attempts this had taken, and the accumulative cost")
print("Expect this to take a while. Probably like, 10 minutes? Unless you're very lucky!!")
input("Ready to begin? Press enter.")
print("\n")
print("Running simulation. Please wait.")

playernum = []
comnum = []
z = True
start = 0
while z == True:
    while len(playernum) < 6:
        x = random.randint(1,59)
        if x not in playernum:
            playernum.append(x)
            playernum = sorted(playernum)
        else:
            pass
    while len(comnum) < 6:
        x = random.randint(1,59)
        if x not in comnum:
            comnum.append(x)
            comnum = sorted(comnum)
        else:
            pass
    if playernum == comnum:
        z == False
        print("Winner.")
        print(f"Tries taken {start}")
        start = start * 2
        print(f"This would have cost you £{start}")
        print("Well done.")
        input("Press enter to close.")
        break
    if playernum[0:4] == comnum[0:4]: # added to keep it from doing nothing, also quite interesting to see how often 5 numbers is possible in comparasion to 6. 
        print(f"5 number match at draw {start}")
        comnum.clear()
    else:
        comnum.clear()
        z == True
        start = start + 1
