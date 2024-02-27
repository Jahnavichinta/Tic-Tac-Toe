import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("900x650+0+0")
root.title("Tic Tac Toe")
root.configure(background = "peru")

Tops = Frame(root, bg = "lightcoral", pady = 2, width = 900, height = 500, relief = RIDGE )
Tops.grid(row = 0, column = 0)

lblTitle = Label(Tops, font = ("arial", 40, "bold"), text = "Tic Tac Toe", bd = 15, bg = "peru", fg = "cornsilk", justify = CENTER)
lblTitle.grid(row = 0, column = 0)

MainFrame = Frame(root, bg = "tan", pady = 2, width = 900, height = 550, relief = RIDGE )
MainFrame.grid(row = 1, column = 0)

Left = Frame(MainFrame, bd = 10, width = 20, height = 500, pady = 2, padx = 10, bg = "tan")
Left.pack(side = LEFT)

LeftFrame = Frame(MainFrame, bd = 10, width = 400, height = 500, pady = 2, padx = 10, bg = "tan", relief = RIDGE)
LeftFrame.pack(side = LEFT)

MidFrame = Frame(MainFrame, bd = 10, width = 70, height = 500, pady = 2, padx = 10, bg = "tan")
MidFrame.pack(side = LEFT)

RightFrame = Frame(MainFrame, bd = 10, width = 400, height = 500, pady = 2, padx = 10, bg = "tan", relief = RIDGE)
RightFrame.pack(side = LEFT)

Right = Frame(MainFrame, bd = 10, width = 20, height = 500, pady = 2, padx = 10, bg = "tan")
Right.pack(side = RIGHT)

RightFrame1 = Frame(RightFrame, bd = 10, width = 300, height = 200, pady = 2, padx = 10, bg = "tan", relief = RIDGE)
RightFrame1.grid(row = 0, column = 0)

RightFrame2 = Frame(RightFrame, bd = 10, width = 300, height = 200, pady = 2, padx = 10, bg = "tan", relief = RIDGE)
RightFrame2.grid(row = 1, column = 0)

playerX = IntVar()
playerO = IntVar()

playerX.set(0)
playerO.set(0)

button = StringVar()
click = True
 
def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()

def is_full():
    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    c = 0
    for button in buttons:
        if button["text"] == " ":
            return False
    return True

def scorekeeper():
        if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
            button1.configure(background = "peru")
            button2.configure(background = "peru")
            button3.configure(background = "peru")
            n = (playerX.get())
            score = n + 1
            playerX.set(score)
            tkinter.messagebox.showinfo("Winner x", "You have won the game Mr X")
            reset()
            
        if button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
            button4.configure(background = "peru")
            button5.configure(background = "peru")
            button6.configure(background = "peru")
            n = (playerX.get())
            score = n + 1
            playerX.set(score)
            tkinter.messagebox.showinfo("Winner x", "You have won the game Mr X")
            reset()

        if button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
            button7.configure(background = "peru")
            button8.configure(background = "peru")
            button9.configure(background = "peru")
            n = (playerX.get())
            score = n + 1
            playerX.set(score)
            tkinter.messagebox.showinfo("Winner x", "You have won the game Mr X")
            reset()
            
        if button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
            button1.configure(background = "peru")
            button4.configure(background = "peru")
            button7.configure(background = "peru")
            n = (playerX.get())
            score = n + 1
            playerX.set(score)
            tkinter.messagebox.showinfo("Winner x", "You have won the game Mr X")
            reset()
            
        if button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
            button2.configure(background = "peru")
            button5.configure(background = "peru")
            button8.configure(background = "peru")
            n = (playerX.get())
            score = n + 1
            playerX.set(score)
            tkinter.messagebox.showinfo("Winner x", "You have won the game Mr X")
            reset()
            
        if button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
            button3.configure(background = "peru")
            button6.configure(background = "peru")
            button9.configure(background = "peru")
            n = (playerX.get())
            score = n + 1
            playerX.set(score)
            tkinter.messagebox.showinfo("Winner x", "You have won the game Mr X")
            reset()
            
        if button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
            button1.configure(background = "peru")
            button5.configure(background = "peru")
            button9.configure(background = "peru")
            n = (playerX.get())
            score = n + 1
            playerX.set(score)
            tkinter.messagebox.showinfo("Winner x", "You have won the game Mr X")
            reset()
            
        if button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
            button3.configure(background = "peru")
            button5.configure(background = "peru")
            button7.configure(background = "peru")
            n = (playerX.get())
            score = n + 1
            playerX.set(score)
            tkinter.messagebox.showinfo("Winner x", "You have won the game Mr X")
            reset()
            
        if button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
            button1.configure(background = "peru")
            button2.configure(background = "peru")
            button3.configure(background = "peru")
            n = (playerO.get())
            score = n + 1
            playerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have won the game Mr O")
            reset()
            
        if button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
            button4.configure(background = "peru")
            button5.configure(background = "peru")
            button6.configure(background = "peru")
            n = (playerO.get())
            score = n + 1
            playerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have won the game Mr O")
            reset()
            
        if button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
            button7.configure(background = "peru")
            button8.configure(background = "peru")
            button9.configure(background = "peru")
            n = (playerO.get())
            score = n + 1
            playerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have won the game Mr O")
            reset()
            
        if button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
            button1.configure(background = "peru")
            button4.configure(background = "peru")
            button7.configure(background = "peru")
            n = (playerO.get())
            score = n + 1
            playerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have won the game Mr O")
            reset()
            
        if button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
            button2.configure(background = "peru")
            button5.configure(background = "peru")
            button8.configure(background = "peru")
            n = (playerO.get())
            score = n + 1
            playerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have won the game Mr O")
            reset()
            
        if button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
            button3.configure(background = "peru")
            button6.configure(background = "peru")
            button9.configure(background = "peru")
            n = (playerO.get())
            score = n + 1
            playerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have won the game Mr O")
            reset()
            
        if button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
            button1.configure(background = "peru")
            button5.configure(background = "peru")
            button9.configure(background = "peru")
            n = (playerO.get())
            score = n + 1
            playerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have won the game Mr O")
            reset()
            
        if button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
            button3.configure(background = "peru")
            button5.configure(background = "peru")
            button7.configure(background = "peru")
            n = (playerO.get())
            score = n + 1
            playerO.set(score)
            tkinter.messagebox.showinfo("Winner O", "You have won the game Mr O")
            reset()
        if is_full():
            tkinter.messagebox.showinfo("Winner", "Nobody Wins")
            reset()
    

