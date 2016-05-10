# Author : Jiangjishi
# Date: 2015/06/12
# 
import maya.cmds as mc
def getShaders():
    shaders =list()
    objects = mc.ls(sl=1)
    for obj in objects :
        shape = mc.listRelatives (obj,s=1,path=1)
        if not shape:
            continue 
        meterial_SG = mc.listConnections (shape[0],type='shadingEngine')
        shaders .extend (meterial_SG )
    
    
        shaders = [m for i,m in enumerate (shaders ) if m not in shaders [:i]]
        return shaders
    