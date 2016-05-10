__author__ = 'administrator'
from maya.cmds import *
node = ls(sl=1)
jnt = ls(sl=1)
n = len(node)
for i in range(n):
    connectAttr((node[i]+".position"),(jnt[i]+".translate"))


from maya.cmds import *
infoNd = ls(sl=1)
select(cl=1)
for i in infoNd:
    print(i)
    grp = group(em =1)
    connectAttr((i+".position"),(grp+".translate"))
    select(cl=1)




