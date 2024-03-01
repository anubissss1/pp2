# ex 1
n = int(input())
square_generator = (i*i for i in range(n + 1))
for square in square_generator:
    print(square)

# ex 2
n = int(input())

even_generator = (i for i in range(n + 1) if i % 2 == 0)

print(", ".join(map(str, even_generator)))

# ex 3
n = int(input())

number_generator = (i for i in range(n + 1) if (i % 3 == 0 and i % 4 == 0))

for i in number_generator:
    print(i)

# ex 4
a = int(input())
b = int(input())

number_generator = (i * i for i in range(a , b + 1,1))

for i in number_generator:
    print(i)

# ex 5
n = int(input())

number_generator = (i for i in range(n,-1,-1))

for i in number_generator:
    print(i)