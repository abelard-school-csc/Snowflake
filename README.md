# Fractal Snowflake Generator

This Python script generates and visualizes fractals by applying Koch curve iterations to an initial regular polygon. The result is a fractal pattern resembling a snowflake or similar intricate structures, depending on the number of sides of the starting polygon and the number of iterations (order).

---

## Features

- **Customizable Order**: Specify the recursion depth for generating fractals, increasing complexity with higher orders.
- **Polygonal Base**: Choose the number of sides for the initial shape (e.g., triangle, square, pentagon).
- **Interactive Visualization**: Displays the fractal using `matplotlib`.

---

## Prerequisites

Before running the script, ensure you have the following Python libraries installed:

- `numpy`: For efficient mathematical computations.
- `matplotlib`: For plotting the generated fractals.

You can install these using pip:

```bash
pip install numpy matplotlib
```

---

## Usage

The script allows you to customize three key parameters:

1. `order`: The recursion depth, which controls the number of fractal iterations.
2. `sides`: The number of sides of the initial polygon (e.g., 3 for a triangle, 4 for a square).
3. `length`: The length of each side of the starting polygon.

### Example

To generate and display a fractal based on a 10-sided polygon with 1 iteration (order):

```python
order = 1  # Number of fractal iterations
sides = 10  # Number of sides for the base polygon
length = 1.0  # Length of each side of the polygon

points = snowflake(order, sides, length)

plt.figure(figsize=(8, 8))
plt.plot(points[:, 0], points[:, 1], 'b-')
plt.axis('equal')
plt.title(f"Fractal with {sides}-sided polygon (Order {order})")
plt.show()
```

This generates and plots the fractal.

---

## How It Works

1. **Base Shape**: The script generates an initial regular polygon (e.g., triangle, square) using trigonometric functions.
2. **Koch Iteration**: 
   - Each side of the polygon is divided into three segments.
   - A new vertex is added to create a triangular "bump" in the middle segment.
   - This process repeats for each recursion level, adding detail with every iteration.
3. **Plotting**: The final points are visualized using `matplotlib`.

---

## Customization Tips

- **Higher `order` Values**: Produces more detailed fractals but increases computation time.
- **Different `sides` Values**: Experiment with polygons like triangles (`sides=3`), pentagons (`sides=5`), or higher.
- **Adjust `length`**: Changes the overall size of the fractal.

---

## Example Outputs

| **Order** | **Sides** | **Fractal Type**                |
|-----------|-----------|----------------------------------|
| 1         | 3         | Classic Koch Snowflake          |
| 2         | 4         | Fractal based on a square       |
| 3         | 5         | Star-like fractal pattern       |
| 1         | 10        | Circular fractal with fine detail|

---

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and share it as you like.

---

## Acknowledgments

- Inspired by classic fractal patterns like the Koch snowflake.
- Special thanks to the Python community for powerful libraries like `numpy` and `matplotlib`.
