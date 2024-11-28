import numpy as np

angles = list(map(int, input().split(" ")))

if max(angles) >= int(np.median(angles)) + min(angles):
    print(sum(angles))
else:
    print(2*(angles[0] + angles[1] - 1))