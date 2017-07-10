import math
import random

# number of darts that land inside.
inside = 0

# total number of darts to throw.
total = 10000

# iterate for the number of darts.
for i in range(0, total):
  # generate random point x,y.
  x, y = random.random(), random.random()

  # increment if inside unit circle.
  if math.sqrt((x**2) + (y**2)) < 1.0: inside += 1

# inside / total = pi / 4
estimate = (float(inside) / total) * 4

print(inside, math.pi, estimate)

print ((786.0/1000)*4)
