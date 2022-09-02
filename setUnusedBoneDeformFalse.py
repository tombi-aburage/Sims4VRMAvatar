import bpy

def setUnusedBoneDeformFalse_init(in_armature):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[in_armature]
    bpy.ops.object.mode_set(mode='EDIT')
    
def female(in_vrm):

    VRoidModel = bpy.data.armatures[in_vrm]

    VRoidModel.edit_bones['J_Sec_R_SkirtFront_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_SkirtFront_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_SkirtFront_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_SkirtFront_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_SkirtSide_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_SkirtSide_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_SkirtSide_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_SkirtSide_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_SkirtBack_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_SkirtBack_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_SkirtBack_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_SkirtBack_end_01'].use_deform =False
    
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtFront_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtFront_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtFront_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtFront_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtSide1_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtSide2_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtSide2_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtSide1_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtSide2_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtSide2_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtBack_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtBack_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtBack_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtBack_end_01'].use_deform =False

    VRoidModel.edit_bones['J_Sec_Hair1_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_03'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_03'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_03'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_02'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_02'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_02'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_05'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_05'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_05'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair4_05'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair5_05'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair6_05'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_06'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_06'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_06'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair4_06'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_04'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_04'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_04'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair4_04'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_08'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_08'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_08'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_07'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_07'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_07'].use_deform =False

def male(in_vrm):

    VRoidModel = bpy.data.armatures[in_vrm]

    VRoidModel.edit_bones['J_Sec_R_TopsUpperLegFront_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_TopsUpperLegFront_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_TopsUpperLegFront_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_TopsUpperLegFront_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_TopsUpperLegSide_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_TopsUpperLegSide_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_TopsUpperLegSide_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_TopsUpperLegSide_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_TopsUpperLegBack_01'].use_deform =False
# this bone name... maybe bug
    VRoidModel.edit_bones['J_Sec_R_TopsUpperLegBack_end 1_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_TopsUpperLegBack_01'].use_deform =False
# this bone name...  maybe bug
    VRoidModel.edit_bones['J_Sec_R_TopsUpperLegBack_end_01'].use_deform =False
#    VRoidModel.edit_bones['J_Sec_L_TopsUpperLegBack_end_01'].use_deform =False

    VRoidModel.edit_bones['J_Sec_R_CoatSkirtFront_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtFront_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtFront_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtFront_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtSide1_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtSide2_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtSide2_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtSide1_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtSide2_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtSide2_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtBack_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_CoatSkirtBack_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtBack_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_CoatSkirtBack_end_01'].use_deform =False

    VRoidModel.edit_bones['J_Sec_R_TopsUpperArmOutside_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_TopsUpperArmOutside_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_TopsUpperArmInside_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_R_TopsUpperArmInside_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_TopsUpperArmOutside_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_TopsUpperArmOutside_end_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_TopsUpperArmInside_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_L_TopsUpperArmInside_end_01'].use_deform =False
    
#https://tombi-aburage.hatenablog.jp/entry/2022/08/18/064853
    VRoidModel.edit_bones['J_Sec_Hair1_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_01'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_02'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_02'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_02'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_07'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_07'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_07'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_03'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_03'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_03'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_05'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_05'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_05'].use_deform =False
#    VRoidModel.edit_bones['J_Sec_Hair4_05'].use_deform =False
#    VRoidModel.edit_bones['J_Sec_Hair5_05'].use_deform =False
#    VRoidModel.edit_bones['J_Sec_Hair6_05'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_06'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_06'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_06'].use_deform =False
#    VRoidModel.edit_bones['J_Sec_Hair4_06'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair1_04'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair2_04'].use_deform =False
    VRoidModel.edit_bones['J_Sec_Hair3_04'].use_deform =False
#    VRoidModel.edit_bones['J_Sec_Hair4_04'].use_deform =False
#    VRoidModel.edit_bones['J_Sec_Hair1_08'].use_deform =False
#    VRoidModel.edit_bones['J_Sec_Hair2_08'].use_deform =False
#    VRoidModel.edit_bones['J_Sec_Hair3_08'].use_deform =False

setUnusedBoneDeformFalse_init('Armature')
#female('Armature')
male('Armature')