def reset():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(background = "bisque")
    button2.configure(background = "bisque")
    button3.configure(background = "bisque")
    button4.configure(background = "bisque")
    button5.configure(background = "bisque")
    button6.configure(background = "bisque")
    button7.configure(background = "bisque")
    button8.configure(background = "bisque")
    button9.configure(background = "bisque")

def NewGame():
    reset()
    playerX.set(0)
    playerO.set(0)
    
lblplayerX = Label(RightFrame1, font = ("arial", 20, "bold"), text = "Player X :", bd = 10, fg = "Black", bg = "tan", justify = CENTER)
lblplayerX.grid(row = 0, column = 0, sticky = W)
txtxPlayerX = Entry(RightFrame1, font = ("arial", 20, "bold"), bd = 2, fg = "black", textvariable = playerX, width = 7, justify = LEFT, bg = "bisque").grid(row = 0, column = 1)

lblplayerO = Label(RightFrame1, font = ("arial", 20, "bold"), text = "Player O :", bd = 10, fg = "Black", bg = "tan", justify = CENTER)
lblplayerO.grid(row = 1, column = 0, sticky = W)
txtxPlayerO = Entry(RightFrame1, font = ("arial", 20, "bold"), bd = 2, fg = "black", textvariable = playerO, width = 7, justify = LEFT, bg = "bisque").grid(row = 1, column = 1)

buttonReset = Button(RightFrame2, text = "RESET", font = ("Arial 15 bold"), height = 1, width = 20, bg = "bisque", command = reset)
buttonReset.grid(row = 0,column = 0, sticky = W)

buttonNew = Button(RightFrame2, text = "NEW GAME", font = ("Arial 15 bold"), height = 1, width = 20, bg = "bisque", command = NewGame)
buttonNew.grid(row = 1,column = 0, sticky = W)

button1 = Button(LeftFrame, text = " ", font = ("Arial 26 bold"), height = 2, width = 6, bg = "bisque", command = lambda:checker(button1))
button1.grid(row = 1,column = 0, sticky = S+N+E+W)

button2 = Button(LeftFrame, text = " ", font = ("Arial 26 bold"), height = 2, width = 6, bg = "bisque", command = lambda:checker(button2))
button2.grid(row = 1,column = 1, sticky = S+N+E+W)

button3 = Button(LeftFrame, text = " ", font = ("Arial 26 bold"), height = 2, width = 6, bg = "bisque", command = lambda:checker(button3))
button3.grid(row = 1,column = 2, sticky = S+N+E+W)

button4 = Button(LeftFrame, text = " ", font = ("Arial 26 bold"), height = 2, width = 6, bg = "bisque", command = lambda:checker(button4))
button4.grid(row = 2,column = 0, sticky = S+N+E+W)

button5 = Button(LeftFrame, text = " ", font = ("Arial 26 bold"), height = 2, width = 6, bg = "bisque", command = lambda:checker(button5))
button5.grid(row = 2,column = 1, sticky = S+N+E+W)

button6 = Button(LeftFrame, text = " ", font = ("Arial 26 bold"), height = 2, width = 6, bg = "bisque", command = lambda:checker(button6))
button6.grid(row = 2,column = 2, sticky = S+N+E+W)

button7 = Button(LeftFrame, text = " ", font = ("Arial 26 bold"), height = 2, width = 6, bg = "bisque", command = lambda:checker(button7))
button7.grid(row = 3,column = 0, sticky = S+N+E+W)

button8 = Button(LeftFrame, text = " ", font = ("Arial 26 bold"), height = 2, width = 6, bg = "bisque", command = lambda:checker(button8))
button8.grid(row = 3,column = 1, sticky = S+N+E+W)

button9 = Button(LeftFrame, text = " ", font = ("Arial 26 bold"), height = 2, width = 6, bg = "bisque", command = lambda:checker(button9))
button9.grid(row = 3,column = 2, sticky = S+N+E+W)


root.mainloop()
#colorhunt