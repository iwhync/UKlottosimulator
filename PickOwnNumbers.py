import random

print("Realistic Lottery Simulator!")
print("You need to choose 6 numbers between 1 - 59. These will remain static.")
print("Numbers will then be drawn over and over until both your numbers, and the drawn numbers are an exact match")
print("You will then be informed of how many attempts this had taken, and how much money you wasted.")
print("Expect this to take a while.\n")

'''
Setting up various placeholders for later
'''

nums = []
playernum = []
comnum = []
combon = []
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
rplayernum = []
c = 1
z = True

while len(playernum) < 6: # we need to have 6 numbers in the list, to match the lottery draw
    
    try: # using try for a little bit of error handling, so no spaces, letters, symbols etc will be accepted

        x = input(f"Number {c} between 1 and 59: ") # x is going to be each number
        x = int(x) # just making sure the number, is a number.
        if x not in playernum: # if the number isn't in the player numbers already
            if x <= 59: # has to be less than or equal to 59
                if x > 0: # or more than zero
                    c = c + 1 # changing the number for the input line, to make it clear where the user is
                    playernum.append(x) # and finally add the chosen number to list

                else:
                    print("Can't be less than 1!") # warning if player tries to select a number less than 1

            else:
                print("Can't be more than 59!") # another if player tries to choose a number over 59
        else:
            print("Number already chosen") # and if number is already in list

        if len(playernum) == 6: # when there's six numbers
            playernum = sorted(playernum) # sorting into numerical order
            rplayernum = ' '.join(str(v) for v in playernum) # this is just to display users numbers without []
            print(f"\nNumbers chosen are: {rplayernum}")
            print("\nRunning Simulation. Please Wait.\n") # for the player to know to wait for a bit
            
    except:
        print("Needs to be a number between 1 and 59.") # error handling

while z == True:       
    while len(comnum) < 6: # similar set up for drawn numbers
        x = random.randint(1,59) # each number is a random between 1 - 59
        if x not in comnum: # if number isn't already selected
            comnum.append(x) # then add to list
            comnum = sorted(comnum) # numerically sorted for consistancy
        else:
            pass
    while len(combon) < 1: # bonus ball
            c = random.randint(1,59) # choosing another number
            if c not in comnum:
                combon.append(c) # and appending
            else:
                pass

    for num in playernum: # iterating through the numbers
        if num in comnum: # if the player number is in the drawn number
            win.append("x") # append an x to "win" for each instance
        
    for num in playernum: # iterating through numbers
        if num in combon: # if the bonus ball is in player numbers
            bon.append("x") # append a character to the bonus list
    
    if len(win) == 6: # if win is len 6, then the player has won
        z == False
        print("\n")
        print("Winner.")
        print("Player numbers were")
        playernum = ' '.join(str(v) for v in playernum) # formatting
        print(playernum)
        print("\n")
        print(f"Tries taken {start}") # kept track of how many draws were made
        cost = start * 2 # UK lotto tickets are £2 each, so just a way to work out how much was "spent"
        print(f"At £2 a ticket, this would have cost you £{cost} to hit the jackpot.") # info for the player
        prize = 5000000 - cost # average prize for jackpot is 5M, just for more info to relay
        print(f"Based on an average jackpot of £5,000,000, this would leave your balance at £{prize}")
        print("Well done.") # sarcasam.
        print("\n")
        print("More Info")
        print("\n")
        
        none = len(none) # changing to just the len of a list, to keep track on how many times each occured
        one = len(one)
        two = len(two)
        three = len(three)
        four = len(four)
        five = len(five)
        bonus = len(bonus)
        
        bonusprize = bonus * 1000000 # keep track of bonus ball winnings (1m each time)
        fiveprize = five * 1750 # keep track of five ball winnings
        fourprize = four * 140 # four ball winnings
        threeprize = three * 30 # three ball winnings
        
        prizes = bonusprize + fiveprize + fourprize + threeprize + 5000000 # everything including jackpot
        everything = prizes - cost # and now taking the overall amount "spent"
        
        print(f"Total prizes are £{prizes}") # all prizes including jackpot
        print(f"Including the jackpot this leaves you with a balance of £{everything}") # prizes - cost
        print("\n")
        
        
        print(f"No numbers matched {none} times") # to inform the user how many times each possible outcome
        print(f"One number matched {one} times")
        print(f"Two numbers matched {two} times")
        print(f"Three numbers matched {three} times. £30 prize for each.")
        print(f"Four numbers matched {four} times. £140 prize for each.")
        print(f"Five numbers drawn {five} times. £1750 prize for each.")
        print(f"Five numbers and bonus ball drawn {bonus} times. £1000000 for each.")
        
        print("\n")

        percentage = (none / start) * 100 # followed by percentages
        print(f"No numbers matched {percentage}% of the time")

        percentage = (one / start) * 100
        print(f"One number matched {percentage}% of the time")

        percentage = (two / start) * 100
        print(f"Two numbers matched {percentage}% of the time")

        percentage = (three / start) * 100
        print(f"Three numbers matched {percentage}% of the time")

        percentage = (four / start) * 100
        print(f"Four numbers matched {percentage}% of the time")

        percentage = (five / start) * 100 # some issues with this and bonus ball, the percentages decimals aren't long enough
        print(f"Five numbers matched {percentage}% of the time") 
        
        percentage = (bonus / start) * 100
        print(f"Five numbers and bonus ball matched {percentage}% of the time")
        input = ("\n Press enter to close!")
        
        break
        
    if len(win) == 1: # if win has one character, then
        start = start + 1 # start = tries made
        one.append(1) # appending a char to list
        comnum.clear() # clearing drawn numbers
        combon.clear() # clearing bonus ball
        win.clear() # clearing win list
        bon.clear() # clearing bonus ball list
        
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
            print(f"5 numbers and bonus ball matched at draw number {start}. Numbers drawn were {comnum} and bonus {combon}")
            # just some info to keep the player entertained
            start = start + 1
            comnum.clear()
            combon.clear()
            bonus.append(6)
            win.clear()
            bon.clear()
        else:
            print(f"5 numbers matched at draw number {start}. Numbers drawn were {comnum}.")
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
