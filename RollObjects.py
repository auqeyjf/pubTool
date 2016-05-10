from pymel.core import *

def getLowestVtx(obj):
    vtx = [(v.currentItemIndex(), v.getPosition('world')) for v in obj.vtx]
    vtx.sort(key=lambda a:a[1][1])
    return vtx[0]

frange=map(int, (playbackOptions(q=1, min=1), playbackOptions(q=1, max=1)))
for obj in ls(sl=1):
    track_data = getLowestVtx(obj)
    for f in range(frange[0], frange[1]+1):
        currentTime(f)
        vtx_data = getLowestVtx(obj)
        x,y,z = 0, 0, 0
        if vtx_data[0] == track_data[0]:
            offset = track_data[1] - vtx_data[1] 
        else:
            offset = track_data[1] - obj.vtx[track_data[0]].getPosition('world')
            track_data = (vtx_data[0], vtx_data[1]+offset)
        x, z = offset[0], offset[2]
        y = vtx_data[1][1]*-1
        
        move(obj, (x, y, z), r=1, ws=1)
        obj.t.setKey()