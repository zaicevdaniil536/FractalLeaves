import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_leaves():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    leaves = f.generate()
    # Add noise to the fractal shape to make it look more like leaves
    noise = np.random.normal(0, 0.05, leaves.shape)
    leaves = leaves + noise
    leaves = np.clip(leaves, 0, 1)
    # Apply a leaves-like color map to the fractal shape
    leaves = plt.cm.Greens(leaves)
    # Return the fractal leaves
    return leaves

# Generate 10 fractal leaves images
for i in range(10):
    leaves = generate_fractal_leaves()
    plt.imsave("fractal_leaves_{}.png".format(i), leaves)
