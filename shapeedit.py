import bpy
import math

def shapeedit_init(in_shapkey, in_mesh, in_armature):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[in_mesh]
    bpy.context.active_object.modifiers.new(name = in_shapkey, type='ARMATURE')
    bpy.context.active_object.modifiers[in_shapkey].object = bpy.data.objects[in_armature]
    bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[in_armature]
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.pose.transforms_clear()
    
def shapeedit_posing(in_shapkey, in_armature):
    B = bpy.data.objects[in_armature].pose.bones
    match in_shapkey:
        case "Fcl_EYE_Close_L":
            B['b__L_UpLid__'].rotation_mode='XYZ'
            B['b__L_UpLid__'].rotation_euler.rotate_axis('Z',math.radians(25))
        case "Fcl_EYE_Close_R":
            B['b__R_UpLid__'].rotation_mode='XYZ'
            B['b__R_UpLid__'].rotation_euler.rotate_axis('Z',math.radians(25))
        case "Fcl_EYE_Close":
            B['b__L_UpLid__'].rotation_mode='XYZ'
            B['b__L_UpLid__'].rotation_euler.rotate_axis('Z',math.radians(25))
            B['b__R_UpLid__'].rotation_mode='XYZ'
            B['b__R_UpLid__'].rotation_euler.rotate_axis('Z',math.radians(25))
        case "Fcl_ALL_Angry":
            B['b__L_InBrow__'].location.x -= 0.009
            B['b__R_InBrow__'].location.x -= 0.009
            B['b__L_UpLip__'].location.x += 0.005
            B['b__R_UpLip__'].location.x += 0.005
            B['b__UpLip__'].location.x += 0.005
            B['b__LoLip__'].location.x += 0.002
            B['b__L_LoLip__'].location.x += 0.003
            B['b__R_LoLip__'].location.x += 0.003
        case "Fcl_ALL_Fun":
            B['b__L_Mouth__'].location.x += 0.005
            B['b__R_Mouth__'].location.x += 0.005
        case "Fcl_ALL_Joy":
            B['b__Jaw__'].rotation_mode='XYZ'
            B['b__Jaw__'].rotation_euler.rotate_axis('Z',math.radians(-5))
            B['b__L_Mouth__'].location.x += 0.005
            B['b__R_Mouth__'].location.x += 0.005
            B['b__L_LoLid__'].rotation_mode='XYZ'
            B['b__L_LoLid__'].rotation_euler.rotate_axis('Z',math.radians(-10))
            B['b__R_LoLid__'].rotation_mode='XYZ'
            B['b__R_LoLid__'].rotation_euler.rotate_axis('Z',math.radians(-10))
        case "Fcl_ALL_Sorrow":
            B['b__L_InBrow__'].location.x += 0.01
            B['b__R_InBrow__'].location.x += 0.01
            B['b__L_MidBrow__'].location.x -= 0.01
            B['b__R_MidBrow__'].location.x -= 0.01
            B['b__L_OutBrow__'].location.x -= 0.01
            B['b__R_OutBrow__'].location.x -= 0.01
            B['b__Jaw__'].rotation_mode='XYZ'
            B['b__Jaw__'].rotation_euler.rotate_axis('Z',math.radians(-5))
            B['b__L_Mouth__'].location.x -= 0.005
            B['b__R_Mouth__'].location.x -= 0.005
        case "Fcl_MTH_I":
            B['b__L_UpLip__'].location.x += 0.002
            B['b__R_UpLip__'].location.x += 0.002
            B['b__UpLip__'].location.x += 0.002
            B['b__LoLip__'].location.x -= 0.002
            B['b__L_LoLip__'].location.x -= 0.002
            B['b__R_LoLip__'].location.x -= 0.002
        case "Fcl_MTH_A":
            B['b__Jaw__'].rotation_mode='XYZ'
            B['b__Jaw__'].rotation_euler.rotate_axis('Z',math.radians(-5))
        case "Fcl_MTH_E":
            B['b__Jaw__'].rotation_mode='XYZ'
            B['b__Jaw__'].rotation_euler.rotate_axis('Z',math.radians(-5))
        case "Fcl_MTH_O":
            B['b__Jaw__'].rotation_mode='XYZ'
            B['b__Jaw__'].rotation_euler.rotate_axis('Z',math.radians(-10))
            B['b__LoLip__'].location.x += 0.005
            B['b__L_LoLip__'].location.x += 0.005
            B['b__R_LoLip__'].location.x += 0.005
        case "Fcl_MTH_U":
            B['b__Jaw__'].rotation_mode='XYZ'
            B['b__Jaw__'].rotation_euler.rotate_axis('Z',math.radians(-5))
            B['b__LoLip__'].location.x += 0.005
            B['b__L_LoLip__'].location.x += 0.005
            B['b__R_LoLip__'].location.x += 0.005
            B['b__L_Mouth__'].location.z -= 0.002
            B['b__R_Mouth__'].location.z += 0.002
        case "Fcl_ALL_Neutral":
            pass

def shapeedit_finish(in_shapkey, in_mesh):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[in_mesh]
    bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=False,modifier=in_shapkey)

def shapeedit_for_(in_shapkey, in_mesh, in_armature):
    shapeedit_init(in_shapkey,in_mesh,in_armature)
    shapeedit_posing(in_shapkey,in_armature)
    shapeedit_finish(in_shapkey,in_mesh)

shapeedit_for_('Fcl_EYE_Close_L', 'JeanCrawford','rig')
shapeedit_for_('Fcl_EYE_Close_R', 'JeanCrawford','rig')
shapeedit_for_('Fcl_EYE_Close', 'JeanCrawford','rig')
shapeedit_for_('Fcl_ALL_Angry', 'JeanCrawford','rig')
shapeedit_for_('Fcl_ALL_Fun', 'JeanCrawford','rig')
shapeedit_for_('Fcl_ALL_Joy', 'JeanCrawford','rig')
shapeedit_for_('Fcl_ALL_Sorrow', 'JeanCrawford','rig')
shapeedit_for_('Fcl_MTH_I', 'JeanCrawford','rig')
shapeedit_for_('Fcl_MTH_A', 'JeanCrawford','rig')
shapeedit_for_('Fcl_MTH_E', 'JeanCrawford','rig')
shapeedit_for_('Fcl_MTH_O', 'JeanCrawford','rig')
shapeedit_for_('Fcl_MTH_U', 'JeanCrawford','rig')
shapeedit_for_('Fcl_ALL_Neutral', 'JeanCrawford','rig')
