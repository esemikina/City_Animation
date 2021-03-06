######################################################
# Project: A Turtle Graphics scene 
# Student Name:  Semikina Yelizaveta 
# UIN: 670246811
# URL: https://trinket.io/library/trinkets/69adce50e0
######################################################
#!/bin/python3

# imports
import turtle 
import random

# globals
t = None
screen = None
screen_width = None
screen_height = None

# initial settings for global variables
t = turtle.Turtle() 
t.speed(5000)
screen = t.getscreen()
screen_width = 500
screen_height = 420

# function definitions
def draw_rectangle(x1, y1, w, h, color = "#EEEEEE"):
  t.fillcolor(color) 
  t.speed(5000)
  t.penup()
  t.goto(x1, y1)
  t.pendown()
  t.begin_fill()
  t.forward(w)
  t.left(90)
  t.forward(h)
  t.left(90)
  t.forward(w)
  t.left(90)
  t.forward(h)
  t.left(90)
  t.end_fill()
  
def draw_door(x, y):
  door_color = "#800000"
  draw_rectangle(x,y,10,15, door_color)
  t.penup()
  t.goto(x+3,y+5)
  t.pendown()
  t.circle(1)

def draw_window(x, y):
  window_color = "#ffffff"
  draw_rectangle(x,y,5,15,window_color) 
  draw_rectangle(x+5,y,5,15,window_color)
  draw_rectangle(x+10,y,5,15,window_color)
  draw_rectangle(x+15,y,5,15,window_color)

def draw_town():
  building_color = "#d16400"
  # draw 3 buildings
  #building in the middle
  draw_rectangle(-25,-160,40,230,building_color)
  # windows 1
  draw_window(-15, -120)
  draw_window(-15, -80)
  draw_window(-15, -40)
  draw_window(-15, 0)
  draw_window(-15, 40)
  # door
  draw_door(-10, -160)
  
   #building on left
  draw_rectangle(-85,-160,60,100,building_color)
  # windows 2
  draw_window(-65, -100) 
  draw_window(-65, -130)
  # door
  draw_door(-58, -160)
    
  #building on right
  draw_rectangle(15,-160,55,135,building_color)
  # windows 3
  draw_window(34, -120)
  draw_window(34, -80)
  # door
  draw_door(38, -160)
  

def draw_sun():
  sun_color_array = ["#E9967A", "#F08080", "#CD5C5C", "#DC143C"]
  t.speed(5000)
  t.penup()
  t.goto(0,-200)
  t.pendown()
  for i in range(25, 1, -3):
    chosen_color = random.choice(sun_color_array)
    t.color(chosen_color)
    t.fillcolor(chosen_color)
    t.begin_fill()
    t.circle(10*i)
    t.end_fill()
  t.penup()
  t.color("#000000")

def draw_snow():
    for i in range(100):
      t.penup()
      t.speed(5000)
      t.color("#eeeeee")
      t.setposition(random.randint(-240, 240), random.randint(-200, 200))
      t.fillcolor("#ffffff")
      t.begin_fill()
      t.pendown()
      t.circle(random.randint(1,3))
      t.end_fill()
      
def writeToScreen(text):
  t.fillcolor('black')
  t.begin_fill()
  screen.tracer(1);
  t.speed(1000);
  t.penup()
  t.setposition(-150, 140)
  t.pendown()
  t.write(text,move=False, font=("Arial", 40, "normal"))
  t.end_fill()
def draw_background():
  water_color = "#5dbcd2";
  # draw sun
  draw_sun()
  # draw water
  draw_rectangle(-250,-210,492,50, water_color)
# Main
def main():
  backgrounColorsArr = ["#E9967A", "#F08080", "#CD5C5C", "#DC143C", "#FF6347", "#FF4500"]
  # setup screen 
  screen.setup(screen_width, screen_height)
  screen.bgcolor(random.choice(backgrounColorsArr))
  screen.tracer(100);
  # draw background
  draw_background()
  # town
  draw_town()
  # add some snow
  draw_snow()
  # write text
  writeToScreen("Stepnogorsk!")
  # hide
  t.hideturtle()
  

main()