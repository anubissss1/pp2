# ex 1
import math 
degree = 15
radians = (degree / 180) * math.pi
print(radians)

# ex 2
import math 
a = int(input())
b = int(input())
h = int(input())
print(((a + b) / 2) * h)

# ex 3
import math

n = int(input())
s = float(input())
area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print(round(area,2))

# ex 4
import math 
length_base = int(input())
height = int(input())
print(height * length_base)