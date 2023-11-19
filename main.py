import random
from turtle import Screen, Turtle
from enemy import Enemy
from player import Player, Bullet

BULLETS = []
ENEMIES = []

screen = Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=600, height=600)


def generate_enemy():
	enemy = Enemy((random.randint(-200, 200), random.randint(100, 250)))
	ENEMIES.append(enemy)

def create_bullet():
	bullet = Bullet((player.xcor(), player.ycor() + 20))
	BULLETS.append(bullet)


player = Player()

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(create_bullet, "space")
generate_enemy()

while True:

	if len(ENEMIES) < 5:
		generate_enemy()
		print(len(ENEMIES))

	for bullet in BULLETS:
		bullet.move()
		if bullet.ycor() > 300:
			print('ok')
			bullet.disappear()
			BULLETS.remove(bullet)
		for enemy in ENEMIES:
			if bullet.distance(enemy) < 20:
				bullet.disappear()
				BULLETS.remove(bullet)
				enemy.die()
				ENEMIES.remove(enemy)

	screen.update()

