import bpy
import math


# Creating Collections
base_collection    = bpy.data.collections.new("Base")
lights_collection  = bpy.data.collections.new("Lights")
objects_collection = bpy.data.collections.new("Objects")
scene = bpy.context.scene
scene.collection.children.link(base_collection)
scene.collection.children.link(lights_collection)
scene.collection.children.link(objects_collection)


# Default Collection
collection = bpy.data.collections.get("Collection")
default_objects = ["Camera", "Cube", "Light"]
for default_obj in default_objects:
    obj = bpy.data.objects.get(default_obj)
    collection.objects.unlink(obj)


# Base Collection
collection = bpy.data.collections.get("Base")
# Base 1
base_1 = bpy.data.objects.get("Cube")
base_1.name = "base_1"
base_1.scale = (3.0, 3.0, 0.5)
# Base 2
base_2 = bpy.data.objects["base_1"].copy()
base_2.name     = "base_2"
base_2.location = (0,   0,   0.9)
base_2.scale    = (3.4, 3.4, 0.4)
# Adding Objects
collection.objects.link(base_1)
collection.objects.link(base_2)
collection.objects.link(bpy.data.objects.get("Camera"))
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')


# Light Collection
collection = bpy.data.collections.get("Lights")
# Sun Light
light = bpy.data.objects.get("Light")
light.data.type = "SUN"
light.location  = (3, 6, 6)
light.rotation_mode  = 'XYZ'
light.rotation_euler = (math.radians(49), math.radians(30.5), math.radians(134))
# Adding Objects
collection.objects.link(light)


# Camera
camera = bpy.data.objects.get("Camera")
camera.location       = (43.7, -41.2, 30.45)
camera.rotation_euler = (math.radians(63.6), 0, math.radians(46.7))
camera.data.lens      = 200.0


# Render Options
bpy.context.scene.render.engine = 'BLENDER_EEVEE'
bpy.context.scene.eevee.taa_render_samples = 2048
bpy.context.scene.render.film_transparent  = True

collection = bpy.data.collections.get("Collection")
bpy.data.collections.remove(collection)
