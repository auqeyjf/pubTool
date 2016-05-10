#=================================
# author: changlong.zang
#   date: 2014-04-14
#=================================
import re
import maya.cmds as mc
import maya.mel  as mel
import nameTool
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

def undo_decorator(func):
    '''
    to fix maya can't undo bug..
    '''
    def doIt(*args, **kvargs):
        mc.undoInfo(openChunk=True)
        func(*args, **kvargs)
        mc.undoInfo(closeChunk=True)
    return doIt


#==============================================
#                    Shapes                   #
#==============================================

def parentShape(*args):
    '''
    parent shapes to last one..
    '''
    if len(args) < 2:
        return
    shapes = mc.listRelatives(args[:-1], s=True, path=True)
    mc.parent(shapes, args[-1], s=True, r=True)
    mc.delete(args[:-1])



def conformShapeNames(transform):
    '''
    pSphere1 -> pSphere1Shape, pSphere1Shape1, pSphere1Shape2..
    '''
    shapes = mc.listRelatives(transform, s=True, path=True) or []
    for shape in shapes:
        mc.rename(shape, '%sShape'%transform)



#==============================================
#                    History                  #
#==============================================


def getHistoryByType(geometry, historyType):
    '''
    return object history by type..
    '''
    historys = mc.listHistory(geometry, pdo=True)
    typedHistory = mc.ls(historys, type=historyType)
    typedHistory = {}.fromkeys(typedHistory).keys()    
    
    return typedHistory




def findDeformer(geometry):
    '''
    return object's deformers..
    '''
    deformers = mel.eval('findRelatedDeformer("%s")'%geometry)
    return deformers




def findSkinCluster(geometry):
    '''
    return object's skinCluster node..
    '''
    skinCluster = mel.eval('findRelatedSkinCluster("%s")'%geometry)
    return skinCluster


#==============================================
#                  blendShape                 #
#==============================================

def getBlendShapeInfo(blendShape):
    '''
    return blendShape's ID and attributes dict..
    '''
    attribute_dict = {}
    if mc.nodeType(blendShape) != 'blendShape':
        return attribute_dict
    
    infomations =  mc.aliasAttr(blendShape, q=True)
    for i in range(len(infomations)):
        if i % 2 == 1:continue
        bs_id   = infomations[i + 1]
        bs_attr = infomations[i + 0]
        bs_id = int(re.search('\d+', bs_id).group())
        attribute_dict[bs_id] = bs_attr

    return attribute_dict




def getBlendShapeAttributes(blendShape):
    '''
    return blendShape attributes..
    '''
    attribute_dict = getBlendShapeInfo(blendShape)
    bs_idList = attribute_dict.keys()
    bs_idList.sort()
    
    attributes = [attribute_dict.get(i,'')  for i in bs_idList]
    return attributes





def getBlendShapeInputGeomTarget(blendShape):
    igt_dict = {}

    attributes = ' '.join(mc.listAttr(blendShape, m=True))
    for old, new in (('inputTargetGroup', 'itg'),
                      ('inputTargetItem',  'iti'),
                      ('inputGeomTarget',  'igt'),
                      ('inputTarget',       'it')):
        attributes = attributes.replace(old, new)
        
    igt_atrributes = re.findall('it\[0\]\.itg\[\d+\]\.iti\[\d{4,}\]\.igt', attributes)    
    for attr in igt_atrributes:
        index = re.search('(?<=itg)\[\d+\]', attr).group()
        igt_dict[int(index[1:-1])] = attr

    return igt_dict





def getActiveTargets(blendShape):
    '''
    get opend blendShape's ids..
    '''
    targents = []
    for weightid, attr in getBlendShapeInfo(blendShape).iteritems():
        if mc.getAttr('%s.%s'%(blendShape, attr)) == 1:
            targents.append(weightid)
    return targents





def getSetsMembers(Sets):
    '''
    get all of sets children..
    '''
    args = []
    
    members = mc.sets(Sets, q=True)
    if mc.sets(members, q=True):
        args.extend(members)
        args.extend(getSetsMembers(members))
    else:
        args.extend(members)

    return args



#==============================================
#                  General                    #
#==============================================


def getChildren(Joint):
    '''give a root joint name, find all children joints to return'''
    L = [Joint]
    for J in mc.listRelatives(Joint, c=True, type='transform', path=True) or []:
        L.append(J)
        
        ccd = mc.listRelatives(J, c=True, type='transform', path=True)
        if ccd:
            for j in ccd:
                L.extend(getChildren(j))
        else:
            pass
    return L


#==============================================
#                  Control                    #
#==============================================
def makeControl(side, nameSpace, count):
    types = ('ctl', 'cth', 'ctg', 'grp')
    control = []
    for t in types:
        controlName = nameTool.compileMayaObjectName('_'.join((side.upper(), nameSpace, t, str(count))))
        if len(control) == 0:
            control.append(mc.group(em=True, n=controlName))
        else:
            control.append(mc.group(control[-1], n=controlName))
    return control
            
            



#==============================================
#                  Other                      #
#==============================================
def attachToCurve(pathCus, attactOBJ, uValue, UpperOBJ=None, uValuezerotoone=True):
    CusShape = mc.listRelatives(pathCus, s=True, type='nurbsCurve')
    motionpathNode = mc.createNode('motionPath')
    
    # connect curve and motionpath node..
    mc.connectAttr(CusShape[0] + '.worldSpace[0]', motionpathNode + '.geometryPath')
    
    # connect motionpath node and object..
    for outAttr, inAttr in (('.rotateOrder', '.rotateOrder'),('.rotate', '.rotate'),('.allCoordinates', '.translate')):
        mc.connectAttr(motionpathNode + outAttr, attactOBJ + inAttr)        

    # set Uvalue..
    mc.setAttr(motionpathNode + '.uValue', uValue)
    
    # set offset..
    if uValuezerotoone:
        mc.setAttr(motionpathNode + '.fractionMode', 1)

    
    if not UpperOBJ:
        return motionpathNode
    # set upvector..
    mc.setAttr(motionpathNode + '.worldUpType', 1)
    mc.connectAttr(UpperOBJ + '.worldMatrix[0]', motionpathNode + '.worldUpMatrix')
    mc.setAttr(motionpathNode + '.frontAxis', 0)
    mc.setAttr(motionpathNode + '.upAxis', 2)
    return motionpathNode