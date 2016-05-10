#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Jiangjishi
  E-mail:  Jiangjishi@foxmail.com
  Created: 2016/1/12 19:09:04
  Description:
  make heartCurve
  Instruction:
  
"""
import math
import maya.cmds as mc

#----------------------------------------------------------------------
def linstep(a,b,n=100):
    """make a curve like heartshape"""
    if n<2:
        return b
    diff=(float(b)-a)/(n-1)
    return [diff*i +a for i in range(n)]

#curve -d 3 -p -7.556184 0 -2.020119 -p -6.179765 0 3.068264 -p -0.846963 0 7.117587 -p 3.072986 0 7.537806 -p 6.041029 0 2.233047 -p 2.57181 0 -7.51884 -p -5.045095 0 -10.248057

t = linstep(-math.pi,math.pi,100)
#cuvCmd = 'mc.curve(d=2, p=[])';
posStr = "";
for i in t:
    x = 16 *math.sin(i) *math.sin(i)*math.sin(i);
    y = 0;
    z = 13 * math.cos(i) - 5 * math.cos(2*i) - 2*math.cos( 3 * i ) - math.cos( 4 * i );
    posStr += ' (%f,%f,%f),'%(x,y,z)
    
    
cuvCmd = 'mc.curve(d=2, p=[%s])'%posStr;        
eval(cuvCmd)
