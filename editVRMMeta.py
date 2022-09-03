import bpy

def editVRMMeta(in_armature, in_mesh):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[in_armature]   
    VRoidModel = bpy.data.armatures[in_armature]    
    for i in VRoidModel.vrm_addon_extension.vrm0.blend_shape_master.blend_shape_groups :
        i.binds[0].mesh.value = in_mesh
 
editVRMMeta('Armature', 'LionelStrickland')
