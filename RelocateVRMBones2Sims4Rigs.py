import bpy

def relocate_init(in_armature):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.context.window.scene.objects[in_armature]
    bpy.ops.object.mode_set(mode='EDIT')

relocate_init('Armature')

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
VRoidModel.edit_bones['J_Sec_R_Bust2'].tail.y = Sims4Model.bones['b__CAS_R_Breast__'].head_local.z * -1 - 0.002 - 0.002
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
VRoidModel.edit_bones['J_Sec_L_Bust2'].tail.y = Sims4Model.bones['b__CAS_L_Breast__'].head_local.z * -1 - 0.002 - 0.002
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
