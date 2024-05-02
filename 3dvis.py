import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
# Path to the uploaded PLY file
ply_path = 'Predicted Point.ply'

print("lmao")
# Load the point cloud from the file
point_cloud = o3d.io.read_point_cloud(ply_path)
# Let's say we want to color the points based on the z coordinate (height)
points = np.asarray(point_cloud.points)
colors = np.zeros(points.shape)  # Initialize colors array

# Normalize z values to the 0-1 range for color mapping
z_min = np.min(points[:, 2])
z_max = np.max(points[:, 2])
z_normalized = (points[:, 2] - z_min) / (z_max - z_min)

# Apply a colormap (matplotlib colormaps can be used)
colormap = plt.get_cmap("viridis")
colors = colormap(z_normalized)[:, :3]  # Exclude the alpha channel

# Assign the colors to the point cloud
point_cloud.colors = o3d.utility.Vector3dVector(colors)

# Save the colored point cloud if you want
o3d.io.write_point_cloud("colored_point_cloud.ply", point_cloud)

# Visualize the point cloud (if you're running this on your local machine)
o3d.visualization.draw_geometries([point_cloud])