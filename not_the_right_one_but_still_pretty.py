import matplotlib.pyplot as plt
import numpy as np

def fractal_polygon(order, sides=3, length=1.0):
    angles = np.linspace(0, 2 * np.pi, sides + 1)
    points = np.array([[np.cos(a), np.sin(a)] for a in angles]) * (length / (2 * np.sin(np.pi / sides)))

    def generate_cutout(pA, pB, sides):
        pA_to_B = pB - pA
        segment_length = np.linalg.norm([pA_to_B[0], pA_to_B[1]])
        cutout_vertices = [pA]
        angle = np.arctan2(pA_to_B[1], pA_to_B[0]) + np.pi / sides

        for i in range(sides):
            vertex = cutout_vertices[-1] + np.array([segment_length * np.cos(angle), segment_length * np.sin(angle)])
            cutout_vertices.append(vertex)
            angle += 2 * np.pi / sides

        cutout_vertices.append(pB)
        return np.array(cutout_vertices)

    def subdivide_polygon(points, sides):
        new_points = []
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            pA = p1 + (p2 - p1) / 3
            pB = p1 + 2 * (p2 - p1) / 3
            cutout = generate_cutout(pA, pB, sides)
            new_points.append(p1)
            new_points.extend(cutout)
        new_points.append(points[-1])
        return new_points

    for _ in range(order):
        points = subdivide_polygon(points, sides)

    return np.array(points)

order = 6
sides = 8
length = 1.0

points = fractal_polygon(order, sides, length)

plt.figure(figsize=(8, 8))
plt.plot(points[:, 0], points[:, 1], 'b-')
plt.axis('equal')
plt.title(f"Fractal Polygon with {sides} sides (Order {order})")
plt.show()
