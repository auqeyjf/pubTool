import maya.cmds as mc

objs=mc.ls(sl=1);
shapes=[]
for  i in objs:
    shapes.append(i+"Shape01Orig");
    
mc.delete(shapes);   