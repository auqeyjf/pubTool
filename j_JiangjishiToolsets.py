#!/usr/bin/env python
#coding:utf-8
u'''
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2016/1/14 16:36:50
  Description:
  "工具集 ToolSet"
  Instruction:
  j_findMesh()
"""'''

import maya.cmds as mc
import pymel.core as pm
import math

def j_findMesh(faceNum=5):#1
    u'''找出少于指定数量的物体'''
    j_meshNode = mc.ls(type='mesh')
    j_finalObj = []
    if len(j_meshNode) == 0:
        print( u'当前场景中没有poly物体，THERE IS NOTHING TO OPERATE !');
        return 0 ;
    for i in j_meshNode:
        j_meshParent = mc.listRelatives(i , parent =1 )
        j_faceNum = mc.polyEvaluate(j_meshParent[0],face=1)
        
        if j_faceNum<= faceNum:  # if current mesh's face less than faceNum ,return the object to j_finalObj 
            j_finalObj.append(j_meshParent[0]) 
            
    if len(j_finalObj) == 0:
        print("There Is No Mesh Has Less Than %s FACES !!!"%(faceNum))
        return 0;
    else:
        mc.select(j_finalObj)

def j_findEmptyGrp():#2
    u''' 找空组 '''
    j_transform = mc.ls(type = 'transform')
    j_finalGrp = []
    if len(j_transform) == 0:
        print("There Is No Transform In Current Scene !")
        return 0 ;    
    for i in j_transform:
        j_child = mc.listRelatives(i,children = 1)
        
        if (j_child == None):
            j_finalGrp.append(i)

    if len(j_finalGrp) == 0:
        print u"当前场景没有空组。THERE IS NO TRANSFORM IS NULL GROUP !!!"
        return 0;
    else:
        mc.select(j_finalGrp)
    
def j_findNoZeroObj():#3
    u''' 检查所选模型是不是冻结过通道栏
    '''
    #mc.select(hi=1)
    #j_root = mc.ls(sl =1) # select the current grp's children
    
    #if (len(j_root) == 0):
    #    raise ValueError("j_geo must be not None , Please select at least one object!")
    
    j_objects = mc.listRelatives(mc.ls(type = 'mesh'),parent = 1)
    mc.select(cl =1 )
    j_noFreezeObjs=[]
    for i in j_objects:
        tx = mc.getAttr(i+".tx")
        ty = mc.getAttr(i+".ty")
        tz = mc.getAttr(i+".tz")
        
        rx = mc.getAttr(i+".rx")
        ry = mc.getAttr(i+".ry")
        rz = mc.getAttr(i+".rz")
        
        sx = mc.getAttr(i+".sx")
        sy = mc.getAttr(i+".sy")
        sz = mc.getAttr(i+".sz")
        
        j_sum = sum([tx,ty,tz,rx,ry,rz,sx,sy,sz])
        if j_sum != 3.0:
            j_noFreezeObjs.append(i)
    mc.select(j_noFreezeObjs , r =1)

def j_checkNameSpace():#4
    u'''找出当前场景中的名字空间'''
     
    j_defaultNP = ["UI" , "shared"]
    j_newNameSpace = mc.namespaceInfo(lon = 1)
    j_oldnum = len(j_newNameSpace)
    j_newnum = len(j_defaultNP)
    
    if j_oldnum != j_newnum:
        print(u"当前场景包含其它名字空间，请清理！！！！！！！！")
    else:
        print(u"当前场景不包含其它名字空间。安好")
        

