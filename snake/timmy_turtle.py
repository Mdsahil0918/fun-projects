import turtle as t
import random

# Create the turtle object
timmy = t.Turtle()

# Set colormode to 255 (RGB mode)
t.colormode(255)

# Function to generate random RGB colors
def random_color():
    r = random.randint(0, 255)  # Random red value between 0 and 255
    g = random.randint(0, 255)  # Random green value between 0 and 255
    b = random.randint(0, 255)  # Random blue value between 0 and 255
    return (r, g, b)  # Return the RGB color tuple

# Directions the turtle can face
directions = [0, 90, 180, 270]

# Set the pen width and speed
timmy.width(5)
timmy.speed(10)  # Set speed to fastest (10)
 
for _ in range(100):
    timmy.color(random_color())  # Set random color
    timmy.forward(30)  # Move the turtle forward by 30 units
    timmy.setheading(random.choice(directions))  # Change direction randomly

# Close the turtle graphics window when clicked
t.done()
 