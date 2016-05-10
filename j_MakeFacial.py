#!/usr/bin/env python
#coding:utf-8
"""
  Author:   Jiangjishi 
  E-mail:   auqeyjf@163.com
  Q    Q:  287236623
  Created:  2015/6/23 16:04:42
  Purpose:  表情制作
  
"""

'''
import maya.cmds as mc
#设置当前选择的物体不可渲
j_obj = mc.listRelatives(c=1);
for j_item in j_obj:
    mc.setAttr((j_item+'.castsShadows'),0)
    mc.setAttr((j_item+'.receiveShadows'),0)
    mc.setAttr((j_item+'.motionBlur'),0)
    mc.setAttr((j_item+'.primaryVisibility'),0)
    mc.setAttr((j_item+'.visibleInReflections'),0)
    mc.setAttr((j_item+'.visibleInRefractions'),0)
    mc.setAttr((j_item+'.doubleSided'),1)
    mc.setAttr((j_item+'.smoothShading'),0)
    mc.setAttr((j_item+'.overrideEnabled'),1)
    mc.setAttr((j_item+'.overrideDisplayType'),2)    
'''

# 1  选点生成骨骼，并新建图层
import maya.cmds  as mc

def MakeMouthSndJnt():
    mouthPnt = mc.filterExpand (sm=31)
    mc.select (cl=1)
    lx_mouthJnt=[]
    lx_num =1
    for lx_i in mouthPnt :
        lx_pos = mc.xform (lx_i ,q=1,ws =1,t=1)
        lx_jnt = mc.joint (n=("snd_mouthLip"+str(lx_num )),p=(lx_pos [0],lx_pos [1],lx_pos [2]),radius= 0.1)
        lx_mouthJnt .append(lx_jnt )
        mc.select (cl=1)
        lx_num += 1
    mc.select (lx_mouthJnt,r=True )
    mc.createDisplayLayer (name="Layer_MouthSnd",num = 1,nr=1)
    mc.setAttr ("Layer_MouthSnd.displayType",0)
    mc.setAttr ("Layer_MouthSnd.color",4)
    mc.group(n = "grp_mouthSnd01",w=1,em=1)
    mc.select (all=1)
    mc.select (cl=1)
    mc.parent(lx_mouthJnt ,"grp_mouthSnd01")

# 2.  给上一步生成的骨骼打两层组
def MakeGroupForJnt():
    mc.select (lx_mouthJnt,r=True )
    lx_jntPos =[]
    lx_jntSets =[]
    for lx_i in lx_mouthJnt :
        lx_jntPos = mc.xform(lx_i,q=1,ws=1,t=1)
        lx_grp01 =mc.group (n=("grp_"+lx_i +"01"),em=True ,p='grp_mouthSnd01')
        lx_grp02 =mc.group (n=("grp_"+lx_i +"03"),em=True ,p=("grp_"+lx_i +"01"))
        mc.setAttr(("grp_"+lx_i +"01.translate"),lx_jntPos[0],lx_jntPos[1],lx_jntPos[2],type = "double3")
        mc.setAttr(("grp_"+lx_i +"03.translate"),0,0,0,type = "double3")
        mc.parent (lx_i,("grp_"+lx_i +"03"))
    
# 3. 在mesh_*MouthLip 上创建 pointOnSurface 节点   
''' 生成节点后，顺带生成一个空组grp_snd_mouthLipxx02，显示局部坐标，让节点链接上这个空组，
     将这个空组做为grp_snd_mouthLipxx01 的子物体，将grp_snd_mouthLipxx03做为grp_snd_mouthLipxx02的子物体，
     并设置grp_snd_mouthLipxx01和grp_snd_mouthLipxx03的translate为0 0 0 ，并将grp_snd_mouthLipxx01重新归中心：xform -cp;
'''
# import maya.cmds as mc
def MakePointOnSurfaceNd(surface):
    mc.select ("mesh_*MouthLip")
    lx_mesh = mc.ls(sl=1)
    mc.select ("snd_mouthLip*")
    lx_sndJnt = mc.ls(sl=True )  
    lx_node ,lx_locGrp=[],[]
    for lx_i in lx_sndJnt :
        lx_temp=mc.xform(lx_i,q=1,ws =1,t=1)
        lx_locN= "loc_"+lx_i 
        mc.spaceLocator(n=lx_locN,a=1,p=(lx_temp[0],lx_temp[1],lx_temp[2]))
        lx_locGrp.append(lx_locN)
        lx_null = 'grp_'+lx_i+'02'
        mc.group(n=lx_null,em =1)
        mc.toggle (lx_null,la=1)
        mc.parent (lx_null ,('grp_'+lx_i+'01'))
        mc.parent (('grp_'+lx_i+'03'),lx_null)
        nd=mc.pointOnSurface(lx_mesh,ch=True )
        #lx_node.insert(1,nd);
        ndName = "pntNd_"+lx_i 
        mc.rename(nd,ndName )
        mc.connectAttr ((ndName +".position"),('grp_'+lx_i+'02.translate'))
        mc.setAttr (('grp_'+lx_i+'01.translate'),0,0,0,type ="double3")
        mc.setAttr (('grp_'+lx_i+'03.translate'),0,0,0,type="double3")
        mc.xform (('grp_'+lx_i+'01'),cp=True)
    mc.select(cl=1)
    mc.select(lx_locGrp )
    mc.group (n="grp_locMouthLip01")



