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