def j_findoutNoVertexMeshObj():#5
    u'''找出没有点的mesh '''
    j_meshNode = mc.ls(type='mesh')
    j_finalObj = []    
    if len(j_meshNode) == 0:
                j_text1 = "THERE IS MESHES IN CURRENT SCENE !"
                return j_text1 ;       
    for i in j_meshNode:
        j_temp = mc.polyInfo(i , fv =1)
        
        if (j_temp == None):
            j_temp = mc.listRelatives(i , parent = 1)
            j_finalObj.append(j_temp[0])
    if len(j_finalObj) == 0:
        j_text2 = "THERE IS MESHES IN CURRENT SCENE !"
        return j_text2 ;               
    else:
        mc.select(j_finalObj , r = 1)
 
def j_findInstanceDup():#6
    u'''
     找出关联复制的物体
    '''
    j_meshNode = mc.ls(type='mesh')
    if len(j_meshNode) == 0:
        j_text1 = u'There Is No Mesh To Operate !';
        return j_text1 ;     
    j_finalObj = []
    for i in j_meshNode:
        j_meshParent = mc.listRelatives(i , allParents =1 )
        j_faceNum = len(j_meshParent)        
        if j_faceNum > 1:  # if bigger than 1 ,that's mean the current shape has more than 1 parent
            for j in j_meshParent:
                j_finalObj.append(j) 
            
    if len(j_finalObj) == 0:
        j_text2 = "There Is No Meshes In Current Scene!"
        return j_text2 ;               
    else:
        mc.select(j_finalObj , r = 1)        

def j_findBoundaryEdges():#7
    u'''
      找出所有模型的边界
    '''
    j_objects = pm.ls(type = "mesh")
    if len(j_objects) == 0:
            j_text1 = u'There Is No Mesh To Operate !';
            return 0 ;    
    j_boundEdge = []
    for m in j_objects:
        for i in m.e:
            if i.isOnBoundary():
                j_boundEdge.append(i)        
        pm.select(j_boundEdge)  
        

def j_findMuchShapesObj():#8
    u'''找出有多个Shape的物体'''
    j_meshNode = mc.listRelatives(mc.ls(type='mesh') , parent =1 )
    if len(j_meshNode) == 0:
        j_text1 = u'There Is No Mesh To Operate !';
        return j_text1 ;    
    j_muchShape = []
    for i in j_meshNode:
        j_temp = mc.listRelatives(i , children =1)
        if (len(j_temp)>1):
            j_muchShape.append(i)
    mc.select(j_muchShape, r =1) 
    
def j_vertexNoFreeze():#9
    u'''找出 点 (vertex)没有清0的模型'''
    j_object = mc.ls(type = "mesh")
    if len(j_object) == 0:
        j_text1 = u'There Is No Mesh To Operate !';
        return j_text1 ;
            
    j_finalObj = []
    for i in j_object:
        j_x = mc.getAttr( i +'.pnts[0].pntx')
        if j_x != 0:
            j_finalObj.append(i)
            
            
    mc.select(j_finalObj)
    
def j_doFreezeVtx(): #10
    u'''
    清除点的位移信息
    '''
    obj = mc.ls(type = "mesh")
    if len(obj) == 0:
            j_text1 = u'There Is No Mesh To Operate !';
            return j_text1 ;    
    mc.select(clear =1)
    for i in obj:
        mc.polySoftEdge( i, a =180 , ch = 0 )
        mc.delete( obj , ch =1 )
        mc.select(obj , r =1)
    print "Complete !!"     
    
def j_MakeContrlsOnJntPos():
    u'make a new contrl on position of specify joint'
    jnt,ctrl = mc.ls(sl=True)
    ctrl_n = mc.duplicate(ctrl)
    mc.select(cl =1 )
    ctrl_grp = mc.group(em = 1,n = ("grp_"+ctrl_n[0]))
    temp = mc.parentConstraint(jnt , ctrl_n, maintainOffset = False)
    mc.delete(temp)
    temp = mc.parentConstraint(ctrl_n, ctrl_grp, maintainOffset = False )
    mc.delete(temp)
    mc.parent(ctrl_n,ctrl_grp)
    temp = mc.parentConstraint(jnt, ctrl_grp)
    mc.delete(temp)
    mc.parent(jnt, ctrl_n)
    mc.select(ctrl, r = True)
    shape = mc.listRelatives(ctrl_n[0], children = 1)[0]
    mc.setAttr((shape + ".overrideEnabled"), 1 )
    mc.setAttr((shape + ".overrideColor"), 4 )        
    
    
    
