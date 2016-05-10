#!/usr/bin/env python
#coding:utf-8
u"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2016/2/24 11:58:32
  Description:
  UI 镜像表情
  Instruction:
  
  j_MirrorBlendshape()
  
"""

import maya.cmds as mc
import maya.mel as mel

def j_MirrorBlendShape():
    '''
     UI
    '''
    global text1
    global text2 
    global text3
    j_MainWindow = ""
    if (mc.window(j_MainWindow, exists = 1 )):
        mc.deleteUI(j_MainWindow)
    j_MainWindow = mc.window(title = u"镜像表情", wh = (300,160))
    mc.columnLayout()
    mc.text(l = "")
    text1 = mc.textFieldButtonGrp( l = u"BaseObject：", buttonLabel = u"    < < < <    ", 
                          buttonCommand = 'xanthus.j_MirrorBlendShape.j_getObj(1)', cw3 = (90,120,100),h = 30)
    
    text2 = mc.textFieldButtonGrp(l = u"In-Between：", buttonLabel = u"    < < < <    ",
                          buttonCommand = "xanthus.j_MirrorBlendShape.j_getObj(2)", cw3 = (90,120,100),h = 30,enable = 0)
    
    text3 = mc.textFieldButtonGrp(l = u"BlendShape：", buttonLabel = u"    < < < <    ", 
                          buttonCommand = "xanthus.j_MirrorBlendShape.j_getObj(3)", cw3 = (90,120,100),h = 30)
    
    mc.text(l = "",h = 10)
    mc.setParent('..')
    mc.rowLayout(nc = 2 ,cw2= (150,150),ct2 = ("left","left") ,co2 = (8,0) )
    mc.button(l = u" 镜    像 ", w = 135, h= 30,c = "xanthus.j_MirrorBlendShape.j_MakeMirror()")
    mc.button(l = u" 重    置 ", w = 135, h= 30,c = "xanthus.j_MirrorBlendShape.j_Reset()")
    mc.setParent('..')
    mc.columnLayout
    mc.text(l = "                        copyright@ xanthus by Jiangjishi ", enable = 0)
    mc.showWindow(j_MainWindow)
    
def j_getObj(value):
    u'''
     获取物体
    '''
       
    global text1, text2, text3
    if value == 1:
        #1 text1
        v1 = mc.ls(sl = 1)[0]
        mc.textFieldButtonGrp(text1,e =1 , text = v1)
    
    if value == 2:
        #3 text2
        v2 = mc.ls(sl = 1)[0]
        mc.textFieldButtonGrp(text2,e =1 , text = v2)
        
    if value == 3:
        #3 text3
        v3 = mc.ls(sl = 1)[0]
        mc.textFieldButtonGrp(text3,e =1 , text = v3)
        
def j_MakeMirror():
    u'''
    镜像
    '''
    global text1
    global text2 
    global text3
    j_bsName = mc.textFieldButtonGrp(text3,q = 1,text =1)
    all_newTargets = []
    #duplicate base geometry
    j_baseGeo = mc.textFieldButtonGrp(text1,q = 1,text = 1)
    #复制出包裹物体
    j_wrapGeo = mc.duplicate(j_baseGeo)[0]
    j_bsNd = mc.textFieldButtonGrp(text3,q =1,text = 1)
    #设置负X轴
    mc.setAttr(j_wrapGeo+".sx", -1)
    #包裹变形
    mc.select(j_wrapGeo,j_baseGeo,r = 1,)
    cmd='string $wraps[]=`doWrapArgList "7" { "1","0","1", "2", "1", "1", "0", "0" }`;'
    r_cmd = mel.eval(cmd)
    
    #获取bs节点的变形属性列表
    j_tgt = mc.listAttr(j_bsNd,k =1, m = 1,s =1,r =1 ,c =1 ,v =1)
    j_tgt.pop(0)
    #循环设置bs的各个属性，并逐个复制模型
    position = []
    for i in j_tgt:
        position = mc.xform(i,ws=1,q= 1,t =1)
        j_translate = [-position[0],position[1],position[2]]
        mc.setAttr((j_bsNd + "." + i), 1)
        newTgt = "j_"+i
        all_newTargets.append(newTgt)
        mc.duplicate(j_wrapGeo,n = newTgt)
        mc.setAttr((j_bsNd + "." + i), 0)
        mc.setAttr(newTgt+".sx", 1)
        mc.xform(newTgt,ws =1 ,t =j_translate)
        
    mc.select(all_newTargets,r =1 )
    mc.group(n = "grp_newTgt_" + j_bsName, world = 1 )
    mc.delete(j_wrapGeo)    
    j_complete = u"猴赛雷，完成了!!!!!!"
    
    print j_complete
    return all_newTargets
    
def j_Reset():
    '''
    reset
    '''
    
    global text1, text2, text3
    mc.textFieldButtonGrp(text1,e =1 , text = '')
    mc.textFieldButtonGrp(text2,e =1 , text = '')
    mc.textFieldButtonGrp(text3,e =1 , text = '')
    