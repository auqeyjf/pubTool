#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2016/1/17 17:11:01
  Description:
  
  Instruction:
  
"""

import maya.cmds as mc
import pymel.core as pm



def j_vertexNoFreeze():
    '''
     找出 点 (vertex)没有清0的模型
    '''
    j_object = mc.ls(type = "mesh")
    j_finalObj = []
    for i in j_object:
        for j in range(1 , 10):
            j_x = mc.getAttr( i +'.pnts[0].pntx')
            if j_x != 0:
                j_finalObj.append(i)
            
            
    mc.select(j_finalObj)

mc.polyEvaluate('pCube5pCube5Shape' , v =1 )

def j_doFreezeVtx():
    '''
    do freeze vertex position on channelBox
    '''
    obj = mc.ls(sl = 1)
    mc.select(clear =1)
    for i in obj:
        mc.polySoftEdge( i, a =180 , ch = 0 )
        mc.delete( obj , ch =1 )
        mc.select(obj , r =1)
    print "Complete !!"    
    
    
    
    
    
u'''找出少于指定数量的物体'''
j_meshNode = mc.ls(type='mesh')
j_finalObj = []
if len(j_meshNode) == 0:
    print "THERE IS NOTHING TO OPERATE!"
    #return;
for i in j_meshNode:
    j_meshParent = mc.listRelatives(i , parent =1 )
    j_faceNum = mc.polyEvaluate(j_meshParent[0],face=1)
    if j_faceNum<= faceNum:  # if current mesh's face less than faceNum ,return the object to j_finalObj 
        j_finalObj.append(j_meshParent[0]) 
if len(j_finalObj) == 0:
    print "THERE IS NO MESH HAVE LESS THAN %s!"%(faceNum)
    #return
else:
    mc.select(j_finalObj)    