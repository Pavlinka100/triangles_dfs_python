from turtle import Turtle
import math

pen = Turtle()
pen.up()
class AllTriangles():
    def __init__(self):
        self.all_white_subtriangles = []
        self.all_black_subtriangles = []
class Triangle():
    def __init__(self):
        self.nodes = []
        self.color = "white"
        self.white_subtriangles = []
        self.black_subtriangles = []
        self.level = 1
    def create_triangle(self, line=600):
        node_a = (0-line/2, -line/2)
        node_b = (0+line/2, -line/2)
        node_c = (0,(-line/2)+ math.sqrt((line * line) - ((line / 2) * (line / 2))))
        self.nodes = [node_a, node_b, node_c]

    def draw_white_triangle(self):
        pen.goto(self.nodes[0])
        pen.down()
        pen.goto(self.nodes[1])
        pen.goto(self.nodes[2])
        pen.goto(self.nodes[0])
        pen.up()

    def split(self):
        """This method takes a triangle and splits it to the 3 same white subtriangles and one black"""
        node_a = self.nodes[0]
        node_b = self.nodes[1]
        node_c = self.nodes[2]

        #node between A and B has the same ycor and is in the middle of the two points
        node_ab = (node_b[0] - (node_b[0] - node_a[0]) / 2, node_a[1])

        # node between B and C is in the middle of the two points
        node_bc = (node_b[0] - ((node_b[0] - node_ab[0]) / 2), node_c[1] - ((node_c[1] - node_b[1])/2))

        # node between A and C is in the middle of the two points
        node_ca = (node_c[0]-((node_ab[0] - node_a[0]) / 2), node_c[1] - ((node_c[1] - node_a[1])/2))

        black = Triangle()
        black.color = "black"
        black.nodes = [node_ab, node_bc, node_ca]
        black.level = self.level + 1
        #black = split_to_create_black(self)

        self.black_subtriangles.append([black])

        #create 3 white subtriangles
        white_a = Triangle()
        white_a.level = self.level +1
        white_a.nodes = [node_a, node_ab, node_ca]
        self.white_subtriangles.append([white_a])
        #print(f"white a {white_a}")

        white_b = Triangle()
        white_b.nodes = [node_ab, node_b, node_bc]
        white_b.level = self.level + 1
        self.white_subtriangles.append(white_b)

        white_c = Triangle()
        white_c.nodes = [node_ca, node_bc, node_c]
        white_c.level = self.level + 1
        self.white_subtriangles.append(white_c)

        black.draw_black()
        return white_a, white_b, white_c, black

    def draw_black(self):
        pen.fillcolor("black")
        pen.begin_fill()
        for node in self.nodes:
            pen.goto(node)
        pen.goto(self.nodes[0])
        pen.end_fill()
        pen.up()
