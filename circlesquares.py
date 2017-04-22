import turtle
mt = turtle.Turtle()
#Setting speed at fast level
mt.speed(0)

def sq(l, a):
	for i in range(4):
		mt.forward(l)
		mt.right(a)

for i in range(100):
	sq(100, 90)
	mt.right(11)

# Circle has 360 degrees
# 360 / 10 = 36