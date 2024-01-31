#Class

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def dist_from_origin(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5


p = Point(1, 4)

print(p.x)
print(p.y)
print(p.dist_from_origin())
