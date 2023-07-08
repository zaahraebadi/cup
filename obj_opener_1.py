import trimesh
import pyrender

obj_file = r"C:\Users\zhr\Desktop\cup.obj"
mesh = trimesh.load_mesh(obj_file)

scene = pyrender.Scene()
scene.add(pyrender.Mesh.from_trimesh(mesh))

viewer = pyrender.Viewer(scene, use_raymond_lighting=True)

while not viewer.is_active:
    viewer.render_lock.release()

viewer.close()
