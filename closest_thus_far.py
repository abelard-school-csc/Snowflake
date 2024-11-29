import matplotlib.pyplot as plt
import numpy as np

def fractal_shape(order, sides=3, length=1.0):
    angles = np.linspace(0, 2 * np.pi, sides + 1)
    radius = length / (2 * np.sin(np.pi / sides))
    points = np.array([[np.cos(a), np.sin(a)] for a in angles]) * radius

    def add_fractal_cutouts(points):
        new_points = []
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            pA = p1 + (p2 - p1) / 3
            pB = p1 + 2 * (p2 - p1) / 3
            edge_vector = pB - pA
            edge_length = np.linalg.norm(edge_vector)
            cutout_radius = edge_length / (2 * np.sin(np.pi / sides))
            cutout_center = pA + edge_vector / 2
            cutout_angle = np.arctan2(edge_vector[1], edge_vector[0])
            cutout_angles = np.linspace(0, 2 * np.pi, sides + 1)[:-1]
            cutout_vertices = [
                cutout_center + cutout_radius * np.array([
                    np.cos(cutout_angle + angle), 
                    np.sin(cutout_angle + angle)
                ])
                for angle in cutout_angles
            ]
            new_points.extend([p1, pA])
            new_points.extend(cutout_vertices)
            new_points.append(pB)
        new_points.append(points[-1])
        return np.array(new_points)

    for _ in range(order):
        points = add_fractal_cutouts(points)

    return points

order = 2
sides = 4
length = 1.0

points = fractal_shape(order, sides, length)

plt.figure(figsize=(8, 8))
plt.plot(points[:, 0], points[:, 1], 'b-')
plt.axis('equal')
plt.title(f"Fractal Shape (Order {order}, Sides {sides})")
plt.show()
