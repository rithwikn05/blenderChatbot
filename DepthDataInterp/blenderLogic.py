# import bpy
import numpy as np
from txtToTensor import main_method
# This function adds a cube at the specified location
def create_cube(x, y, z, size):
    print(f"bpy.ops.mesh.primitive_cube_add(size={size}, location={x, y, z})")

# This function generates the Blender script for the 3D object
def generate_blender_script(dimensions, tensors):
    size = 1  # Assuming each block is 1x1x1
    placed_blocks = set()

    depth, height, width = dimensions

    # Process each view tensor and generate blocks
    for view, tensor in tensors.items():
        for i in range(tensor.shape[0]):
            for j in range(tensor.shape[1]):
                depth_value = tensor[i, j]
                if depth_value >= 0 and depth_value < depth:
                    if view == "front":
                        x, y, z = j, height - i -1, depth_value
                    elif view == "back":
                        x, y, z = width - j -1 ,height - i -1, depth - depth_value -1
                    elif view == "left":
                        x, y, z = depth_value ,height - 1 - i, depth - 1 - j
                    elif view == "right":
                        x, y, z = width - depth_value - 1, height - i - 1, j
                    elif view == "top":
                        x, y, z = j, height - depth_value - 1, depth - i -1
                    elif view == "bottom":
                        x, y, z = j, depth_value,  i
                    position = (x, y, z)
                    if position not in placed_blocks:
                        create_cube(x, y, z, size)
                        placed_blocks.add(position)

# Example usage with 3x3x3 dimensions and tensors
dimensions = (256, 256, 256)


tensors = {
    "front":main_method(),
    "back": main_method(),
    "left": main_method(),
    "right": main_method(),
    "top":main_method(),
    "bottom": main_method()
}

# tensors = {
#     "front":np.array([
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 2, 3, 2, 0, 0, 0],
#     [0, 0, 1, 3, 3, 3, 1, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 2, 3, 4, 3, 2, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 1, 3, 3, 2, 1, 0, 0],
#     [0, 0, 1, 1, 2, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0]
# ]),
#     "back": np.array([
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 2, 3, 2, 0, 0, 0],
#     [0, 0, 1, 3, 3, 3, 1, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 2, 3, 4, 3, 2, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 1, 3, 3, 2, 1, 0, 0],
#     [0, 0, 1, 1, 2, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0]
# ]),
#     "left": np.array([
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 2, 3, 2, 0, 0, 0],
#     [0, 0, 1, 3, 3, 3, 1, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 2, 3, 4, 3, 2, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 1, 3, 3, 2, 1, 0, 0],
#     [0, 0, 1, 1, 2, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0]
# ]),
#     "right": np.array([
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 2, 3, 2, 0, 0, 0],
#     [0, 0, 1, 3, 3, 3, 1, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 2, 3, 4, 3, 2, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 1, 3, 3, 2, 1, 0, 0],
#     [0, 0, 1, 1, 2, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0]
# ]),
#     "top":np.array([
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 2, 3, 2, 0, 0, 0],
#     [0, 0, 1, 3, 3, 3, 1, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 2, 3, 4, 3, 2, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 1, 3, 3, 2, 1, 0, 0],
#     [0, 0, 1, 1, 2, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0]
# ]),
#     "bottom": np.array([
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 2, 3, 2, 0, 0, 0],
#     [0, 0, 1, 3, 3, 3, 1, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 2, 3, 4, 3, 2, 0, 0],
#     [0, 0, 2, 3, 3, 3, 2, 0, 0],
#     [0, 0, 1, 3, 3, 2, 1, 0, 0],
#     [0, 0, 1, 1, 2, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0]
# ])
# }


generate_blender_script(dimensions, tensors)
