import turtle as t
import random
import time

screen = t.Screen()
screen.title("Maze")
def display_message(msg):
    pen = t.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 250) 
    pen.color("Indigo")
    pen.write(msg, align="center", font=("Times New Roman", 16, "bold"))

mode=None
walls=[]
def no_wall(x, y):
    for wall in walls:
        buffer = 5
        min_x, min_y, max_x, max_y = wall
        if min_x - buffer <= x <= max_x + buffer and min_y - buffer <= y <= max_y + buffer:
            return False
    return True

def maze():
    maze = t.Turtle()
    maze.speed(0)
    maze.penup()
    maze.goto(-200, 200)
    maze.pendown()
    maze.pensize(5)
    def record_wall(start_x, start_y, end_x, end_y):
        buffer = 5
        min_x = min(start_x, end_x)
        max_x = max(start_x, end_x)
        min_y = min(start_y, end_y)
        max_y = max(start_y, end_y)
        walls.append((min_x - buffer, min_y - buffer, max_x + buffer, max_y + buffer))
    start_x, start_y = maze.position()
    maze.forward(100)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(100)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.penup()
    maze.backward(50)
    maze.left(90)  
    maze.pendown()
    start_x, start_y = maze.position()
    maze.forward(100)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.penup()
    maze.backward(50)
    maze.right(90)
    maze.pendown()
    start_x, start_y = maze.position()
    maze.forward(150) ## down
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.left(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.left(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.left(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.penup()
    maze.goto(-50,0)  
    maze.pendown()
    maze.left(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.left(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.penup()
    maze.left(90)
    maze.goto(-50, 200)
    maze.pendown()
    start_x, start_y = maze.position()
    maze.forward(150)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    start_x, start_y = maze.position()
    maze.backward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor()) 
    maze.left(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.backward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.left(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(100)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.penup()
    maze.goto(100,50)
    maze.pendown()
    start_x, start_y = maze.position()
    maze.backward(150)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.left(90)
    start_x, start_y = maze.position()
    maze.forward(150)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.penup()
    maze.backward(50)
    maze.left(90)
    maze.pendown()
    start_x, start_y = maze.position()
    maze.forward(150)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.left(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.penup()
    maze.left(90)
    maze.forward(50)
    maze.pendown()
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(100)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.penup()
    maze.backward(50)
    maze.pendown()
    maze.left(90)
    start_x, start_y = maze.position()
    maze.forward(100)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.penup()
    maze.left(90)
    maze.forward(50)
    maze.right(90)
    maze.backward(100)
    maze.pendown()
    start_x, start_y = maze.position()
    maze.forward(150)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor())
    maze.right(90)
    start_x, start_y = maze.position()
    maze.forward(50)
    record_wall(start_x, start_y, maze.xcor(), maze.ycor()) 
    maze.penup() 
    maze.goto(-200,0)
maze()

goals=[(-100,200,-50,200),(-200,0,-200,-50)]
def check_goal(x, y): 
    buffer = 10 
    for goal in goals:
        x1, y1, x2, y2 = goal
        if (min(x1, x2) - buffer<= x <= max(x1, x2)+ buffer and min(y1, y2) - buffer <= y <= max(y1, y2)+ buffer):
            print("Goal reached!")
            if mode == "p":
                display_message("Goal Reached! You Win!")
                screen.ontimer(t.bye, 3000)
            return True
    return False
def spawn_point():  
    while True:
        x = random.randint(-200, 100)
        y = random.randint(-100, 200)
        if no_wall(x, y):
            return x, y
player = t.Turtle()
player.shape("turtle")
player.color("teal")
player.penup()
player.left(90)
spawn_x, spawn_y = spawn_point()
player.goto(spawn_x, spawn_y)

def move_up():
    x,y=player.position()
    if no_wall(x,y+20):
        player.goto(x,y+20)
    if check_goal(x,y+20):
        player.color("gold") 
        
def move_down():
    x,y=player.position()
    if no_wall(x,y-20):
        player.goto(x,y-20)
    if check_goal(x,y-20):
        player.color("gold")
        
def move_left():
    x,y=player.position()
    if no_wall(x-20,y):
        player.goto(x-20,y)
    if check_goal(x-20,y):
        player.color("gold") 
         
def move_right():
    x,y=player.position()
    if no_wall(x+20,y):
        player.goto(x+20,y)
    if check_goal(x+20,y):
        player.color("gold")

        

#for automating
def auto_solve():
    start = (int(player.xcor()), int(player.ycor()))
    queue = [(start, [start])]
    visited = set([start])
    step = 20 

    moves = [(0, step), (0, -step), (step, 0), (-step, 0)]

    while queue:
        (x, y), path = queue.pop(0)

        if check_goal(x, y):
            return path  # Found path to goal

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and no_wall(nx, ny):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return None

def follow_path(path):
    for (x, y) in path:
        player.goto(x, y)
        screen.update()
        time.sleep(0.1)
    player.color("gold")
    screen.ontimer(t.bye, 3000)
def start_auto():
    path = auto_solve()
    if path:
        follow_path(path)
    else:
        print("No path found!")

screen.onkey(start_auto, "a")  

def game():
    global mode
    mode = screen.textinput("Maze Game", "Choose mode: P for Player, A for Auto").lower()

    if mode == "p":
        screen.onkey(move_up, "Up")
        screen.onkey(move_down, "Down")
        screen.onkey(move_left, "Left")
        screen.onkey(move_right, "Right")
        screen.listen()

    elif mode == "a":
        path = auto_solve()
        if path:
            follow_path(path)
        else:
            print("No path found!")

    else:
        print("Invalid choice! Please restart and enter P or A.")

game()
t.done()
