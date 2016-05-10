#f = open('D:/22.json', 'w')
import maya.cmds as cmds
import json

verCount = cmds.polyEvaluate('pSphere1',vertex =1)
config = json.loads(open('D:/12.json').read())

i = 0
while i<verCount:
     vdd = 'pSphere2.vtx[' + str(i) + ']' 
     #cmds.skinPercent("skinCluster2",vdd)
     
     #print(vdd,i)
     influence = cmds.skinPercent('skinCluster2',vdd,query =True,v=True)  
     sums =len(influence)
     j = 0
     while j<sums:
          vv = 'skinCluster1.wl['+str(i)+'].w['+str(j)+']'
          vc = 'skinCluster2.wl['+str(i)+'].w['+str(j)+']'
          wt = cmds.setAttr(vc,config[vv])  
          
          
          j=j+1
		  
     i= i+1
     
     

     
     
     
import maya.cmds as cmds
import json
DT = {}
f = open('D:/22.json', 'w')
verCount = cmds.polyEvaluate('pSphere1',vertex =1)

i = 0
while i<verCount:
     vdd = 'pSphere1.vtx[' + str(i) + ']' 
     #cmds.skinPercent("skinCluster2",vdd)
     
     #print(vdd,i)
     influence = cmds.skinPercent('skinCluster1',vdd,query =True,v=True)  
     sums =len(influence)
     j = 0
     while j<sums:
          vv = 'skinCluster1.wl['+str(i)+'].w['+str(j)+']'
          wt = cmds.getAttr(vv)  
          #print(vv,wt)
          DT[vv] = wt
          j=j+1
          #json.dump(DT, f)
          
i= i+1
     
json.dump(DT, f)
f.close()