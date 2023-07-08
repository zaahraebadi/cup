import trimesh
import pyrender

# Prompt user for the directory of the OBJ file
obj_file = input("Enter the directory of the OBJ file: ")

# Load OBJ file
mesh = trimesh.load_mesh(obj_file)

# Create a pyrender scene and add the mesh to it
scene = pyrender.Scene()
scene.add(pyrender.Mesh.from_trimesh(mesh))

# Create a pyrender viewer
viewer = pyrender.Viewer(scene, use_raymond_lighting=True)

# Keep the viewer open until it's closed
while not viewer.is_active:
    viewer.render_lock.release()

viewer.close()
