import maya.cmds as cmds
from os import popen


			
def lx_DuplicateFace():
	j_bsName=('MadBrow','SadBrow','WorryBrow','EyeBrowUpMid','EyeBrowDownMid','EyeBrowUpTip','EyeBrowDownTip','EyeBrowNarrowTip','EyeBrowUpEnd','EyeBrowDownEnd','FenGeFu','EyeLidUpMad',
			'EyeLidUpSad','EyeLidDownMad','EyeLidDownSad','EyeLidUpSemi','EyeLidUpDown','EyeLidUpUp','EyeLidDownUp','EyeLidDownDown','FenGeFu','NoseSneer','NosePuff','NoseSuck','FenGeFu',
			'MouthSmile','MouthFrown','MouthNarrow','MouthWide','MouthCornerUp','MouthCornerDown','LipUpRollIn','LipUpRollOut','LipDownRollIn','LipDownRollOut','LipUpUp',
			'LipUpDown','LipDownUp','LipDownDown','LipUpSneerUp','LipUpSneerDown','LipDownSneerUp','LipDownSneerDown','CheekIn','CheekOut','Squint','MMouthPucker','MMouthAngry')
	j_Head = cmds.ls(selection =1)[0];
	
	j_startPosX = 5;
	j_startPosY = 5;
	
	cmds.group(name='Grp_Targets',em=1);	
	j_baseGeo = cmds.duplicate(j_Head,name=j_Head+'baseGeo')[0];
	cmds.setAttr((j_baseGeo + ".tx"),lock = 0,);
	cmds.setAttr((j_baseGeo + ".ty"),lock = 0,);
	cmds.setAttr((j_baseGeo + ".tz"),lock = 0,);
	cmds.setAttr((j_baseGeo + ".rx"),lock = 0,);
	cmds.setAttr((j_baseGeo + ".ry"),lock = 0,);
	cmds.setAttr((j_baseGeo + ".rz"),lock = 0,);
	cmds.setAttr((j_baseGeo + ".sx"),lock = 0,);
	cmds.setAttr((j_baseGeo + ".sy"),lock = 0,);
	cmds.setAttr((j_baseGeo + ".sz"),lock = 0,);
	j_baseGeoShape = cmds.listRelatives(j_baseGeo,s=1,);
	if(len(j_baseGeoShape)>1):
	    cmds.delete(j_baseGeoShape[1:]);
	cmds.xform((j_Head+'baseGeo'),ws =1,t=(0,15,0))
	for bsMesh in j_bsName:
		if(bsMesh=='FenGeFu'):
			j_startPosX = 5;
			j_startPosY = j_startPosY +5;
		else:
			if(bsMesh=='MMouthPucker'or bsMesh=='MMouthAngry'):
				cmds.duplicate(j_baseGeo,name=bsMesh);
				cmds.xform(bsMesh,ws= 1, t =(j_startPosX,j_startPosY,5))
				j_startPosX = j_startPosX + 4;
				j_selShape = cmds.listRelatives(bsMesh,s=1,)[0];
				cmds.rename(j_selShape,(bsMesh+'Shape01'));
				cmds.parent(bsMesh,'Grp_Targets')
			else:
				#cmds.textCurve(ch
				cmds.duplicate(j_baseGeo,name="L"+bsMesh);
				cmds.parent('L'+bsMesh,'Grp_Targets')
				cmds.xform("L"+bsMesh,ws= 1, t =(j_startPosX,j_startPosY,5))
				j_selShape = cmds.listRelatives("L"+bsMesh,s=1,)[0];
				cmds.rename(j_selShape,("L"+bsMesh+'Shape01'));
				j_startPosX = j_startPosX + 4;
				cmds.duplicate(j_baseGeo,name="R"+bsMesh);
				cmds.parent('R'+bsMesh,'Grp_Targets')
				cmds.xform("R"+bsMesh,ws= 1, t =(j_startPosX,j_startPosY,5))
				j_selShape = cmds.listRelatives("R"+bsMesh,s=1,)[0];
				cmds.rename(j_selShape,("R"+bsMesh+'Shape01'));
				j_startPosX = j_startPosX + 6;
			
				if j_startPosX >=50:
					j_startPosX = 5;
					j_startPosY =j_startPosY + 5;