# 4. 调整UV数值，调整完UV需要再归一次中心
# import maya.cmds as mc
def MakeUVValue():
    mc.select ("snd_mouthLip*")
    lx_sndJnt = mc.ls(sl=True )  
    for lx_i in lx_sndJnt :
        mc.xform (('grp_'+lx_i+'01'),cp=True)

# 5. 给曲面生成控制骨骼，这里的骨骼要与嘴的模型对应轴向，并蒙皮

# 6. 根据Jaw_M，JawEnd_M，生成一个骨骼链。
# import maya.cmds as mc
def MakeNewJawSkeleton():
    lx_jawSPt  =mc.xform ("Jaw_M",q=1,ws=1,t=1)
    lx_jawEPt =mc.xform("JawEnd_M",q=1,ws=1,t=1)
    mc.joint(n="JawCenter01",p=(lx_jawSPt[0],lx_jawSPt[1],lx_jawSPt[2]))
    mc.joint (n="JawCenterEnd01",p=(lx_jawEPt[0],lx_jawEPt[1],lx_jawEPt[2]))
    mc.select (cl=1)
    mc.joint ("JawCenter01",e=1,zso=1,oj="xyz")
    mc.setAttr ("JawCenterEnd01.jointOrient",0,0,0,type ="double3")

# 7. 选择嘴部次级骨骼，用头部骨骼和JawCenter01同时约束嘴部次级骨骼们。

#import  maya.cmds  as mc
def MakeParentConstrain():
    lx_sel=mc.ls(sl=1)
    mc.parent("JawCenter01","Head_M")
    mc.parentConstraint ("Jaw_M","JawCenter01",maintainOffset=1)
    for lx_i in lx_sel :
        mc.parentConstraint ("Head_M","JawCenter01",("grp_"+lx_i+'01'),maintainOffset=1)


# 8.调整约束权重，并手动驱动
""" 在张嘴状态下调整权重，使得次级骨骼贴合嘴型，然后用口型控制器再驱动权重值。将次级骨骼添加到脸上，刷权重。
     这次换一种方式，不用微调权重值，只控制步差，让它错开。
     用权重来补齐因约束权重修补效果差的地方
     
     驱动的方式就是在控制为0的时候K一次，1k一次，然后在0.5的时候调成一个o口型。
""" 

#-------------------------------  眼睛制作 ----------------------------------------------------
# 1. 选择眼球中心骨骼，会生成骨骼之前，生成一个loc_EyeCenter01来定位眼球中心

def MakeCenterLoc(CenterJnt):
#----------------------------------------------------------------------
    lx_cPos= mc.xform(CenterJnt,q=1,ws=1,t=1)
    mc.spaceLocator (n="loc_eyeCenter01",p=(0,0,0))
    mc.xform("loc_eyeCenter01",ws=1,t=(lx_cPos[0],lx_cPos[1],lx_cPos[2]))

#2. 选择两圈眼球上的线，生成
#----------------------------------------------------------------------
def  MakeJntAndIKs(side):
    """
    选择两圈眼球上的线，生成骨骼和ik，side的值例如：R_In or R_Out
    ps: 选择骨骼链的子物体，打组，centerPivot，在原点生成一个骨点，用组约束骨点，正确命名，然后将IK组分别放到对应骨点下边。
    """    
    lx_start=mc.xform('loc_eyeCenter01',q=1,ws=1,t=1)
    lx_mouthPnt= mc.filterExpand(sm=31)
    mc.select (cl=1)
    lx_Jnts=[]
    lx_IKs = []
    for i in lx_mouthPnt :
        lx_end=mc.xform(i,q=1,ws=1,t=1)
        lx_stJnt=mc.joint (n=("Jnt_"+side+"_st"),p=(lx_start[0],lx_start[1],lx_start[2]),radius=0.1)
        lx_edJnt=mc.joint (n=("Jnt_"+side+"_ed"),p=(lx_end[0],lx_end[1],lx_end[2]),radius=0.1)        
        lx_scik =mc.ikHandle (n=("scik_"+side+str(01)),sj=lx_stJnt,ee=lx_edJnt,sol="ikSCsolver")
        #mc.setAttr((str(lx_scik[0]) +".visibility") ,0)
        mc.select(cl=1)
        lx_Jnts.append(lx_stJnt)
        lx_IKs .append(lx_scik[0])
    mc.select(lx_Jnts,r=1)
    mc.group(n=("grp_Jnts"+side))
    
    mc.select(lx_IKs,r=1)
    mc.group(n=("grp_iks"+side))
    mc.setAttr((str("grp_iks"+side) +".visibility") ,0)
    
#3.选择眼皮曲线，执行脚本，生成
    def  MakeEyeLidJnts(cuvs):
        
        