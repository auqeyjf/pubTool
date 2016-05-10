import maya.cmds as mc
#选择lip基础面，生成口型mesh_KouXingBase 外加 众口型目标体，自动做bs,表情节点名称为：bs_MouthKouXing.基础表情名称：bs_MouthKouXingBase
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

# ########################### 华丽丽的分隔线 ##################################################

import maya.cmds as mc
#根据骨骼点的数量在mesh上生成相应数量pointOnSurface node

# 在生成的同时，生成对应数量的空组，并显示局部坐标
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
# 合并上一步生成的空组和之前生成的次级骨骼的组。
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
#获取眼球的中心点坐标
lx_cption = mc.xform(mc.ls(sl=1)[0],q=1,ws=1,t=1);


import maya.cmds as mc
#选择眼皮的线，生成骨骼链。并加上scik
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