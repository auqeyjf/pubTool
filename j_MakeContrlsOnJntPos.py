#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com 
  Created: 2016/5/31 15:07:58
  Description:
  
  Instruction: 根据给定骨骼和控制器，在骨骼位置生成一个新的控制器，并将骨骼做为新控制器的子物体
  
"""

import maya.cmds as mc

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