#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2016/1/14 16:36:50
  Description:
  找出场景中低于指定数量的模型
  Instruction:
  j_findMesh()
"""

import maya.cmds as mc

def j_findMesh(faceNum=5):
    '''
    find out the less than faceNum object;
    '''
    j_meshNode = mc.ls(type='mesh')
    j_finalObj = []
    for i in j_meshNode:
        j_meshParent = mc.listRelatives(i , parent =1 )
        j_faceNum = mc.polyEvaluate(j_meshParent[0],face=1)
        
        if j_faceNum<= faceNum:  # if current mesh's face less than faceNum ,return the object to j_finalObj 
            j_finalObj.append(j_meshParent[0]) 
            
    mc.select(j_finalObj)
    
def j_findEmptyGrp():
    ''' check out the empty group '''
    j_transform = mc.ls(type = 'transform')
    j_finalGrp = []
    j_allType = ['joint',u'orientConstraint' , u'parentConstraint' ,  u'ikEffector' , u'ikHandle', u'poleVectorConstraint']
    for i in j_transform:
        j_child = mc.listRelatives(i,children = 1)
        j_Type = mc.ls(i,showType=1)
        if j_child == None:
            j_finalGrp.append(i)
    mc.select(j_finalGrp)
