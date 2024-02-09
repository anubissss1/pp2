array = [i for i in range(1, 101)]

array = filter(lambda a: sum([1 for i in range(1, a + 1) if a % i == 0]) == 2, array)

print(*array)