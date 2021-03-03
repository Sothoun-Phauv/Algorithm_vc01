
import tkinter as tk
import random
import winsound

# start code
root = tk.Tk()
root.geometry("1000x700")
root.title("Crazy Game")
canvas = tk.Canvas(root)

# create background

bg = tk.PhotoImage(file = "images/sky.png")
background_windows = canvas.create_image(500, 350, image = bg)
enemy = tk.PhotoImage(file = "images/scar.png")
monster3 = canvas.create_image(400, 300, image = enemy)
# create bullets

bullets = tk.PhotoImage(file = "images/shoot.png")
# create killer

sky = tk.PhotoImage(file = "images/plane.png")
airplane_fly = canvas.create_image(500, 635, image = sky)

# create aviarable
Scores = 0
x = 500
x1 = 200
x2 =800
y = 0
# create monster

monster = tk.PhotoImage(file = "images/mounster.png")
monster1 = canvas.create_image(100, 50, image = monster)
pop = tk.PhotoImage(file = "images/pop.png")
monster2 = canvas.create_image(600, 50, image = pop)
tent = tk.PhotoImage(file = "images/tent.png")
monster3 = canvas.create_image(700, 50, image = tent)
# create score
canvas.create_text(50,30, text = "Score: 0", fill = "red",font = 50)
canvas.create_text(45,60, text = "Life: 3", fill = "red",font = 50)
# function bullets

def Rockets():
    global leftBullet, rightBullet, middleBullet
    canvas.move(leftBullet, 0, -15)
    canvas.move(rightBullet, 0, -15)
    canvas.move(middleBullet,0, -15)
    position = canvas.coords(leftBullet)[1]
    Shooting = position <= 0
   
    
    if not Shooting:
        canvas.after(10, lambda: Rockets())
    else:
        canvas.delete(leftBullet)
        canvas.delete(rightBullet)
        canvas.delete(middleBullet)
        Shoot()
# function enemies



def Shoot():
    global airplane_fly, leftBullet, rightBullet,middleBullet, bullets, Rockets
    X1 = canvas.coords(airplane_fly)[0]
    Y1 = canvas.coords(airplane_fly)[1]
    leftBullet = canvas.create_image(X1 - 20, Y1 + 120, image = bullets)
    middleBullet = canvas.create_image(X1 +0, Y1 + 90, image = bullets)
    rightBullet = canvas.create_image(X1 + 20, Y1 + 120, image = bullets)
    Rockets()

# function move

def moveLeft(event):
    if canvas.coords(airplane_fly)[0] > 50:
        canvas.move(airplane_fly, -20, 0)
  

def moveRight(event):
    if canvas.coords(airplane_fly)[0] < 950:
        canvas.move(airplane_fly, 20, 0)
   

def moveUp(event):
    if canvas.coords(airplane_fly)[1]>50:
        canvas.move(airplane_fly, 0, -20)
   

def moveDown(event):
    if canvas.coords(airplane_fly)[1] < 650:
        canvas.move(airplane_fly, 0, 20)
   

# funtion enemy
def move() :
    global x,y,monster1
    
    canvas.moveto(monster1,x,y)
    if y <660 :
        y += 40
        canvas.after(300,lambda:move())
    else:
        y=0
        canvas.after(300,lambda:move())
def move1() :
    global x1,y,monster2
    canvas.moveto(monster2,x1,y)
    if y <660 :
        y += 40
        canvas.after(500,lambda:move1())
    else:
        y=0
        canvas.after(500,lambda:move1())
def move2() :
    global x,y,monster3
    canvas.moveto(monster3,x2,y)
    if y <660 :
        y += 40
        canvas.after(800,lambda:move2())
    else:
        y=0
        canvas.after(800,lambda:move2())
# function damage
# def impactBullets(bullets,monster):
    
# if impactBulletsMonster(bullets,monster):
#     delete monster
# if not Shootchooting and not impact:
#     canvas.after(Rockets)
# else:
#     canvas.delete
#     shoot()
# create sound
winsound.PlaySound("sound/gameover3",winsound.SND_FILENAME)
#Function Call
Shoot()
move()
move1()
move2()
# key event

canvas.bind_all("<Left>", moveLeft)
canvas.bind_all("<Right>", moveRight)
canvas.bind_all("<Up>", moveUp)
canvas.bind_all("<Down>", moveDown)

# root
root.resizable(False,False)
canvas.pack(expand=True,fill="both")
root.mainloop()