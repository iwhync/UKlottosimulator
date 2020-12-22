import random

print("Realistic Lottery Simulator!")
print("You will be assigned 6 random numbers between 1 - 59.")
print("These will remain static.")
print("Numbers will then be drawn over and over until both your numbers, and the drawn numbers are an exact match")
print("You will then be informed of how many attempts this had taken, and the accumulative cost")
print("Expect this to take a while. Probably like, 10 minutes? Unless you're very lucky!!")
input("Press enter to begin.")

print("\n")
print("Running simulation. Please wait.")
print("\n")

playernum = []
comnum = []
combon = []
z = True
five = []
four = []
three = []
two = []
one = []
none = []
bonus = []
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
            while len(combon) < 1:
                c = random.randint(1,59)
                if c not in comnum:
                    combon.append(c)
                else:
                    pass
    if playernum == comnum:
        z == False
        print("Winner.")
        print("Player numbers were")
        print(playernum)
        print("\n")
        print(f"Tries taken {start}")
        cost = start * 2
        print(f"At £2 a ticket, this would have cost you £{cost} to hit the jackpot.")
        prize = 5000000 - cost
        print(f"Based on an average jackpot of £5,000,000, this would leave your balance at £{prize}")
        print("Well done.")
        print("\n")
        print("More Info")
        print("\n")
        
        none = len(none)
        two = len(two)
        three = len(three)
        four = len(four)
        five = len(five)
        bonus = len(bonus)
        
        print(f"None or One numbers matched {none} times")
        print(f"Two numbers matched {two} times")
        print(f"Three numbers matched {three} times")
        print(f"Four numbers matched {four} times")
        print(f"Five numbers drawn {five} times")
        print(f"Five numbers and bonus ball drawn {bonus} times")
        
        print("\n")

        percentage = (none / start) * 100
        print(f"One or No numbers matched {percentage}% of the time")

        percentage = (two / start) * 100
        print(f"Two numbers matched {percentage}% of the time")

        percentage = (three / start) * 100
        print(f"Three numbers matched {percentage}% of the time")

        percentage = (four / start) * 100
        print(f"Four numbers matched {percentage}% of the time")

        percentage = (five / start) * 100
        print(f"Five numbers matched {percentage}% of the time")
        
        percentage = (bonus / start) * 100
        print(f"Five numbers and bonus ball matched {percentage}% of the time")
        
        break
        
    if playernum[0:4] == comnum[0:4]:
        for num in playernum:
            i = num in combon
            if i == True:
                print(f"Five numbers and bonus ball drawn at {start}! Average £1,000,000 prize.")
                bonus.append("b")
                start = start + 1
                comnum.clear()
                combon.clear()
        else: 
            print(f"Five numbers drawn at {start}, Average £1750 prize.")
            start = start + 1
            five.append("5")
            comnum.clear()
            combon.clear()
    elif playernum[0:3] == comnum[0:3]:
        four.append("4")
        start = start + 1
        comnum.clear()
        combon.clear()
    elif playernum[0:2] == comnum[0:2]:
        three.append("3")
        start = start + 1
        comnum.clear()
        combon.clear()
    elif playernum[0:1] == comnum[0:1]:
        two.append("2")
        start = start + 1
        comnum.clear()
        combon.clear()
    else:
        none.append("x")
        start = start + 1
        comnum.clear() 
        combon.clear()
