import matplotlib.pyplot as plt
import numpy as np

def snowflake(order, sides=3, length=1.0):
    angles = np.linspace(0, 2 * np.pi, sides + 1)
    points = np.array([[np.cos(a), np.sin(a)] for a in angles]) * (length / (2 * np.sin(np.pi / sides)))

    def koch_iteration(points):
        new_points = []
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            pA = p1 + (p2 - p1) / 3
            pB = p1 + 2 * (p2 - p1) / 3
            dx, dy = pB - pA
            length = np.sqrt(dx**2 + dy**2)
            angle = np.arctan2(dy, dx) + np.pi / 3
            pC = pA + np.array([length * np.cos(angle), length * np.sin(angle)])
            new_points.extend([p1, pA, pC, pB])
        new_points.append(points[-1])
        return np.array(new_points)

    for _ in range(order):
        points = koch_iteration(points)

    return points

order = 1
sides = 10
length = 1.0

points = snowflake(order, sides, length)

plt.figure(figsize=(8, 8))
plt.plot(points[:, 0], points[:, 1], 'b-')
plt.axis('equal')
plt.title(f"Fractal with {sides}-sided polygon (Order {order})")
plt.show()
