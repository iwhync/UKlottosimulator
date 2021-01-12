from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkst
import random


window = Tk()

window.title("Lottery Simulator") # title bar
window.configure(background="gray")

window.geometry('310x160') # resized window

lbl1 = Label(window, text="Player Numbers", font=("Arial Bold", 30)) # text in program
lbl1.configure(background="gray") # Making the text colour fit
lbl1.grid(column=0, row=1) # where the text will be

lbl2 = Label(window, text="Pick 6 Numbers between 1 - 59", font=("Arial Bold", 10)) # text in program
lbl2.configure(background="gray") # Making the text colour fit
lbl2.grid(column=0, row=2) # where the text will be

x1 = Entry(window,width=5) # adding a text entry box, width 5, for all six numbers.
x2 = Entry(window,width=5)
x3 = Entry(window,width=5)
x4 = Entry(window,width=5)
x5 = Entry(window,width=5)
x6 = Entry(window,width=5)

x1.place(x=30, y=80) # placing buttons in a nice order
x2.place(x=70, y=80)
x3.place(x=110, y=80)
x4.place(x=150, y=80)
x5.place(x=190, y=80)
x6.place(x=230, y=80)




def go(): # the function when that will run from the button
    
    try:
        
        playernum = []
    
        p1 = int(x1.get()) # changing each entry into a number
        p2 = int(x2.get())
        p3 = int(x3.get())
        p4 = int(x4.get())
        p5 = int(x5.get())
        p6 = int(x6.get())
        
    except:
        
        lbl3 = Label(window, text="  Error, Try Again.  ", font=("Arial", 10)) # bit of error handling if there's no number
        lbl3.configure(background="red") # stands out in red
        lbl3.grid(column=0, row=4) # where the text will be
        lbl3.after(2000, lambda: lbl3.destroy() ) # clear after 2 seconds
        playernum.clear() # removes whatever numbers in the list already
        x1.delete(0,"end") # and deletes all text out of the boxes so as to not confuse anything
        x2.delete(0,"end")
        x3.delete(0,"end")
        x4.delete(0,"end")
        x5.delete(0,"end")
        x6.delete(0,"end")
    
    try:
    
        if p1 not in playernum: # if first entry isn't already in our player numbers, append to list
            if p1 <= 59: # although check first it's not more than 59
                if p1 > 0: # or less than zero!
                    playernum.append(p1) 
                else:
                    playernum.clear() # if the number is invalid clear list
                    lbl4 = Label(window, text="Numbers can't be less than 1", font=("Arial", 10))  # user warning
                    lbl4.configure(background="red") 
                    lbl4.grid(column=0, row=4) 
                    lbl4.after(2000, lambda: lbl4.destroy() )
                    x1.delete(0,"end") # finally remove the invalid number from the GUI

                    '''
                    This is the same now for all 6 numbers, not going to comment them. Just amend as needed.
                    '''

            else:
                playernum.clear()
                lbl5 = Label(window, text="Number can't be higher than 59", font=("Arial", 10)) 
                lbl5.configure(background="red") 
                lbl5.grid(column=0, row=4) 
                lbl5.after(2000, lambda: lbl5.destroy() )
                time.sleep(2)
                x1.delete(0,"end")
        else:
            playernum.clear()
            lbl6 = Label(window, text="     Number already chosen     ", font=("Arial", 10)) 
            lbl6.configure(background="red") 
            lbl6.grid(column=0, row=4) 
            lbl6.after(2000, lambda: lbl6.destroy() )
            time.sleep(2)
            x1.delete(0,"end")
                
                    
        if p2 not in playernum:
            if p2 <= 59:
                if p2 > 0:
                    playernum.append(p2)
                else:
                    playernum.clear()
                    lbl7 = Label(window, text="Numbers can't be less than 1", font=("Arial", 10)) 
                    lbl7.configure(background="red") 
                    lbl7.grid(column=0, row=4) 
                    lbl7.after(2000, lambda: lbl7.destroy() )
                    print("Can't be less than 1.")
                    x2.delete(0,"end")
            else:
                playernum.clear()
                lbl8 = Label(window, text="Number can't be higher than 59", font=("Arial", 10)) 
                lbl8.configure(background="red") 
                lbl8.grid(column=0, row=4) 
                lbl8.after(2000, lambda: lbl8.destroy() )
                x2.delete(0,"end")
        else:
            playernum.clear()
            lbl9 = Label(window, text="     Number already chosen     ", font=("Arial", 10)) 
            lbl9.configure(background="red") 
            lbl9.grid(column=0, row=4) 
            lbl9.after(2000, lambda: lbl9.destroy() )
            x2.delete(0,"end")
            
                    
        if p3 not in playernum:
            if p3 <= 59:
                if p3 > 0:
                    playernum.append(p3)
                else:
                    playernum.clear()
                    lbl10 = Label(window, text="Numbers can't be less than 1", font=("Arial", 10)) 
                    lbl10.configure(background="red") 
                    lbl10.grid(column=0, row=4) 
                    lbl10.after(2000, lambda: lbl10.destroy() )
                    x3.delete(0,"end")
            else:
                playernum.clear()
                lbl11 = Label(window, text="Number can't be higher than 59", font=("Arial", 10)) 
                lbl11.configure(background="red") 
                lbl11.grid(column=0, row=4) 
                lbl11.after(2000, lambda: lbl11.destroy() )
                x3.delete(0,"end")
        else:
            playernum.clear()
            lbl12 = Label(window, text="     Number already chosen     ", font=("Arial", 10)) # text in program
            lbl12.configure(background="red") # Making the text colour fit
            lbl12.grid(column=0, row=4) # where the text will be
            lbl12.after(2000, lambda: lbl12.destroy() )
            x3.delete(0,"end")
                    
        if p4 not in playernum:
            if p4 <= 59:
                if p4 > 0:
                    playernum.append(p4)
                else:
                    playernum.clear()
                    lbl13 = Label(window, text="Numbers can't be less than 1", font=("Arial", 10)) 
                    lbl13.configure(background="red") 
                    lbl13.grid(column=0, row=4) 
                    lbl13.after(2000, lambda: lbl13.destroy() )
                    x4.delete(0,"end")
            else:
                playernum.clear()
                lbl14 = Label(window, text="Number can't be higher than 59", font=("Arial", 10)) 
                lbl14.configure(background="red") 
                lbl14.grid(column=0, row=4) 
                lbl14.after(2000, lambda: lbl14.destroy() )
                x4.delete(0,"end")
        else:
            playernum.clear()
            lbl5 = Label(window, text="     Number already chosen     ", font=("Arial", 10)) 
            lbl5.configure(background="red") 
            lbl5.grid(column=0, row=4) 
            lbl5.after(2000, lambda: lbl5.destroy() )
            x4.delete(0,"end")
                    
        if p5 not in playernum:
            if p5 <= 59:
                if p5 > 0:
                    playernum.append(p5)
                else:
                    playernum.clear()
                    lbl6 = Label(window, text="Numbers can't be less than 1", font=("Arial", 10)) 
                    lbl6.configure(background="red") 
                    lbl6.grid(column=0, row=4) 
                    lbl6.after(2000, lambda: lbl6.destroy() )
                    x5.delete(0,"end")
            else:
                playernum.clear()
                lbl7 = Label(window, text="Number can't be higher than 59", font=("Arial", 10)) 
                lbl7.configure(background="red") 
                lbl7.grid(column=0, row=4) 
                lbl7.after(2000, lambda: lbl7.destroy() )
                x5.delete(0,"end")
        else:
            playernum.clear()
            lbl8 = Label(window, text="     Number already chosen     ", font=("Arial", 10)) 
            lbl8.configure(background="red") 
            lbl8.grid(column=0, row=4) 
            lbl8.after(2000, lambda: lbl8.destroy() )
            x5.delete(0,"end")
                    
        if p6 not in playernum:
            if p6 <= 59:
                if p6 > 0:
                    playernum.append(p6)
                else:
                    playernum.clear()
                    lbl9 = Label(window, text="Numbers can't be less than 1", font=("Arial", 10)) 
                    lbl9.configure(background="red") 
                    lbl9.grid(column=0, row=4) 
                    lbl9.after(2000, lambda: lbl9.destroy() )
                    x6.delete(0,"end")
            else:
                playernum.clear()
                lb20 = Label(window, text="Number can't be higher than 59", font=("Arial", 10)) 
                lb20.configure(background="red") 
                lb20.grid(column=0, row=4)
                lb20.after(2000, lambda: lb20.destroy() )
                x6.delete(0,"end")
        else:
            playernum.clear()
            lb21 = Label(window, text="     Number already chosen     ", font=("Arial", 10)) 
            lb21.configure(background="red") 
            lb21.grid(column=0, row=4) 
            lb21.after(2000, lambda: lb21.destroy() )
            x6.delete(0,"end")
    
    except:
        
        playernum.clear() # just some error handling, anything goes wrong and we delete all text and clear the list
        x1.delete(0,"end")
        x2.delete(0,"end")
        x3.delete(0,"end")
        x4.delete(0,"end")
        x5.delete(0,"end")
        x6.delete(0,"end")
        
    finally:
        
        if len(playernum) == 6: # now the length of our playernum is 6 we begin the simulation
            
            playernum = sorted(playernum) # sorted, just for formatting reasons.
            
            x1.delete(0,"end") # remove all entered user numbers
            x2.delete(0,"end")
            x3.delete(0,"end")
            x4.delete(0,"end")
            x5.delete(0,"end")
            x6.delete(0,"end")

            x1.insert(END, playernum[0]) # and replace with new sorted list, just for formatting.
            x2.insert(END, playernum[1])
            x3.insert(END, playernum[2])
            x4.insert(END, playernum[3])
            x5.insert(END, playernum[4])
            x6.insert(END, playernum[5])
            
            x1.config(state='disabled') # and grey out the boxes, because why not.
            x2.config(state='disabled')
            x3.config(state='disabled')
            x4.config(state='disabled')
            x5.config(state='disabled')
            x6.config(state='disabled')
            
            
            wind = tk.Tk() # opening a new window now
            wind.title("Running Simulation") # title of window
            frame1 = tk.Frame(master = wind,bg = '#808000')
            frame1.pack(fill='both', expand='yes') # packing frame for scrolled text
            editArea = tkst.ScrolledText(master = frame1,wrap = tk.WORD,width  = 100,height = 50) # the results can be huge
            # so using scrolled text
            editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
            editArea.insert(tk.INSERT,"The simulation will end when all 6 numbers are matched \n") # and a bit of info
            editArea.insert(tk.INSERT,"or you can close at any time.\n")  # so the user knows
            editArea.insert(tk.INSERT,"This can take a while, please wait..... \n") # what's going on
            
            nums = [] # general placeholders created
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
            
            while z == True:  # drawing computer numbers, simple list
                while len(comnum) < 6: # we'll move on when 6 numbers are drawn
                    x = random.randint(1,59) # random number in range
                    if x not in comnum: # just to make sure we're not adding the same number twice
                        comnum.append(x) # appending drawn numbers to a list
                        comnum = sorted(comnum) # formatting reasons
                    else:
                        pass # might want to put something in here?
                while len(combon) < 1: # bonus ball is a seperate list
                        c = random.randint(1,59)
                        if c not in comnum: # not really needed
                            combon.append(c) # adding bonus ball to it's own list
                        else:
                            pass

                if playernum == comnum: # if all player numbers match drawn numbers
                    
                    editArea.insert(tk.INSERT,"\n") # insert is adding text to the window
                    editArea.insert(tk.INSERT,"Winner.")
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,"Player numbers were")
                    editArea.insert(tk.INSERT,"\n")
                    playernum = ' '.join(str(v) for v in playernum) # just to make it look nice without []
                    editArea.insert(tk.INSERT,playernum)
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,f"Tries taken {start}") # keeping track of how many draws
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,"\n")
                    cost = start * 2 # a lottery ticket here is £2, so this is to work out overall cost.
                    editArea.insert(tk.INSERT,f"At £2 a ticket, this would have cost you £{cost} to hit the jackpot.")
                    editArea.insert(tk.INSERT,"\n")
                    prize = 5000000 - cost # £5M jackpot, minus cost for tries taken
                    editArea.insert(tk.INSERT,f"Based on an average jackpot of £5,000,000, this would leave your balance at £{prize}")
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,"Well done.\nMore Info\n") # sarcasam
                    editArea.insert(tk.INSERT,"\n")

                    none = len(none) # each outcome has assigned an int to a list.
                    one = len(one) # we're checking the length of each list
                    two = len(two) # to determin how many of each outcome occured
                    three = len(three)
                    four = len(four)
                    five = len(five)
                    bonus = len(bonus)

                    bonusprize = bonus * 1000000 # these are the only outcomes that give a prize
                    fiveprize = five * 1750 # so len of list * average prize
                    fourprize = four * 140
                    threeprize = three * 30

                    prizes = bonusprize + fiveprize + fourprize + threeprize + 5000000 # all prizes + 5M jackpot
                    everything = prizes - cost # total overall cost / loss ratio

                    editArea.insert(tk.INSERT,f"Total prizes are £{prizes}")
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,f"Including the jackpot this leaves you with a balance of £{everything}")
                    editArea.insert(tk.INSERT,"\n")


                    editArea.insert(tk.INSERT,f"No numbers matched {none} times") # some more details for the user
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,f"One number matched {one} times")
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,f"Two numbers matched {two} times")
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,f"Three numbers matched {three} times. £30 prize for each.")
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,f"Four numbers matched {four} times. £140 prize for each.")
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,f"Five numbers drawn {five} times. £1750 prize for each.")
                    editArea.insert(tk.INSERT,"\n")
                    editArea.insert(tk.INSERT,f"Five numbers and bonus ball drawn {bonus} times. £1000000 for each.")
                    editArea.insert(tk.INSERT,"\n")

                    percentage = (none / start) * 100 # simple formula for percentages
                    editArea.insert(tk.INSERT,f"No numbers matched {percentage}% of the time")
                    editArea.insert(tk.INSERT,"\n")

                    percentage = (one / start) * 100
                    editArea.insert(tk.INSERT,f"One number matched {percentage}% of the time")
                    editArea.insert(tk.INSERT,"\n")

                    percentage = (two / start) * 100
                    editArea.insert(tk.INSERT,f"Two numbers matched {percentage}% of the time")
                    editArea.insert(tk.INSERT,"\n")

                    percentage = (three / start) * 100
                    editArea.insert(tk.INSERT,f"Three numbers matched {percentage}% of the time")
                    editArea.insert(tk.INSERT,"\n")

                    percentage = (four / start) * 100
                    editArea.insert(tk.INSERT,f"Four numbers matched {percentage}% of the time")
                    editArea.insert(tk.INSERT,"\n")

                    percentage = (five / start) * 100
                    editArea.insert(tk.INSERT,f"Five numbers matched {percentage}% of the time")
                    editArea.insert(tk.INSERT,"\n")

                    percentage = (bonus / start) * 100
                    editArea.insert(tk.INSERT,f"Five numbers and bonus ball matched {percentage}% of the time")
                    editArea.insert(tk.INSERT,"\n")

                    
                    wind.mainloop() # finally break loop
                    

                    break # and end

                for num in playernum: # for any other outcomes
                    if num in comnum: # iterate through lists and match up numbers
                        win.append("x") # append to win list, length of list will determin how many numbers matched

                for num in playernum: # same for bonus ball
                    if num in combon:
                        bon.append("x")

                if len(win) == 1: # for 1 ball matched
                    start = start + 1 # add one to the tries taken counter
                    one.append(1) # append an int to "one" list
                    comnum.clear() # clear drawn balls for another try
                    combon.clear() # clear bonus ball for another try
                    win.clear() # clear win list for another try
                    bon.clear() # clear bonus list for another try

                '''
                This is more of the same for the other outcomes, so won't comment, just amend as needed.
                '''


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

                '''
                It's the same for 5 balls too, BUT as this is a "rare" happening, we're giving the user a bit of info just for boredom reasons
                    
                '''

                if len(win) == 5:
                    if len(bon) == 1: # if 5 numbers drawn AND bonus ball a different message is displayed
                        editArea.insert(tk.INSERT,f"5 numbers and bonus ball matched at draw number {start}. Numbers drawn were {comnum[0],comnum[1],comnum[2],comnum[3],comnum[4],comnum[5]} and Bonus {combon[0]}")
                        editArea.insert(tk.INSERT,"\n") 
                        start = start + 1
                        comnum.clear()
                        combon.clear()
                        bonus.append(6)
                        win.clear()
                        bon.clear()
                        
                    else:
                        editArea.insert(tk.INSERT,f"5 numbers matched at draw number {start}. Numbers drawn were {comnum[0],comnum[1],comnum[2],comnum[3],comnum[4],comnum[5]}.")
                        editArea.insert(tk.INSERT,"\n")
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
                    
                wind.update() # update the window each iteration for a "live" feed for user
                    


btn0 = Button(window, text="Run Simulation", bg="green", fg="black",command=go) # the one button command
btn0.place(x=180, y=110) # where it is
window.mainloop() # break loop
