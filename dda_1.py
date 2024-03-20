
import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    x = x1
    y = y1
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment
    return points
x1 = int(input("Enter x-coordinate of first point: "))
y1 = int(input("Enter y-coordinate of first point: "))
x2 = int(input("Enter x-coordinate of second point: "))
y2 = int(input("Enter y-coordinate of second point: "))

points = dda_line(x1, y1, x2, y2)
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]

plt.plot(x_values, y_values, marker='o', color='b')
plt.plot([x1, x2], [y1, y2], marker='o', color='r')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('DDA Algorithm Line Drawing')
plt.grid(True)
plt.show()


