from turtle import Turtle


class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("triangle")
		self.color("white")
		self.shapesize(stretch_wid=1, stretch_len=2)
		self.penup()
		self.speed(1)
		self.goto(0, -250)
		self.left(90)
		self.moving = False

	def move_left(self):
		if not self.moving and self.xcor() > -280:
			print(self.xcor())
			self.moving = True
			self.left(10)
			x = self.xcor()
			x -= 20
			self.setx(x)
			self.right(10)
			self.moving = False

	def move_right(self):
		if not self.moving and self.xcor() < 280:
			self.moving = True
			self.right(10)
			x = self.xcor()
			x += 20
			self.setx(x)
			self.left(10)
			self.moving = False


class Bullet(Turtle):
	def __init__(self, xy):
		super().__init__()
		self.setpos(xy)
		self.shape("triangle")
		self.color("yellow")
		self.shapesize(stretch_wid=0.5, stretch_len=0.5)
		self.penup()
		self.speed = 10

	def move(self):
		self.sety(self.ycor() + self.speed)

	def disappear(self):
		self.hideturtle()
