#!/usr/bin/env python
#coding:utf-8
u"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2016/5/19 17:20:02
  Description:
  
  Instruction: fix advanceSkeleton v3.99 arm and leg can not stretchy 
  just run follow script
  
"""

import maya.cmds as mc

j_drivenKey = {"antiPop":4.990848, "normal":4.878867}

for drv in j_drivenKey: #数值 
    for pat in ("Arm","Leg"):  #arm or leg
        for side in ("_R","_L"):
            for i in ("antiPop","normal"):
                mc.selectKey(("IKdistance" + pat + side +"Shape_"+ i), ot =True, f = (j_drivenKey[drv],))
                mc.keyTangent(("IKdistance" + pat + side +"Shape_"+ i), lock = False,)
                mc.keyTangent( itt = "clamped",ott = "clamped",)            
            
        
        
