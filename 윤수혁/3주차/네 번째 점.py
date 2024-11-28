import numpy as np

dots = [(x1 := int(input()), y1 := int(input())), (x2 := int(input()), y2 := int(input())), (x3 := int(input()), y3 := int(input()))]
print(f'dots: ' + str(dots))

unique_x_list = [x1, x2, x3]
unique_y_list = [y1, y2, y3]

def uniqueFinder(unique_list):
    for i in unique_list:
        if i != np.median(unique_list):
            return i

unique_x = uniqueFinder(unique_x_list)
unique_y = uniqueFinder(unique_y_list)

new_dot = (unique_x, unique_y)
print(f'new dot: ' + str(new_dot))