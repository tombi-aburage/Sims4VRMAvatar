import bpy
import math

def changeAPoseToTPose_init(in_armature):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[in_armature]
    bpy.ops.object.mode_set(mode='POSE')

def changeAPoseToTPose():
    B = bpy.context.active_object.pose.bones
    B['b__R_UpperArm__'].rotation_mode='XYZ'
    B['b__R_UpperArm__'].rotation_euler.rotate_axis('Y',math.radians(-45))
    B['b__L_UpperArm__'].rotation_mode='XYZ'
    B['b__L_UpperArm__'].rotation_euler.rotate_axis('Y',math.radians(45))
    
def changeAPoseToTPose_finish(in_armature,in_mesh ):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[in_mesh]
    bpy.ops.object.modifier_apply(modifier='アーマチュア')
    bpy.ops.object.modifier_apply(modifier='Armature')
    bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[in_armature]
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.armature_apply(selected=False) 

changeAPoseToTPose_init('rig')
changeAPoseToTPose()
changeAPoseToTPose_finish('rig','LionelStrickland')
