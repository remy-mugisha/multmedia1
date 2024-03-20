import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    error = int(dx / 2.0)
    y_step = 1 if y1 < y2 else -1
    y = y1
    for x in range(x1, x2 + 1):
        coord = (y, x) if steep else (x, y)
        points.append(coord)
        error -= dy
        if error < 0:
            y += y_step
            error += dx
    if swapped:
        points.reverse()
    return points

x1, y1 = 2, 4
x2, y2 = 10, 15

points = bresenham_line(x1, y1, x2, y2)

x_values = [point[0] for point in points]
y_values = [point[1] for point in points]

plt.plot(x_values, y_values, marker='o', color='b')

plt.plot([x1, x2], [y1, y2], marker='o', color='r')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bresenham\'s Line Drawing Algorithm')

plt.grid(True)
plt.show()


# import matplotlib.pyplot as plt

# def bresenham_line(x1, y1, x2, y2):
#     points = []
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     steep = dy > dx
#     if steep:
#         x1, y1 = y1, x1
#         x2, y2 = y2, x2
#     swapped = False
#     if x1 > x2:
#         x1, x2 = x2, x1
#         y1, y2 = y2, y1
#         swapped = True
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     error = int(dx / 2.0)
#     y_step = 1 if y1 < y2 else -1
#     y = y1
#     for x in range(x1, x2 + 1):
#         coord = (y, x) if steep else (x, y)
#         points.append(coord)
#         error -= dy
#         if error < 0:
#             y += y_step
#             error += dx
#     if swapped:
#         points.reverse()
#     return points

# x1 = int(input("Enter x-coordinate of first point: "))
# y1 = int(input("Enter y-coordinate of first point: "))
# x2 = int(input("Enter x-coordinate of second point: "))
# y2 = int(input("Enter y-coordinate of second point: "))

# points = bresenham_line(x1, y1, x2, y2)

# x_values = [point[0] for point in points]
# y_values = [point[1] for point in points]

# plt.plot(x_values, y_values, marker='o', color='b')

# plt.plot([x1, x2], [y1, y2], marker='o', color='r')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Bresenham\'s Line Drawing Algorithm')
# plt.grid(True)
# plt.show()

