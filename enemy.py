from turtle import Turtle


class Enemy(Turtle):
	def __init__(self, xy):
		super().__init__()
		self.shape("triangle")
		self.right(90)
		self.color("red")
		self.shapesize(stretch_wid=1, stretch_len=2)
		self.penup()
		self.speed(3)
		self.setpos(xy)

	def die(self):
		self.hideturtle()
