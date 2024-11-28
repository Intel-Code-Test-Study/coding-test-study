points = list(map(int , input().split(" ")))

point_list = []
for i in range(len(points)):
    if i % 2 != 0:
        if i == 0:
            continue
        else:
            point = []
            point.append(points[i-1])
            point.append(points[i])
            point_list.append(point)

x_point_list = []
for i in range(len(point_list)):
    for j in range(len(point_list[i])):
        if j % 2 == 0:
            x_point_list.append(point_list[i][j])

y_point_list = []
for i in range(len(point_list)):
    for j in range(len(point_list[i])):
        if j % 2 != 0:
            y_point_list.append(point_list[i][j])

length_x = abs(max(x_point_list) - min(x_point_list))
length_y = abs(max(y_point_list) - min(y_point_list))
square = length_x * length_y
print(square)