def j_fixAdv3_99_forMaya2016():
    'fix advanceSkeleton v3.99 stretch not work in maya2016'
    j_drivenKey = {"antiPop":4.990848, "normal":4.878867}
    
    for drv in j_drivenKey: #数值 
        for pat in ("Arm","Leg"):  #arm or leg
            for side in ("_R","_L"):
                for i in ("antiPop","normal"):
                    mc.selectKey(("IKdistance" + pat + side +"Shape_"+ i), ot =True, f = (j_drivenKey[drv],))
                    mc.keyTangent(("IKdistance" + pat + side +"Shape_"+ i), lock = False,)
                    mc.keyTangent( itt = "clamped",ott = "clamped",)       
                    
def j_createRigHead():
    u'create some groups'
    mc.select(cl =True)
    filename_type = mc.file(q = 1,sn = 1,shn = 1)
    filename = filename_type[:-3]
    g1 = mc.group(em =1,n = (filename + "_Rig"))
    g2 = mc.group(em =1,n = "Geometry")
    g3 = mc.group(em =1,n = "GlobalSetting")   
    g4 = mc.group(em =1,n = "Grp_Master")
    mc.parent(g2,g3,g4,g1)
    
    
def j_changeOverrideColor(colorNum = 4):
    u'set the overrideColor [4 暗红] [15 浅蓝] [22 淡黄] 6 亮蓝  13 亮红 14 亮绿  17黄色  23 淡绿 28 淡蓝 18 adv'
    contrls = mc.ls(sl =1)
    for item in contrls:
        shape = mc.listRelatives(item,children =1)[0]
        mc.setAttr((shape + ".overrideEnabled"),1)
        mc.setAttr((shape + ".overrideColor"),colorNum)


def j_MakeStretchy(mainContrl="Main"):
    u'做拉伸,主控制器，先选骨骼链，最后选ik曲线'
    #ready
    jnt = mc.ls(sl =True)[:-1]
    cuv = mc.ls(sl =True)[-1]
    arcNode = mc.arclen(cuv,ch =True,)  
    num = len(jnt)
    #operater
    length = mc.getAttr((arcNode + ".arcLength"))
    # mainScale = mc.getAttr((mainContrl+".scaleX"))
    md1 = mc.createNode('multiplyDivide')
    md2 = mc.createNode('multiplyDivide')
    #md3 = mc.createNode('multiplyDivide')
    mc.connectAttr((mainContrl+".scaleX"),(md1 +".input1X"))
    mc.setAttr((md1 +".input2X"),length)
    
    mc.connectAttr((arcNode+".arcLength"),(md2+".input1X"))
    mc.connectAttr((md1+".outputX"),(md2 +".input2X"))    
    mc.setAttr((md2+".operation"),2)
    axiss = ("X","Y","Z")
    nodeNumA = (num*1.0)/3 # num%3 #
    #nodeNumB = math.ceil(nodeNumB)
    nodeCount = int(math.ceil(nodeNumA))
    attr = 0
    for n in range(nodeCount):
        mdnode = mc.createNode('multiplyDivide')        
        for i in axiss:
            print attr
            if attr>=(num):
                break
            tranX = mc.getAttr(jnt[attr] + ".tx")
            mc.setAttr((mdnode + ".input2" + i),tranX) #设置为骨骼的初始位移值
            mc.connectAttr((md2+".outputX"),(mdnode + ".input1"+i))
            mc.connectAttr((mdnode+".output"+i),(jnt[attr]+'.tx'))
            attr +=1                  
    
    #compelte
            