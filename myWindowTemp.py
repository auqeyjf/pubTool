#=============================================
# author: Jiangjishi    
#   mail: auqeyjf@163.com
#   date: 06/15/15  17:28
#=============================================

import maya.cmds as cmds
#----------------------------------------------------------------------
def  ExportImportShading():    
    j_win = cmds.window (title= "Export && Import Materials By Jiangjishi" ,w= 350,h=50,sizeable =0,mnb=0,mxb=0,rtf=1)
    cmds.columnLayout ()
    cmds .rowLayout(nc = 3,w=350,adjustableColumn=1)
    cmds.button(l="Export",c="shaderIOTt.shaderCore.exportGeometryShader()",w = 160,h=40)
    cmds.button(l="Import",c="shaderIOTt.shaderCore.importGeometryShader()",w = 160,h=40)
    cmds.setParent('..')
    cmds.text(l="Please select at least one object to Export!!",enable=0)
    cmds.text(l="Author: Jiangjishi            e-mail: auqeyjf@163.com" ,enable =0)
    cmds.showWindow(j_win )