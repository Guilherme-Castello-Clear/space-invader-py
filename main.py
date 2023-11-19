from turtle import Screen, Turtle
from player import Player, Bullet

BULLETS = []

screen = Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=600, height=600)


def create_bullet():
	bullet = Bullet((player.xcor(), player.ycor() + 20))
	BULLETS.append(bullet)

player = Player()

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(create_bullet, "space")

while True:
	for bullet in BULLETS:
		bullet.move()
		if bullet.ycor() > 300:
			print('ok')
			bullet.desapear()
			BULLETS.remove(bullet)
	screen.update()


screen.exitonclick()
