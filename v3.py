import random

print("Realistic Lottery Simulator!")
print("You will be assigned 6 random numbers between 1 - 59.")
print("These will remain static.")
print("Numbers will then be drawn over and over until both your numbers, and the drawn numbers are an exact match")
print("You will then be informed of how many attempts this had taken, and how much money you wasted.")
print("Expect this to take a while.")
input("Press enter to begin.")

print("\n")
print("Running simulation. Please wait.")
print("\n")

nums = []
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
y = 0
win = []
bon = []

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
    while len(combon) < 1:
            c = random.randint(1,59)
            if c not in comnum:
                combon.append(c)
            else:
                pass
    
    if playernum == comnum:
        z == False
        print("\n")
        print("Winner.")
        print("Player numbers were")
        playernum = ' '.join(str(v) for v in playernum)
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
        one = len(one)
        two = len(two)
        three = len(three)
        four = len(four)
        five = len(five)
        bonus = len(bonus)
        
        bonusprize = bonus * 1000000
        fiveprize = five * 1750
        fourprize = four * 140
        threeprize = three * 30
        
        prizes = bonusprize + fiveprize + fourprize + threeprize + 5000000
        everything = prizes - cost
        
        print(f"Total prizes are £{prizes}")
        print(f"Including the jackpot this leaves you with a balance of £{everything}")
        print("\n")
        
        
        print(f"No numbers matched {none} times")
        print(f"One number matched {one} times")
        print(f"Two numbers matched {two} times")
        print(f"Three numbers matched {three} times. £30 prize for each.")
        print(f"Four numbers matched {four} times. £140 prize for each.")
        print(f"Five numbers drawn {five} times. £1750 prize for each.")
        print(f"Five numbers and bonus ball drawn {bonus} times. £1000000 for each.")
        
        print("\n")

        percentage = (none / start) * 100
        print(f"No numbers matched {percentage}% of the time")

        percentage = (one / start) * 100
        print(f"One number matched {percentage}% of the time")

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
        
    if playernum[0] in comnum:
        win.append("x")
    if playernum[1] in comnum:
        win.append("x")
    if playernum[2] in comnum:
        win.append("x")
    if playernum[3] in comnum:
        win.append("x")
    if playernum[4] in comnum:
        win.append("x")
        
    for num in playernum:
        if num in combon:
            bon.append("x")
        
    if len(win) == 1:
        start = start + 1
        one.append(1)
        comnum.clear()
        combon.clear()
        win.clear()
        bon.clear()
        
    if len(win) == 2:
        start = start + 1
        comnum.clear()
        combon.clear()
        two.append(2)
        win.clear()
        bon.clear()
        
    if len(win) == 3:
        start = start + 1
        comnum.clear()
        combon.clear()
        three.append(3)
        win.clear()
        bon.clear()
        
    if len(win) == 4:
        start = start + 1
        comnum.clear()
        combon.clear()
        four.append(4)
        win.clear()
        bon.clear()
        
    if len(win) == 5:
        if len(bon) == 1:
            print(f"5 numbers and bonus ball matched at {start}")
            start = start + 1
            comnum.clear()
            combon.clear()
            bonus.append(6)
            win.clear()
            bon.clear()
        else:
            print(f"5 numbers matched at {start}")
            start = start + 1
            comnum.clear()
            combon.clear()
            five.append(5)
            win.clear()
            bon.clear()
                
    if len(win) == 0:
        start = start + 1
        comnum.clear()
        combon.clear()
        none.append(0)
        win.clear()
        bon.clear()
