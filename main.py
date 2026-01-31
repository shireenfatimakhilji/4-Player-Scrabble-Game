import graphics as g
import data
import random

class Player():
    def __init__(self, name, score, x_coor, y_goti, x=8):
        self.name = name
        self.score = score
        self.x = x
        self.x_goti = [x_coor]
        self.y_goti = y_goti
        self.n = []
        self.gotiList = data.game_data["gotian"] 
        self.word = []
        self.gotiAllocation()

    def gotiAllocation(self):
        for i in range(0, self.x):
            j = random.randint(0, len(self.gotiList)-1)
            self.n.append(self.gotiList[j])
            if (self.n[i] == "-"):
                self.n[i] = g.choose_l()
            del self.gotiList[j] 
        self.x_goti = g.initializeX(self.x, self.x_goti)
        self.displayGoti()
    
    def displayGoti(self):
        g.displayPlayerGoti(self.n, self.x_goti, self.y_goti, self.name, self.score)
    
    def onClick(self, x, y, grid):
        if g.selLetter=="":
            for i in range(0, self.x):
                if x>=self.x_goti[i] and (x<=(self.x_goti[i]+g.cellSize)) and y<=self.y_goti and (y>=(self.y_goti-g.cellSize)) and self.n[i]!="":
                    g.selLetter = self.n[i]
                    self.n[i] = ""
                    g.drawSquare(self.x_goti[i], self.y_goti, "black")
                    break
        else:
            for i in range(g.gridSize):
                for j in range(g.gridSize):
                    if x>=grid[i][j][0] and (x<=(grid[i][j][0]+g.cellSize)) and y<=grid[i][j][1] and (y>=(grid[i][j][1]-g.cellSize)) and  grid[i][j][2]=="":
                        grid[i][j][2] = g.selLetter
                        g.drawSquare(grid[i][j][0], grid[i][j][1], g.randColour(), grid[i][j][2])
                        self.word.append([i, j, grid[i][j][2]])
                        g.selLetter = "" 
                        break 

    def vertical(self, r, c, grid):
        w = ""
        row = r 
        for i in self.word:
            if i[1] != c:
                print("same column condition")
                return ""
        while row >= 0 and grid[row][c][2] != "":
            row -= 1
        row += 1
        while row < g.gridSize and grid[row][c][2] != "":
            w += grid[row][c][2]
            row += 1
        return w 

    def horizontal(self, r, c, grid):
        w = ""
        column = c 
        for i in self.word:
            if i[0] != r:
                print("same row condition")
                return ""
        while column >= 0 and grid[r][column][2] != "":
            column -= 1 
        column += 1
        while column < g.gridSize and grid[r][column][2] != "":
            w += grid[r][column][2]
            column += 1
        return w 

    def checkWord(self, w):
        for i in data.game_data["words"]:
            i = i.lower()
            if w == i:
                return True 
        return False

    def updateScore(self, grid):
        print("word: ",self.word)
        print(self.word[0][0], self.word[0][1])
        w_h = self.horizontal(self.word[0][0], self.word[0][1], grid)
        w_v = self.vertical(self.word[0][0], self.word[0][1], grid)
        w_h = w_h.strip()
        w_v = w_v.strip()
        print("hor:",w_h," ver:", w_v)
        print("is it in here?")
        if (w_h!="" and self.checkWord(w_h)):
            print("checks hor a word:",w_h)
            word_score = 0
            for letter in w_h:
                for letterScore in data.game_data["alphabet_score"]:
                    if letter == letterScore["alphabet"]:
                        word_score += letterScore["score"]
                        self.score += letterScore["score"]
                        g.displayInfo(self.x_goti[0], self.y_goti, self.name, self.score) 
                        print(self.score)
                        break 
            # store score and word in player.json
            file = open(f"{self.name}.json", "a")
            file.write(f"{{{w_h}: {word_score}}}\n")
            file.close()
            j = 0 
            if len(self.gotiList) >= self.x:
                for i in range(len(self.n)):
                    if self.n[i]=="" and j<len(self.word):
                        ran = random.randint(0, len(self.gotiList)-1)
                        self.n[i] = self.gotiList[ran]
                        if (self.n[i] == "-"):
                            self.n[i] = g.choose_l()
                        del self.gotiList[ran]
                        self.word[j][2] = ""
                        j += 1
            else:
                g.gameEnd(g.currentTurn)
                return
            self.word.clear() 
            self.displayGoti()
        elif (w_v!="" and self.checkWord(w_v)):
            word_score = 0
            print("checks ver a word:",w_v)
            for letter in w_v:
                for letterScore in data.game_data["alphabet_score"]:
                    if letter == letterScore["alphabet"]:
                        word_score += letterScore["score"]
                        self.score += letterScore["score"]
                        g.displayInfo(self.x_goti[0], self.y_goti, self.name, self.score)
                        print(self.score) 
                        break
            # store score and word in player.json
            file = open(f"{self.name}.json", "a")
            file.write(f"{{{w_v}: {word_score}}}\n")
            file.close()
            j = 0 
            if len(self.gotiList) >= self.x:
                for i in range(len(self.n)):
                    if self.n[i]=="" and j<len(self.word):
                        ran = random.randint(0, len(self.gotiList)-1)
                        self.n[i] = self.gotiList[ran]
                        if (self.n[i] == "-"):
                            self.n[i] = g.choose_l()
                        del self.gotiList[ran]
                        self.word[j][2] = ""
                        j += 1
            else:
                g.gameEnd(g.currentTurn)
                return
            self.word.clear() 
            self.displayGoti() 
        else:
            print("not word:",w_h,  w_v)
            j = 0 
            for i in range(len(self.n)):
                if self.n[i]=="" and j<len(self.word):
                    self.n[i] = self.word[j][2]
                    self.word[j][2] = ""
                    grid[self.word[j][0]][self.word[j][1]][2] = ""
                    g.drawSquare(grid[self.word[j][0]][self.word[j][1]][0], grid[self.word[j][0]][self.word[j][1]][1], g.randColour(), grid[self.word[j][0]][self.word[j][1]][2])
                    j += 1 
            self.word.clear() 
            self.displayGoti() 
                            
grid = [[[0, 0, ""] for i in range(g.gridSize)] for j in range(g.gridSize)]
grid = g.initializeGrid(grid)
g.displayGrid(grid)        

players = []
name = g.input(1)
player1 = Player(name, 0,250, 400, 8)

name = g.input(2)
player2 = Player(name, 0,250, 200, 8)

name = g.input(3)
player3 = Player(name, 0,250, 0, 8)

name = g.input(4)
player4 = Player(name, 0,250, -200, 8)

players = [player1, player2, player3, player4]

g.turnInfo(g.currentTurn)

def gotiClick(x, y):
    players[g.currentTurn].onClick(x, y, grid)

def updateTurn():
    players[g.currentTurn].updateScore(grid)
    g.currentTurn = (g.currentTurn+1) % len(players)
    g.totalTurns += 1
    if (g.totalTurns > 2*len(players)):
        max = players[0] 
        for p in players:
            if p.score > max.score:
                max = p
        write = open("winner.txt", "w")
        read = open(f"{max.name}.json", "r")
        winner_data = read.read()
        write.write(winner_data)
        write.close()
        read.close()
        # determine player with highest score and make him winner and copy his file to winner.txt
        g.gameEnd(g.currentTurn)
        return 
    g.turnInfo(g.currentTurn)

g.window.onscreenclick(gotiClick)
g.window.onkeypress(updateTurn, "1")
g.window.listen()
g.window.mainloop()
