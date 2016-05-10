#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2015/11/26 10:44:25
  Description:
           j_AboutRender()
  Instruction:
     根据需要，替换不同后缀的文件，方便制作
"""

import maya.cmds as mc

def j_AboutRender():
    # FILE LIST
    j_allRefNodes = mc.ls(type = 'reference')
#global    
    j_currentRefNodes =  j_labelPath= []
    
    for i in j_allRefNodes:
        j_temp = i.split(':')
        j_num =  len(j_temp)-1
        if j_num and  j_temp[0] =='shareReferenceNode':
            j_currentRefNodes.append(j_allRefNodes[i])
           #
            j_labelPath.append(mc.referenceQuery(j_allRefNodes[i],f=1))
            #
            

    #UI;
    if mc.window(j_AboutRender,ex=1):
        mc.deleteUI(j_AboutRender)
        
    j_checkBoxes = j_pathText = []
    mc.window(j_AboutRender,t='ChangerRenderFileType Window ',s=0,wh=(500,500))
    mc.frameLayout(h=400,cl1=1,l='Reference File List:')
    mc.columnLayout()
    mc.scrollLayout(h=350,w=490)
    columnLayout()
    for j in j_currentRefNodes:
        mc.rowLayout(nc=2,cw2=(130,300))
        j_checkBoxes.append(mc.checkBox(j_currentRefNodes[j],l=1,))
        j_pathText.append(mc.text(j_labelPath[j],l=1))
        mc.setParent('..')
        mc.setParent('..')
        
        
    mc.rowLayout(nc=3,cw3=(80,80,80))
    mc.button(w=75,l='Update',c='j_AboutRender')
    mc.button(w=75,l='Select All',c='j_Choice 1')  #同下
    mc.button(w=75,l='Select All',c='j_Choice  0')  #命令格式得修
    mc.setParent('..')
    mc.frameLayout(cl1=1,l='Change File')
    mc.rowLayout(nc=4,cw4=(100,100,100,100))
    mc.button(w=95,l='Beauty',c='j_ButtonCommand("Beauty")')
    mc.button(w=95,l='ID',c='j_ButtonCommand("ID")')
    mc.button(w=95,l='SSS',c='j_ButtonCommand("SSS")')
    mc.button(w=95,l='Skin',c='j_ButtonCommand("Skin")')
    mc.setParent('..')   
    mc.showWindow(j_AboutRender)
    
    
def j_ButtonCommand(j_buttonLabel):
    global j_labelPath,j_checkBoxes,j_pathText,j_currentRefNodes
    j_checkBoxValues = newLabels = buffer
    
    for i in j_checkBoxes:
        if mc.checkBox(j_checkBoxes,q=1,v =1):
            i.split["_"]
            
    
                       