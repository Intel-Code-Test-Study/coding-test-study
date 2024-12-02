import numpy as np

angles = list(map(int, input().split(" ")))

if max(angles) >= int(np.median(angles)) + min(angles):
    print('Invalid')

elif angles[0] == angles[1] == angles[2]:
    print('Equilateral')

elif angles[0] == angles[1] or angles[0] == angles[2] or angles[1] == angles[2]:
    print('Isosceles')

else:
    print('Scalene')