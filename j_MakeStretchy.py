#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2016/5/20 18:39:28
  Description:
  
  Instruction:  auto create joints stretchy on translateX
  
"""

import maya.cmds as mc
jnts = mc.ls(sl =True)
cuv = mc.ls(sl =True)[0]
mainCtl = mc.ls(sl=True)[0] + '.ScaleX'
arcNode = mc.arclen(cuv,ch =True,)
jntCount = len(jnts)
axis = ("X","Y","Z")
i = 0
# get the right scale value

md1 = mc.createNode("multiplyDivide",n = 'md_scaleValue1')
md2 = mc.createNode("multiplyDivide",n = 'md_scaleValue2')

dftLength = mc.getAttr((arcNode + ".arcLength"))
dftScale = mc.getAttr((mainCtl + ".ScaleX"))

mc.setAttr((md1 + ".input1X"),dftLength )
mc.connectAttr((mainCtl + ".ScaleX") , (md1 + ".input1X"))
for jnt in jnts:
    
