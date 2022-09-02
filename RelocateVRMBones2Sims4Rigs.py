import bpy

def relocate_init(in_armature):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[in_armature]
    bpy.ops.object.mode_set(mode='EDIT')

def female_hair(in_vrm, in_sims4):
    VRoidModel = bpy.data.armatures[in_vrm]
    Sims4Model = bpy.data.armatures[in_sims4].edit_bones.data
    
    VRoidModel.edit_bones['J_Sec_R_SkirtFront_01'].head.x = Sims4Model.bones['b__R_Thigh__'].head_local.x
    VRoidModel.edit_bones['J_Sec_R_SkirtFront_01'].head.y = Sims4Model.bones['b__R_Thigh__'].head_local.z * -1 - 0.10
    VRoidModel.edit_bones['J_Sec_R_SkirtFront_01'].head.z = Sims4Model.bones['b__R_Thigh__'].head_local.y - 0.10
    VRoidModel.edit_bones['J_Sec_R_SkirtFront_01'].length = 0.1
    VRoidModel.edit_bones['J_Sec_R_SkirtFront_end_01'].length = 0.1

    VRoidModel.edit_bones['J_Sec_R_SkirtSide_01'].head.x = Sims4Model.bones['b__R_Thigh__'].head_local.x - 0.10
    VRoidModel.edit_bones['J_Sec_R_SkirtSide_01'].head.y = Sims4Model.bones['b__R_Thigh__'].head_local.z * -1
    VRoidModel.edit_bones['J_Sec_R_SkirtSide_01'].head.z = Sims4Model.bones['b__R_Thigh__'].head_local.y - 0.08
    VRoidModel.edit_bones['J_Sec_R_SkirtSide_01'].length = 0.1
    VRoidModel.edit_bones['J_Sec_R_SkirtSide_end_01'].length = 0.1

    VRoidModel.edit_bones['J_Sec_R_SkirtBack_01'].head.x = Sims4Model.bones['b__R_Thigh__'].head_local.x
    VRoidModel.edit_bones['J_Sec_R_SkirtBack_01'].head.y = Sims4Model.bones['b__R_Thigh__'].head_local.z * -1 + 0.10
    VRoidModel.edit_bones['J_Sec_R_SkirtBack_01'].head.z = Sims4Model.bones['b__R_Thigh__'].head_local.y - 0.10
    VRoidModel.edit_bones['J_Sec_R_SkirtBack_01'].length = 0.1
    VRoidModel.edit_bones['J_Sec_R_SkirtBack_end_01'].length = 0.1

    VRoidModel.edit_bones['J_Sec_L_SkirtFront_01'].head.x = Sims4Model.bones['b__L_Thigh__'].head_local.x
    VRoidModel.edit_bones['J_Sec_L_SkirtFront_01'].head.y = Sims4Model.bones['b__L_Thigh__'].head_local.z * -1 - 0.10
    VRoidModel.edit_bones['J_Sec_L_SkirtFront_01'].head.z = Sims4Model.bones['b__L_Thigh__'].head_local.y - 0.10
    VRoidModel.edit_bones['J_Sec_L_SkirtFront_01'].length = 0.1
    VRoidModel.edit_bones['J_Sec_L_SkirtFront_end_01'].length = 0.1

    VRoidModel.edit_bones['J_Sec_L_SkirtSide_01'].head.x = Sims4Model.bones['b__L_Thigh__'].head_local.x + 0.10
    VRoidModel.edit_bones['J_Sec_L_SkirtSide_01'].head.y = Sims4Model.bones['b__L_Thigh__'].head_local.z * -1
    VRoidModel.edit_bones['J_Sec_L_SkirtSide_01'].head.z = Sims4Model.bones['b__L_Thigh__'].head_local.y - 0.08
    VRoidModel.edit_bones['J_Sec_L_SkirtSide_01'].length = 0.1
    VRoidModel.edit_bones['J_Sec_L_SkirtSide_end_01'].length = 0.1

    VRoidModel.edit_bones['J_Sec_L_SkirtBack_01'].head.x = Sims4Model.bones['b__L_Thigh__'].head_local.x
    VRoidModel.edit_bones['J_Sec_L_SkirtBack_01'].head.y = Sims4Model.bones['b__L_Thigh__'].head_local.z * -1 + 0.10
    VRoidModel.edit_bones['J_Sec_L_SkirtBack_01'].head.z = Sims4Model.bones['b__L_Thigh__'].head_local.y - 0.10
    VRoidModel.edit_bones['J_Sec_L_SkirtBack_01'].length = 0.1
    VRoidModel.edit_bones['J_Sec_L_SkirtBack_end_01'].length = 0.1

    VRoidModel.edit_bones['J_Sec_Hair1_03'].head.x = Sims4Model.bones['b__R_UpperArm__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_03'].head.y = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.z * -1
    VRoidModel.edit_bones['J_Sec_Hair1_03'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y +0.08
    VRoidModel.edit_bones['J_Sec_Hair1_03'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair2_03'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair3_03'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair1_02'].head.x = Sims4Model.bones['b__L_UpperArm__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_02'].head.y = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.z * -1
    VRoidModel.edit_bones['J_Sec_Hair1_02'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y +0.08
    VRoidModel.edit_bones['J_Sec_Hair1_02'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair2_02'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair3_02'].length = 0.05

    VRoidModel.edit_bones['J_Sec_Hair1_04'].head.x = Sims4Model.bones['b__L_UpperArm__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_04'].head.y = Sims4Model.bones['b__Head__'].head_local.z * -1 + 0.15
    VRoidModel.edit_bones['J_Sec_Hair1_04'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y
    VRoidModel.edit_bones['J_Sec_Hair1_04'].length = 0.10
    VRoidModel.edit_bones['J_Sec_Hair2_04'].length = 0.10
    VRoidModel.edit_bones['J_Sec_Hair3_04'].length = 0.10

    VRoidModel.edit_bones['J_Sec_Hair4_04'].length = 0.10

    VRoidModel.edit_bones['J_Sec_Hair1_05'].head.x = Sims4Model.bones['b__Head__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_05'].head.y = Sims4Model.bones['b__Head__'].head_local.z * -1 + 0.15
    VRoidModel.edit_bones['J_Sec_Hair1_05'].head.z = Sims4Model.bones['b__Head__'].head_local.y
    VRoidModel.edit_bones['J_Sec_Hair1_05'].length = 0.2
    VRoidModel.edit_bones['J_Sec_Hair2_05'].length = 0.2
    VRoidModel.edit_bones['J_Sec_Hair3_05'].length = 0.2
    
    VRoidModel.edit_bones['J_Sec_Hair4_05'].length = 0.2
    VRoidModel.edit_bones['J_Sec_Hair5_05'].length = 0.2
    VRoidModel.edit_bones['J_Sec_Hair6_05'].length = 0.2

    VRoidModel.edit_bones['J_Sec_Hair1_06'].head.x = Sims4Model.bones['b__R_UpperArm__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_06'].head.y = Sims4Model.bones['b__Head__'].head_local.z * -1 + 0.15
    VRoidModel.edit_bones['J_Sec_Hair1_06'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y
    VRoidModel.edit_bones['J_Sec_Hair1_06'].length = 0.10
    VRoidModel.edit_bones['J_Sec_Hair2_06'].length = 0.10
    VRoidModel.edit_bones['J_Sec_Hair3_06'].length = 0.10
    
    VRoidModel.edit_bones['J_Sec_Hair4_06'].length = 0.10
    
    VRoidModel.edit_bones['J_Sec_Hair1_07'].head.x = Sims4Model.bones['b__L_UpperArm__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_07'].head.y = Sims4Model.bones['b__Head__'].head_local.z * -1 + 0.15
    VRoidModel.edit_bones['J_Sec_Hair1_07'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y + 0.15
    VRoidModel.edit_bones['J_Sec_Hair1_07'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair2_07'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair3_07'].length = 0.05
    
    VRoidModel.edit_bones['J_Sec_Hair1_08'].head.x = Sims4Model.bones['b__R_UpperArm__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_08'].head.y = Sims4Model.bones['b__Head__'].head_local.z * -1 + 0.15
    VRoidModel.edit_bones['J_Sec_Hair1_08'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y + 0.15
    VRoidModel.edit_bones['J_Sec_Hair1_08'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair2_08'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair3_08'].length = 0.05

def male_hair(in_vrm, in_sims4):
    VRoidModel = bpy.data.armatures[in_vrm]
    Sims4Model = bpy.data.armatures[in_sims4].edit_bones.data

    VRoidModel.edit_bones['J_Sec_Hair1_03'].head.x = Sims4Model.bones['b__L_UpperArm__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_03'].head.y = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.z * -1
    VRoidModel.edit_bones['J_Sec_Hair1_03'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y +0.08
    VRoidModel.edit_bones['J_Sec_Hair1_03'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair2_03'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair3_03'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair1_07'].head.x = Sims4Model.bones['b__R_UpperArm__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_07'].head.y = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.z * -1
    VRoidModel.edit_bones['J_Sec_Hair1_07'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y +0.08
    VRoidModel.edit_bones['J_Sec_Hair1_07'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair2_07'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair3_07'].length = 0.05

    VRoidModel.edit_bones['J_Sec_Hair1_04'].head.x = Sims4Model.bones['b__L_UpperArm__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_04'].head.y = Sims4Model.bones['b__Head__'].head_local.z * -1 + 0.15
    VRoidModel.edit_bones['J_Sec_Hair1_04'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y
    VRoidModel.edit_bones['J_Sec_Hair1_04'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair2_04'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair3_04'].length = 0.05

#    VRoidModel.edit_bones['J_Sec_Hair4_04'].length = 0.10

    VRoidModel.edit_bones['J_Sec_Hair1_05'].head.x = Sims4Model.bones['b__Head__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_05'].head.y = Sims4Model.bones['b__Head__'].head_local.z * -1 + 0.15
    VRoidModel.edit_bones['J_Sec_Hair1_05'].head.z = Sims4Model.bones['b__Head__'].head_local.y + 0.10
    VRoidModel.edit_bones['J_Sec_Hair1_05'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair2_05'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair3_05'].length = 0.05
    
#    VRoidModel.edit_bones['J_Sec_Hair4_05'].length = 0.2
#    VRoidModel.edit_bones['J_Sec_Hair5_05'].length = 0.2
#    VRoidModel.edit_bones['J_Sec_Hair6_05'].length = 0.2

    VRoidModel.edit_bones['J_Sec_Hair1_06'].head.x = Sims4Model.bones['b__R_UpperArm__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_06'].head.y = Sims4Model.bones['b__Head__'].head_local.z * -1 + 0.15
    VRoidModel.edit_bones['J_Sec_Hair1_06'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y
    VRoidModel.edit_bones['J_Sec_Hair1_06'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair2_06'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair3_06'].length = 0.05
    
#    VRoidModel.edit_bones['J_Sec_Hair4_06'].length = 0.10

    VRoidModel.edit_bones['J_Sec_Hair1_02'].head.x = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair1_02'].head.y = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.z * -1
    VRoidModel.edit_bones['J_Sec_Hair1_02'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y +0.25
    VRoidModel.edit_bones['J_Sec_Hair2_02'].head.x = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.x
    VRoidModel.edit_bones['J_Sec_Hair2_02'].head.y = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.z * -1
    VRoidModel.edit_bones['J_Sec_Hair2_02'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y +0.25 -0.05
    VRoidModel.edit_bones['J_Sec_Hair2_02'].length = 0.05
    VRoidModel.edit_bones['J_Sec_Hair3_02'].length = 0.05

relocate_init('Armature')
#female_hair('Armature','rig')
male_hair('Armature','rig')

VRoidModel = bpy.data.armatures['Armature']
Sims4Model = bpy.data.armatures['rig'].edit_bones.data

VRoidModel.edit_bones['J_Bip_C_Hips'].head.xzy = Sims4Model.bones['b__ROOT_bind__'].head_local
VRoidModel.edit_bones['J_Bip_C_Hips'].head.y = Sims4Model.bones['b__ROOT_bind__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_C_Spine'].head.xzy = Sims4Model.bones['b__Spine0__'].head_local
VRoidModel.edit_bones['J_Bip_C_Spine'].head.y = Sims4Model.bones['b__Spine0__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_C_Chest'].head.xzy = Sims4Model.bones['b__Spine1__'].head_local
VRoidModel.edit_bones['J_Bip_C_Chest'].head.y = Sims4Model.bones['b__Spine1__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_C_UpperChest'].head.xzy = Sims4Model.bones['b__Spine2__'].head_local
VRoidModel.edit_bones['J_Bip_C_UpperChest'].head.y = Sims4Model.bones['b__Spine2__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_C_Neck'].head.xzy = Sims4Model.bones['b__Neck__'].head_local
VRoidModel.edit_bones['J_Bip_C_Neck'].head.y = Sims4Model.bones['b__Neck__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_C_Head'].head.xzy = Sims4Model.bones['b__Head__'].head_local
VRoidModel.edit_bones['J_Bip_C_Head'].head.y = Sims4Model.bones['b__Head__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_C_Head'].tail.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y
VRoidModel.edit_bones['J_Bip_C_Head'].tail.y = Sims4Model.bones['b__ROOT_bind__'].head_local.z

VRoidModel.edit_bones['J_Adj_R_FaceEye'].head.xzy = Sims4Model.bones['b__R_Eye__'].head_local
VRoidModel.edit_bones['J_Adj_R_FaceEye'].head.y = Sims4Model.bones['b__R_Eye__'].head_local.z * -1
VRoidModel.edit_bones['J_Adj_R_FaceEye'].tail.z = Sims4Model.bones['b__R_Eye__'].head_local.y
VRoidModel.edit_bones['J_Adj_R_FaceEye'].head.y = Sims4Model.bones['b__ROOT_bind__'].head_local.z
VRoidModel.edit_bones['J_Adj_R_FaceEye'].tail.y = Sims4Model.bones['b__R_Eye__'].head_local.z -1
VRoidModel.edit_bones['J_Adj_R_FaceEye'].length = 0.01

VRoidModel.edit_bones['J_Bip_R_Shoulder'].head.xzy = Sims4Model.bones['b__R_Clavicle__'].head_local
VRoidModel.edit_bones['J_Bip_R_Shoulder'].head.y = Sims4Model.bones['b__R_Clavicle__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_R_UpperArm'].head.xzy = Sims4Model.bones['b__R_UpperArm__'].head_local
VRoidModel.edit_bones['J_Bip_R_UpperArm'].head.y = Sims4Model.bones['b__R_UpperArm__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_R_LowerArm'].head.xzy = Sims4Model.bones['b__R_Forearm__'].head_local
VRoidModel.edit_bones['J_Bip_R_LowerArm'].head.y = Sims4Model.bones['b__R_Forearm__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_R_Hand'].head.xzy = Sims4Model.bones['b__R_Hand__'].head_local
VRoidModel.edit_bones['J_Bip_R_Hand'].head.y = Sims4Model.bones['b__R_Hand__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Hand'].tail.xzy = Sims4Model.bones['b__R_Stigmata'].head_local
VRoidModel.edit_bones['J_Bip_R_Hand'].tail.y = Sims4Model.bones['b__R_Stigmata'].head_local.z * -1

VRoidModel.edit_bones['J_Sec_R_Bust1'].head.xzy = Sims4Model.bones['b__CAS_R_Breast__'].head_local
VRoidModel.edit_bones['J_Sec_R_Bust1'].head.y = Sims4Model.bones['b__CAS_R_Breast__'].head_local.z * -1
VRoidModel.edit_bones['J_Sec_R_Bust1'].tail.z = Sims4Model.bones['b__CAS_R_Breast__'].head_local.y
VRoidModel.edit_bones['J_Sec_R_Bust1'].tail.y = Sims4Model.bones['b__CAS_R_Breast__'].head_local.z * -1 - 0.002
VRoidModel.edit_bones['J_Sec_R_Bust1'].tail.x = Sims4Model.bones['b__CAS_R_Breast__'].head_local.x
VRoidModel.edit_bones['J_Sec_R_Bust2'].tail.z = Sims4Model.bones['b__CAS_R_Breast__'].head_local.y
VRoidModel.edit_bones['J_Sec_R_Bust2'].tail.y = Sims4Model.bones['b__CAS_R_Breast__'].head_local.z * -1 - 0.002 - 0.01
VRoidModel.edit_bones['J_Sec_R_Bust2'].tail.x = Sims4Model.bones['b__CAS_R_Breast__'].head_local.x

VRoidModel.edit_bones['J_Bip_R_UpperLeg'].head.xzy = Sims4Model.bones['b__R_Thigh__'].head_local
VRoidModel.edit_bones['J_Bip_R_UpperLeg'].head.y = Sims4Model.bones['b__R_Thigh__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_LowerLeg'].head.xzy = Sims4Model.bones['b__R_Calf__'].head_local
VRoidModel.edit_bones['J_Bip_R_LowerLeg'].head.y = Sims4Model.bones['b__R_Calf__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_R_Foot'].head.xzy = Sims4Model.bones['b__R_Foot__'].head_local
VRoidModel.edit_bones['J_Bip_R_Foot'].head.y = Sims4Model.bones['b__R_Foot__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_R_ToeBase'].head.xzy = Sims4Model.bones['b__R_Toe__'].head_local
VRoidModel.edit_bones['J_Bip_R_ToeBase'].head.y = Sims4Model.bones['b__R_Toe__'].head_local.z * -1

VRoidModel.edit_bones['J_Adj_L_FaceEye'].head.xzy = Sims4Model.bones['b__L_Eye__'].head_local
VRoidModel.edit_bones['J_Adj_L_FaceEye'].head.y = Sims4Model.bones['b__L_Eye__'].head_local.z * -1
VRoidModel.edit_bones['J_Adj_L_FaceEye'].tail.z = Sims4Model.bones['b__L_Eye__'].head_local.y
VRoidModel.edit_bones['J_Adj_L_FaceEye'].head.y = Sims4Model.bones['b__ROOT_bind__'].head_local.z
VRoidModel.edit_bones['J_Adj_L_FaceEye'].tail.y = Sims4Model.bones['b__L_Eye__'].head_local.z -1
VRoidModel.edit_bones['J_Adj_L_FaceEye'].length = 0.01

VRoidModel.edit_bones['J_Bip_L_Shoulder'].head.xzy = Sims4Model.bones['b__L_Clavicle__'].head_local
VRoidModel.edit_bones['J_Bip_L_Shoulder'].head.y = Sims4Model.bones['b__L_Clavicle__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_UpperArm'].head.xzy = Sims4Model.bones['b__L_UpperArm__'].head_local
VRoidModel.edit_bones['J_Bip_L_UpperArm'].head.y = Sims4Model.bones['b__L_UpperArm__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_LowerArm'].head.xzy = Sims4Model.bones['b__L_Forearm__'].head_local
VRoidModel.edit_bones['J_Bip_L_LowerArm'].head.y = Sims4Model.bones['b__L_Forearm__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_L_Hand'].head.xzy = Sims4Model.bones['b__L_Hand__'].head_local
VRoidModel.edit_bones['J_Bip_L_Hand'].head.y = Sims4Model.bones['b__L_Hand__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Hand'].tail.xzy = Sims4Model.bones['b__L_Stigmata'].head_local
VRoidModel.edit_bones['J_Bip_L_Hand'].tail.y = Sims4Model.bones['b__L_Stigmata'].head_local.z * -1

VRoidModel.edit_bones['J_Sec_L_Bust1'].head.xzy = Sims4Model.bones['b__CAS_L_Breast__'].head_local
VRoidModel.edit_bones['J_Sec_L_Bust1'].head.y = Sims4Model.bones['b__CAS_L_Breast__'].head_local.z * -1
VRoidModel.edit_bones['J_Sec_L_Bust1'].tail.z = Sims4Model.bones['b__CAS_L_Breast__'].head_local.y
VRoidModel.edit_bones['J_Sec_L_Bust1'].tail.y = Sims4Model.bones['b__CAS_L_Breast__'].head_local.z * -1 - 0.002
VRoidModel.edit_bones['J_Sec_L_Bust1'].tail.x = Sims4Model.bones['b__CAS_L_Breast__'].head_local.x
VRoidModel.edit_bones['J_Sec_L_Bust2'].tail.z = Sims4Model.bones['b__CAS_L_Breast__'].head_local.y
VRoidModel.edit_bones['J_Sec_L_Bust2'].tail.y = Sims4Model.bones['b__CAS_L_Breast__'].head_local.z * -1 - 0.002 - 0.01
VRoidModel.edit_bones['J_Sec_L_Bust2'].tail.x = Sims4Model.bones['b__CAS_L_Breast__'].head_local.x

VRoidModel.edit_bones['J_Bip_L_UpperLeg'].head.xzy = Sims4Model.bones['b__L_Thigh__'].head_local
VRoidModel.edit_bones['J_Bip_L_UpperLeg'].head.y = Sims4Model.bones['b__L_Thigh__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_LowerLeg'].head.xzy = Sims4Model.bones['b__L_Calf__'].head_local
VRoidModel.edit_bones['J_Bip_L_LowerLeg'].head.y = Sims4Model.bones['b__L_Calf__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Foot'].head.xzy = Sims4Model.bones['b__L_Foot__'].head_local
VRoidModel.edit_bones['J_Bip_L_Foot'].head.y = Sims4Model.bones['b__L_Foot__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_ToeBase'].head.xzy = Sims4Model.bones['b__L_Toe__'].head_local
VRoidModel.edit_bones['J_Bip_L_ToeBase'].head.y = Sims4Model.bones['b__L_Toe__'].head_local.z * -1

VRoidModel.edit_bones['J_Bip_R_Thumb1'].head.xzy = Sims4Model.bones['b__R_Thumb0__'].head_local
VRoidModel.edit_bones['J_Bip_R_Thumb1'].head.y = Sims4Model.bones['b__R_Thumb0__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Thumb2'].head.xzy = Sims4Model.bones['b__R_Thumb1__'].head_local
VRoidModel.edit_bones['J_Bip_R_Thumb2'].head.y = Sims4Model.bones['b__R_Thumb1__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Thumb3'].head.xzy = Sims4Model.bones['b__R_Thumb2__'].head_local
VRoidModel.edit_bones['J_Bip_R_Thumb3'].head.y = Sims4Model.bones['b__R_Thumb2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Thumb3'].tail.z = Sims4Model.bones['b__R_Thumb2__'].head_local.y
VRoidModel.edit_bones['J_Bip_R_Thumb3'].tail.y = Sims4Model.bones['b__R_Thumb2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Thumb3'].tail.x = Sims4Model.bones['b__R_Thumb2__'].head_local.x - 0.02

VRoidModel.edit_bones['J_Bip_R_Index1'].head.xzy = Sims4Model.bones['b__R_Index0__'].head_local
VRoidModel.edit_bones['J_Bip_R_Index1'].head.y = Sims4Model.bones['b__R_Index0__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Index2'].head.xzy = Sims4Model.bones['b__R_Index1__'].head_local
VRoidModel.edit_bones['J_Bip_R_Index2'].head.y = Sims4Model.bones['b__R_Index1__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Index3'].head.xzy = Sims4Model.bones['b__R_Index2__'].head_local
VRoidModel.edit_bones['J_Bip_R_Index3'].head.y = Sims4Model.bones['b__R_Index2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Index3'].tail.z = Sims4Model.bones['b__R_Index2__'].head_local.y
VRoidModel.edit_bones['J_Bip_R_Index3'].tail.y = Sims4Model.bones['b__R_Index2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Index3'].tail.x = Sims4Model.bones['b__R_Index2__'].head_local.x - 0.02

VRoidModel.edit_bones['J_Bip_R_Middle1'].head.xzy = Sims4Model.bones['b__R_Mid0__'].head_local
VRoidModel.edit_bones['J_Bip_R_Middle1'].head.y = Sims4Model.bones['b__R_Mid0__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Middle2'].head.xzy = Sims4Model.bones['b__R_Mid1__'].head_local
VRoidModel.edit_bones['J_Bip_R_Middle2'].head.y = Sims4Model.bones['b__R_Mid1__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Middle3'].head.xzy = Sims4Model.bones['b__R_Mid2__'].head_local
VRoidModel.edit_bones['J_Bip_R_Middle3'].head.y = Sims4Model.bones['b__R_Mid2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Middle3'].tail.z = Sims4Model.bones['b__R_Mid2__'].head_local.y
VRoidModel.edit_bones['J_Bip_R_Middle3'].tail.y = Sims4Model.bones['b__R_Mid2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Middle3'].tail.x = Sims4Model.bones['b__R_Mid2__'].head_local.x - 0.02

VRoidModel.edit_bones['J_Bip_R_Ring1'].head.xzy = Sims4Model.bones['b__R_Ring0__'].head_local
VRoidModel.edit_bones['J_Bip_R_Ring1'].head.y = Sims4Model.bones['b__R_Ring0__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Ring2'].head.xzy = Sims4Model.bones['b__R_Ring1__'].head_local
VRoidModel.edit_bones['J_Bip_R_Ring2'].head.y = Sims4Model.bones['b__R_Ring1__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Ring3'].head.xzy = Sims4Model.bones['b__R_Ring2__'].head_local
VRoidModel.edit_bones['J_Bip_R_Ring3'].head.y = Sims4Model.bones['b__R_Ring2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Ring3'].tail.z = Sims4Model.bones['b__R_Ring2__'].head_local.y
VRoidModel.edit_bones['J_Bip_R_Ring3'].tail.y = Sims4Model.bones['b__R_Ring2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Ring3'].tail.x = Sims4Model.bones['b__R_Ring2__'].head_local.x - 0.02

VRoidModel.edit_bones['J_Bip_R_Little1'].head.xzy = Sims4Model.bones['b__R_Pinky0__'].head_local
VRoidModel.edit_bones['J_Bip_R_Little1'].head.y = Sims4Model.bones['b__R_Pinky0__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Little2'].head.xzy = Sims4Model.bones['b__R_Pinky1__'].head_local
VRoidModel.edit_bones['J_Bip_R_Little2'].head.y = Sims4Model.bones['b__R_Pinky1__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Little3'].head.xzy = Sims4Model.bones['b__R_Pinky2__'].head_local
VRoidModel.edit_bones['J_Bip_R_Little3'].head.y = Sims4Model.bones['b__R_Pinky2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Little3'].tail.z = Sims4Model.bones['b__R_Pinky2__'].head_local.y
VRoidModel.edit_bones['J_Bip_R_Little3'].tail.y = Sims4Model.bones['b__R_Pinky2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_R_Little3'].tail.x = Sims4Model.bones['b__R_Pinky2__'].head_local.x - 0.02

VRoidModel.edit_bones['J_Bip_L_Thumb1'].head.xzy = Sims4Model.bones['b__L_Thumb0__'].head_local
VRoidModel.edit_bones['J_Bip_L_Thumb1'].head.y = Sims4Model.bones['b__L_Thumb0__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Thumb2'].head.xzy = Sims4Model.bones['b__L_Thumb1__'].head_local
VRoidModel.edit_bones['J_Bip_L_Thumb2'].head.y = Sims4Model.bones['b__L_Thumb1__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Thumb3'].head.xzy = Sims4Model.bones['b__L_Thumb2__'].head_local
VRoidModel.edit_bones['J_Bip_L_Thumb3'].head.y = Sims4Model.bones['b__L_Thumb2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Thumb3'].tail.z = Sims4Model.bones['b__L_Thumb2__'].head_local.y
VRoidModel.edit_bones['J_Bip_L_Thumb3'].tail.y = Sims4Model.bones['b__L_Thumb2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Thumb3'].tail.x = Sims4Model.bones['b__L_Thumb2__'].head_local.x + 0.02

VRoidModel.edit_bones['J_Bip_L_Index1'].head.xzy = Sims4Model.bones['b__L_Index0__'].head_local
VRoidModel.edit_bones['J_Bip_L_Index1'].head.y = Sims4Model.bones['b__L_Index0__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Index2'].head.xzy = Sims4Model.bones['b__L_Index1__'].head_local
VRoidModel.edit_bones['J_Bip_L_Index2'].head.y = Sims4Model.bones['b__L_Index1__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Index3'].head.xzy = Sims4Model.bones['b__L_Index2__'].head_local
VRoidModel.edit_bones['J_Bip_L_Index3'].head.y = Sims4Model.bones['b__L_Index2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Index3'].tail.z = Sims4Model.bones['b__L_Index2__'].head_local.y
VRoidModel.edit_bones['J_Bip_L_Index3'].tail.y = Sims4Model.bones['b__L_Index2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Index3'].tail.x = Sims4Model.bones['b__L_Index2__'].head_local.x + 0.02

VRoidModel.edit_bones['J_Bip_L_Middle1'].head.xzy = Sims4Model.bones['b__L_Mid0__'].head_local
VRoidModel.edit_bones['J_Bip_L_Middle1'].head.y = Sims4Model.bones['b__L_Mid0__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Middle2'].head.xzy = Sims4Model.bones['b__L_Mid1__'].head_local
VRoidModel.edit_bones['J_Bip_L_Middle2'].head.y = Sims4Model.bones['b__L_Mid1__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Middle3'].head.xzy = Sims4Model.bones['b__L_Mid2__'].head_local
VRoidModel.edit_bones['J_Bip_L_Middle3'].head.y = Sims4Model.bones['b__L_Mid2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Middle3'].tail.z = Sims4Model.bones['b__L_Mid2__'].head_local.y
VRoidModel.edit_bones['J_Bip_L_Middle3'].tail.y = Sims4Model.bones['b__L_Mid2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Middle3'].tail.x = Sims4Model.bones['b__L_Mid2__'].head_local.x + 0.02

VRoidModel.edit_bones['J_Bip_L_Ring1'].head.xzy = Sims4Model.bones['b__L_Ring0__'].head_local
VRoidModel.edit_bones['J_Bip_L_Ring1'].head.y = Sims4Model.bones['b__L_Ring0__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Ring2'].head.xzy = Sims4Model.bones['b__L_Ring1__'].head_local

VRoidModel.edit_bones['J_Bip_L_Ring2'].head.y = Sims4Model.bones['b__L_Ring1__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Ring3'].head.xzy = Sims4Model.bones['b__L_Ring2__'].head_local
VRoidModel.edit_bones['J_Bip_L_Ring3'].head.y = Sims4Model.bones['b__L_Ring2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Ring3'].tail.z = Sims4Model.bones['b__L_Ring2__'].head_local.y
VRoidModel.edit_bones['J_Bip_L_Ring3'].tail.y = Sims4Model.bones['b__L_Ring2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Ring3'].tail.x = Sims4Model.bones['b__L_Ring2__'].head_local.x + 0.02

VRoidModel.edit_bones['J_Bip_L_Little1'].head.xzy = Sims4Model.bones['b__L_Pinky0__'].head_local
VRoidModel.edit_bones['J_Bip_L_Little1'].head.y = Sims4Model.bones['b__L_Pinky0__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Little2'].head.xzy = Sims4Model.bones['b__L_Pinky1__'].head_local
VRoidModel.edit_bones['J_Bip_L_Little2'].head.y = Sims4Model.bones['b__L_Pinky1__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Little3'].head.xzy = Sims4Model.bones['b__L_Pinky2__'].head_local
VRoidModel.edit_bones['J_Bip_L_Little3'].head.y = Sims4Model.bones['b__L_Pinky2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Little3'].tail.z = Sims4Model.bones['b__L_Pinky2__'].head_local.y
VRoidModel.edit_bones['J_Bip_L_Little3'].tail.y = Sims4Model.bones['b__L_Pinky2__'].head_local.z * -1
VRoidModel.edit_bones['J_Bip_L_Little3'].tail.x = Sims4Model.bones['b__L_Pinky2__'].head_local.x + 0.02

VRoidModel.edit_bones['J_Sec_Hair1_01'].head.x = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.x
VRoidModel.edit_bones['J_Sec_Hair1_01'].head.y = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.z * -1
VRoidModel.edit_bones['J_Sec_Hair1_01'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y +0.15
VRoidModel.edit_bones['J_Sec_Hair2_01'].head.x = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.x
VRoidModel.edit_bones['J_Sec_Hair2_01'].head.y = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.z * -1
VRoidModel.edit_bones['J_Sec_Hair2_01'].head.z = Sims4Model.bones['b__CAS_NoseBridge__'].head_local.y +0.15 -0.05
VRoidModel.edit_bones['J_Sec_Hair2_01'].length = 0.05

VRoidModel.edit_bones['J_Sec_R_CoatSkirtSide1_01'].head.x = Sims4Model.bones['b__R_Calf__'].head_local.x - 0.12
VRoidModel.edit_bones['J_Sec_R_CoatSkirtSide1_01'].head.y = Sims4Model.bones['b__R_Calf__'].head_local.z * -1
VRoidModel.edit_bones['J_Sec_R_CoatSkirtSide1_01'].head.z = Sims4Model.bones['b__R_Calf__'].head_local.y +0.05
VRoidModel.edit_bones['J_Sec_R_CoatSkirtSide1_01'].length = 0.15

VRoidModel.edit_bones['J_Sec_L_CoatSkirtSide1_01'].head.x = Sims4Model.bones['b__L_Calf__'].head_local.x + 0.12
VRoidModel.edit_bones['J_Sec_L_CoatSkirtSide1_01'].head.y = Sims4Model.bones['b__L_Calf__'].head_local.z * -1
VRoidModel.edit_bones['J_Sec_L_CoatSkirtSide1_01'].head.z = Sims4Model.bones['b__L_Calf__'].head_local.y +0.05
VRoidModel.edit_bones['J_Sec_L_CoatSkirtSide1_01'].length = 0.15
