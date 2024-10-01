#see readme.md

from turtle import Turtle, Screen
from triangles import AllTriangles, Triangle


line = 600

def draw_triangles_depth(triangle, number):
    """This function takes number as level of recursion (or number of the triangle) and calls itself on the subtriangles based on DFS"""
    if number == 1:
        screen.update()
        triangle.draw_white_triangle()
        all_triangles.all_white_subtriangles.append(triangle)
    if number > 1 and triangle.level < number:
        screen.update()

        # draw a basic triangle
        triangle.draw_white_triangle()

        #split triangles with the black one and draw it
        white_a, white_b, white_c, black = triangle.split()

        #update lists of black and white subtriangles
        all_triangles.all_white_subtriangles.append(white_a)
        all_triangles.all_white_subtriangles.append(white_b)
        all_triangles.all_white_subtriangles.append(white_c)
        all_triangles.all_black_subtriangles.append(black)


        draw_triangles_depth(white_a, number)
        draw_triangles_depth(white_b, number)
        draw_triangles_depth(white_c, number)

#setup screen, pen for triangles, writing pen and initiate triangle and all_triangles white and black lists
screen = Screen()
screen.setup(800, 800)
screen.tracer(0)

number = int(screen.numinput("Triangles","Insert number from 1 to 10: ",  minval=1, maxval=10))

wr_pen = Turtle()
wr_pen.up()
wr_pen.hideturtle()
triangle = Triangle()
triangle.create_triangle()
all_triangles = AllTriangles()

#run the main logic and create all subtriangles and draw them
draw_triangles_depth(triangle, number)

#count subtriangles and print their counts
white_shape_count = 0
for shape in all_triangles.all_white_subtriangles:
   if shape.level == number:
       white_shape_count += 1
print(f"white shape count is {white_shape_count}")

for shape in all_triangles.all_black_subtriangles:
   print(shape.nodes, shape.level)
print(f"black shape count is {len(all_triangles.all_black_subtriangles)}")


#this part writes black and white counts on the screen
wr_pen.color("black")
wr_pen.pensize(3)
wr_pen.goto(-100, 300)
wr_pen.showturtle()
wr_pen.write(f"Level {number}", font=('Arial', 30, 'normal'))
wr_pen.goto(-300, 280)
wr_pen.write(f"White count: {white_shape_count}", font=('Arial', 20, 'normal'))
wr_pen.goto(-300, 280)
wr_pen.goto(100, 280)
wr_pen.write(f"Black count: {len(all_triangles.all_black_subtriangles)}", font=('Arial', 20, 'normal'))

screen.exitonclick()
