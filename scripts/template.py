import bpy
import math

COLLECTIONS     = ["Base", "Lights", "Objects"]
DEFAULT_OBJECTS = ["Cube", "Light",  "Camera"]


def init_collections():
    # Unlinking default objects from default collection
    default_collection = bpy.data.collections.get("Collection")
    for default_object in DEFAULT_OBJECTS:
        obj = bpy.data.objects.get(default_object)
        default_collection.objects.unlink(obj)

    # Creating template collections
    for collection in COLLECTIONS:
        coll_object = bpy.data.collections.new(collection)
        scene = bpy.context.scene
        scene.collection.children.link(coll_object)

    # Deleting default collection
    collection = bpy.data.collections.get("Collection")
    bpy.data.collections.remove(collection)


def init_base_collection():
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


def init_light_collection():
    collection = bpy.data.collections.get("Lights")
    # Sun Light
    light = bpy.data.objects.get("Light")
    light.data.type = "SUN"
    light.location  = (3, 6, 6)
    light.rotation_mode  = 'XYZ'
    light.rotation_euler = (math.radians(49), math.radians(30.5), math.radians(134))
    # Adding Objects
    collection.objects.link(light)


def init_camera():
    camera = bpy.data.objects.get("Camera")
    camera.location       = (43.7, -41.2, 30.45)
    camera.rotation_euler = (math.radians(63.6), 0, math.radians(46.7))
    camera.data.lens      = 200.0


def set_render_options():
    bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    bpy.context.scene.eevee.taa_render_samples = 2048
    bpy.context.scene.render.film_transparent  = True


if __name__ == "__main__":
    init_collections()
    init_base_collection()
    init_light_collection()
    init_camera()
    set_render_options()
