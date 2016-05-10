#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2015/11/12 13:59:03
  Description: export \ import animation curves
  
  Instruction: 
                     1.  Export  Animation:  
                                                                select all animation curves to export 
                     2.  Import Animation:
  
"""

import maya.cmds as mc
import json

def ExportAniData():
#选择控制器，然后逐个控制器读属性，把数据写成字典。    
    contrlCuvs = mc.ls(sl=1)
    
#----------------------------------------------------------------------
def ImportAniData():
#如果当前有选择的控制器，就仅仅给当前选择的控制器导入动画；
#若没有选择控制器，则导入文件里所有动画。
    contrler =  mc.ls(sl =True)
    f = open('D:/AniData.json','r')
    if(len(contrler)==0):# 没有选择控制器
        