import maya.cmds as mc
#ѡ��lip�����棬���ɿ���mesh_KouXingBase ��� �ڿ���Ŀ���壬�Զ���bs,����ڵ�����Ϊ��bs_MouthKouXing.�����������ƣ�bs_MouthKouXingBase
lx_mesh = mc.ls(sl=1);
mc.select(clear=1);
mc.duplicate (lx_mesh, n="mesh_KouXingBase");
lx_kxName=("AA","HH","EE","SS","WW","OO","MM","LL","FF","UU");
lx_targets=[];
for lx_temp in lx_kxName :
    mc.duplicate(lx_mesh ,n=("mesh_"+ lx_temp ));
    lx_targets .append("mesh_"+lx_temp );
    
mc.select (lx_targets,r=1);
mc.select("mesh_KouXingBase",add=1);
mc.blendShape (frontOfChain=1,n="bs_MouthKouXing");

mc.select ("mesh_KouXingBase",lx_mesh,r=1);
mc.blendShape (frontOfChain=1,name="bs_MouthKouXingBase");

mc.setAttr("bs_MouthKouXingBase.mesh_KouXingBase",1);
mc.setAttr("bs_MouthKouXingBase.mesh_KouXingBase",lock=True );

# ########################### �������ķָ��� ##################################################

import maya.cmds as mc
#���ݹ������������mesh��������Ӧ����pointOnSurface node

# �����ɵ�ͬʱ�����ɶ�Ӧ�����Ŀ��飬����ʾ�ֲ�����
lx_mesh = mc.ls(sl=1);


lx_jnt = mc.ls(sl=1);
lx_node=[];
for lx_temp in lx_jnt :
    nd=mc.pointOnSurface(lx_mesh,ch=True );
    lx_node.insert(1,nd);
    mc.rename(nd,"pntNd_"+lx_temp);
    mc.group(empty=1,n=("nl_"+lx_temp));
    mc.connectAttr(("pntNd_"+lx_temp +".position"),("nl_"+lx_temp+".translate"));
    mc.toggle (("nl_"+lx_temp),localAxis=1);
    

import maya.cmds as mc
# �ϲ���һ�����ɵĿ����֮ǰ���ɵĴμ��������顣
lx_jntgrp = mc.ls(sl=1);
lx_nlgrp =mc.ls("nl_*");
    
for lx_i in lx_jntgrp :
    lx_chr  = "grp_" + lx_i + "01";
    lx_pnt = "nl_" + lx_i ;
    mc.parent(lx_chr ,lx_pnt )
    mc.toggle (("grp_" + lx_i + "02"),localAxis=1);
    mc.setAttr(("grp_" + lx_i + "01.translate") ,0,0,0,type ="double3");
    
    
import  maya.cmds as mc 
lx_pntNod=mc.ls("pntNd_*");
j_pointOnSurfaceNodeProc;

import maya.cmds as mc
#��ȡ��������ĵ�����
lx_cption = mc.xform(mc.ls(sl=1)[0],q=1,ws=1,t=1);


import maya.cmds as mc
#ѡ����Ƥ���ߣ����ɹ�������������scik
lx_eyeLidPtion = mc.filterExpand (sm=31);
mc.select (cl=True );
for lx_i in lx_eyeLidPtion :
    lx_endPtion = mc.xform (lx_i,q=True ,ws=True ,t=True );
    lx_sj = mc.joint (p=(lx_cption[0],lx_cption[1],lx_cption[2]));
    lx_ee = mc.joint (p=(lx_endPtion [0],lx_endPtion [1],lx_endPtion [2],));
    mc.ikHandle (sj =lx_sj,ee = lx_ee ,sol ="ikSCsolver" );
    mc.select (cl=1);
    

import maya.cmds as mc
lx_curve = mc.ls(sl=1);

import maya.cmds as mc
lx_jnt = mc.ls(sl=1);
lx_node=[];
for lx_temp in lx_jnt :
    nd=mc.pointOnCurve (lx_curve,ch=True );
    lx_node.insert(1,nd);
    mc.rename(nd,"cueNd_"+lx_temp);
    mc.group(empty=1,n=("nl_"+lx_temp));
    mc.connectAttr(("cueNd_"+lx_temp +".position"),("nl_"+lx_temp+".translate"));
    mc.toggle (("nl_"+lx_temp),localAxis=1);
    
    
    
    
import maya.cmds as mc
infoNd = mc.ls(sl=1)
mc.select(cl=1)
for i in infoNd:
    mc.print(i)
    grp = mc.group(em =1)
    mc.connectAttr((i+".position"),(grp+".translate"))
    mc.select(cl=1)