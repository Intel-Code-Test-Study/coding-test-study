angles = list(map(int, input().split(" ")))

count = 0

if angles[0] + angles[1] + angles[2] != 180:
    print('Error')

elif angles[0] == angles[1] == angles[2]:
    print('Equilateral')

elif angles[0] == angles[1] or angles[0] == angles[2] or angles[1] == angles[2]:
    print('Isosceles')

else:
    print('Scalene')