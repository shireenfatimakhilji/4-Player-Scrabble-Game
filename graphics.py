import turtle
import random 

window = turtle.Screen()
window.bgcolor("black")
window.title("SCRABBLE")
window.setup(width=1000, height=500)

draw = turtle.Turtle()
draw.speed(1000)
draw.pensize(2)
gridSize = 15
cellSize = 40

selLetter = ""
currentTurn = 0
totalTurns = 0

colours = ["magenta", "coral", "lightblue", "lightgray", "orange"]

draw.hideturtle()

def randColour():
    return random.choice(colours)

def drawSquare( x, y, c, letter=""):
    draw.fillcolor(c)
    draw.begin_fill()
    draw.penup()
    draw.goto(x, y)
    draw.pendown()
    for i in range(4):
        draw.forward(cellSize)
        draw.right(90)
    draw.end_fill()
    draw.penup()
    draw.goto(x+20, y-30)
    draw.pendown()
    draw.write(letter, align="center", font=("Arial", 15, "normal"))
    draw.penup()    

def input(x):
    name = turtle.textinput("Name input", f"Enter name of Player {x}")
    return name

def initializeGrid(grid):
    x_start = -cellSize**1.75 
    y_start = cellSize**1.6
    x = x_start
    y = y_start
    for i in range(gridSize):
        for j in range(gridSize):
            grid[i][j] = [x, y, ""]
            x += cellSize
        x = x_start
        y -= cellSize
    return grid

def displayGrid(grid):
    for i in range(gridSize):
        for j in range(gridSize):
            drawSquare(grid[i][j][0], grid[i][j][1], randColour(), grid[i][j][2])

def displayPlayerGoti(n, x_start, y_start, name, score):
    displayInfo(x_start[0], y_start, name, score)
    draw.color("black")
    for i in range(len(n)):
        drawSquare(x_start[i], y_start, randColour(), n[i])
    draw.penup()
    draw.color("black")

def displayInfo(x, y, name, score):
    draw.fillcolor("black")
    draw.penup()
    draw.goto(x, y + (cellSize/2)+30)
    draw.begin_fill()
    draw.forward(400)
    draw.right(90)
    draw.forward(40)
    draw.right(90)
    draw.forward(400)
    draw.right(90)
    draw.forward(40)
    draw.right(90)
    draw.end_fill()
    draw.penup()
    draw.goto(x, y + (cellSize/2))
    draw.pendown()
    draw.color("white")    
    draw.write(f"{name}'s Score: {score}", align="left", font=("Arial", 15, "normal"))

def initializeX(length, x_goti):
    x_coor = x_goti[0]
    for i in range(1, length):
        x_coor += cellSize
        x_goti.append(x_coor)
    return x_goti

def turnInfo(currentTurn):
    draw.fillcolor("black")
    draw.penup()
    draw.goto(-cellSize-gridSize, -cellSize*8+25)
    draw.begin_fill()
    draw.forward(400)
    draw.right(90)
    draw.forward(200)
    draw.right(90)
    draw.forward(400)
    draw.right(90)
    draw.forward(200)
    draw.right(90)
    draw.end_fill()
    draw.penup()
    draw.goto(-cellSize-gridSize, -cellSize*8)
    draw.pendown()
    draw.color("white")    
    draw.write(f"Player {currentTurn+1}'s turn (Press 1 to finish turn)", align="left", font=("Arial", 15, "normal"))
    draw.color("black")

def gameEnd(c):
    draw.penup()
    draw.goto(-50, -290)
    draw.pendown()
    draw.color("pink")    
    draw.write(f"Player {c+1} has won", align="left", font=("Arial", 15, "normal"))
    draw.color("black") 

def choose_l():
    ch = turtle.textinput("Letter Choice", "Enter any letter of your choice")
    return ch 