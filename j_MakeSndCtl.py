#!/usr/bin/env python
#coding:utf-8
u"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2015/12/18 13:29:25
  Description:
  次级生成脚本
  Instruction:
  
"""

import maya.cmds as mc
import pymel.core as pm

def j_MakeSecondContrl():
    j_sndcontrls = [];
    j_surface = []
    j_edges = mc.ls(os=1,fl=1);
    #loft -ch 1 -u 1 -c 0 -ar 1 -d 3 -ss 1 -rn 0 -po 0 -rsn true "MOBBodyAA.e[6450]" "MOBBodyAA.e[7030]";
    for i in (range(1,len(j_edges),2)):
        j_sndcontrls = mc.loft(j_edges[i-1],j_edges[i],ch=1,rn =0,ar =1,)
        j_surface.append(j_sndcontrls[0])
    mc.select(cl=1)
    j_grp = 'grp_loftSurface01';
    if not mc.objExists(j_grp):
        mc.group(n= "grp_loftSurface01",empty =1)
    mc.parent(j_surface,j_grp,);    
    for j in j_surface:
        j_pnd = pm.pointOnSurface(j,ch=1,u=0.5, v = 0.1, top =1,)
        j_position = pm.getAttr(j_pnd + ".position")
        j_loc = mc.spaceLocator( p = (j_position[0], j_position[1] , j_position[2]))
        j_circle = pm.circle(ch = 0)
        j_pnt = pm.group(em = 1 , ) 
        pm.parentConstraint()
        
    return j_surface;  
