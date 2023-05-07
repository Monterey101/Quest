import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
window.title("Maze Quest")
window.geometry("600x600")
window.resizable(False, False)

class Game():
        Maze1 = [
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
        ]
        Maze2 = [
            [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0]
        ]
        Maze3 = [
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
            [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0]
        ]
        CurrentMaze = Maze1
        LastMaze = False

        def NextMaze(self):
            if self.CurrentMaze == self.Maze1:
                self.CurrentMaze = self.Maze2
            elif self.CurrentMaze == self.Maze2:
                self.CurrentMaze = self.Maze3
                self.LastMaze = True

Quest = Game()

def Menu():
    MenuBackground = tk.Frame(window, width="600", height="600", bg="grey")
    MenuBackground.pack()

    Title = tk.Label(MenuBackground, text="Maze Quest", font=('consolas',70), fg="white", bg="grey")
    Title.place(x=120, y=40)

    #img = tk.PhotoImage(file="QuestIcon.png")
    #MenuImage= tk.Label(MenuBackground, image = img, bg="red")
    #MenuImage.place(x=250, y=160, width=100, heigh=100)

    #img = tk.PhotoImage(file="QuestIcon.jpg")
    #panel = tk.Label(window, image = img)
    #panel.pack(side = "bottom", fill = "both", expand = "yes")

    Quest.CurrentMaze = Quest.Maze1

    PlayButton = tk.Button(MenuBackground, text="PLAY", bg="white", command=Play, width=20, height=2, fg="black")
    PlayButton.place(x=190, y=350)

def Play():

    class Player():
        ypos = 0
        xpos = 0
    player = Player()

    def SetBoard():
        ycounter = 0
        for y in Quest.CurrentMaze:
            xcounter = 0
            for x in y:
                gap = 0
                if x == 1:
                    box = tk.Frame(window, bg="grey", width=50, height=50)
                    box.place(x=(xcounter*50)+gap, y=ycounter*50)
                else:
                    gap+=50

                xcounter += 1
            ycounter += 1

    board = tk.Canvas(window, width="600", height="600", highlightthickness=0, bg="white")
    Goal = board.create_oval(560, 60, 590, 90, fill="yellow")
    rectangle = board.create_rectangle(40, 40, 10, 10, fill="red")
    board.place(x=0, y=0)

    SetBoard()

    def NextMaze():
        Quest.NextMaze()
        Play()

    def CheckWin():
        if player.xpos == 11 and player.ypos == 1:
            Win = tk.Label(text="YOU WIN", font=('consolas',70), bg="black", width=14, height=8, fg="green")
            Win.place(x=0, y=-75)
            if Quest.LastMaze != True:
                PlayButton = tk.Button(Win, text="NEXT MAZE", bg="white", command=NextMaze, width=20, height=2, fg="black")
                PlayButton.place(x=200, y=400)

    def MoveLeft():
        if player.xpos > 0 and Quest.CurrentMaze[player.ypos][player.xpos - 1] != 1:
            board.move(rectangle, -50, 0)
            player.xpos = player.xpos - 1
        CheckWin()

    def MoveRight():
        if player.xpos < 11 and Quest.CurrentMaze[player.ypos][player.xpos + 1] != 1:
            board.move(rectangle, 50, 0)
            player.xpos = player.xpos + 1
        CheckWin()

    def MoveUp():
        if player.ypos > 0 and Quest.CurrentMaze[player.ypos - 1][player.xpos] != 1:
            board.move(rectangle, 0, -50)
            player.ypos = player.ypos - 1
        CheckWin()

    def MoveDown():
        if player.ypos < 11 and Quest.CurrentMaze[player.ypos + 1][player.xpos] != 1:
            board.move(rectangle, 0, 50)
            player.ypos = player.ypos + 1
        CheckWin()

    window.bind("<KeyPress-Left>", lambda e: MoveLeft())
    window.bind("<KeyPress-Right>", lambda e: MoveRight())
    window.bind("<KeyPress-Up>", lambda e: MoveUp())
    window.bind("<KeyPress-Down>", lambda e: MoveDown())

Menu()
window.mainloop()