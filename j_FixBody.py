#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2015/12/9 14:02:19
  Description:  
                        duplicate joint base from advanceskeleton,like 'ShoulderPart2_L','Elbow_L','ElbowPart1_L','HipPart2_L','Knee_L','KneePart1_L'
                        and create ikhandle with ikSCsolver, parent to their parent
  Instruction:
                        j_BodyFix();
"""
import maya.cmds as mc
import re
def j_BodyFix():
    # Get The Goal Joint position 
    position = dict()
    dupJnt = ['ShoulderPart2_L','Elbow_L','ElbowPart1_L','HipPart2_L','Knee_L','KneePart1_L']
    for jnt in dupJnt:
        position[jnt] =mc.xform(jnt,ws=1,t=1,q=1)
        
    # Create  Joint  And Ikhandle From position
    newJnt = []
    na =1;
    for j in dupJnt: 
        if mc.objExists(('Fix'+j)):
            mc.select(('Fix'+j),r=1)
            break;
        newJnt.append(mc.joint(n=('Fix'+j),p=position[j],radius=1.75))
        if na%3==0:        
        # Create IKHandle With ikRPsolver , Then Mirror With IkHandle
            mc.joint(newJnt[0],e=1,zso=1,oj='xyz',sao='yup')
            mc.joint(newJnt[1],e=1,zso=1,oj='xyz',sao='yup')
            mc.setAttr('%s.jointOrient'%newJnt[2],0,0,0)
            ikhand = mc.ikHandle(name=('rpik_'+newJnt[1]+'01'),sj=newJnt[0],ee=newJnt[2],sol = 'ikSCsolver')
            mc.setAttr('%s.v'%ikhand[0],0)
            # mirrorJoint -mirrorYZ -mirrorBehavior -searchReplace "_L" "_R";
            mc.mirrorJoint(newJnt[0],mirrorYZ =1,mirrorBehavior =1,searchReplace=('_L','_R'))
            mc.parent(ikhand[0],j)
            mc.parent((re.sub('_L',"_R",ikhand[0])),(re.sub('_L','_R',j)))
            mc.parent(newJnt[0],dupJnt[na-3])
            mc.parent((re.sub("_L","_R",newJnt[0])),(re.sub('_L','_R',dupJnt[na-3])))
            newJnt = []       
            mc.select(clear=1)
        na=na+1; 
      