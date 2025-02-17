import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(3)

# Start drawing the heart
pen.begin_fill()

pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)

pen.end_fill()

# Move the pen to a position to write the name
pen.penup()
pen.goto(30,40)  # Adjust this position based on where you want the text
pen.pendown()

# Write the name inside the heart
pen.color("white")  # Set the color of the text
pen.write("Nisha Ranjan", align="center", font=("Arial", 16, "bold"))

# Hide the turtle after drawing
pen.hideturtle()

# Keep the window open
turtle.done()
