#=================================
# author: changlong.zang
#   date: 2014-05-05
#=================================
import string, os, re
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
VERSION_PADDING = 3


def conformFilePath(path, MSC='maya'):
    '''
    E:/a\b/c\qq.ma -> E:/a/b/c/qq.ma 
    E:/a\b/c\qq.ma -> E:\a\b\c\qq.ma 
    '''
    if MSC == 'maya':
        newPath = path.replace('\\', '/')
    else:
        newPath = path.replace('/', '\\')
    return newPath




def getVersionsFiles(path):
    '''
    { '001': 'E:/ss_v001.ma',  '002': 'E:/ss_v002.ma',  '003': 'E:/ss_v003.ma' }
    '''
    fileDict = {}
    if not os.path.isdir(path):
        return fileDict
    
    for f in os.listdir(path):
        version = re.search('(?<=v)\d+$', os.path.splitext(f)[0])
        if not version:continue
        fileDict[version.group()] = conformFilePath(os.path.join(path, f))
    
    return fileDict




def getVersions(path):
    '''
    ['001', '002', '003', '004', ..., '999', '1000']
    '''
    versions = getVersionsFiles(path).keys()
    versions.sort()
    return versions





def getLastVersion(path):
    '''
    ['001', '002', '003', '004'] -> '004'
    '''
    versions = getVersions(path)
    versions.insert(0, 0)
    
    lastVersion = max([int(v) for v in versions])
    lastVersion = string.zfill(lastVersion, VERSION_PADDING)
    return lastVersion




def getNewVersion(path):
    '''
    ['001', '002', '003', '004'] -> '005'
    '''
    lastVersion = int(getLastVersion(path))
    newVersion = string.zfill(lastVersion+1, VERSION_PADDING)
    return newVersion




def getVersiondFile(path, version):
    '''
    001 -> E:/ss_v001.ma   002 -> E:/ss_v002.ma   003 -> E:/ss_v003.ma
    '''
    fileDict = getVersionsFiles(path)
    filePath = fileDict.get(version, '')
    return filePath




def getLastFile(path):
    '''
    { '001': 'E:/ss_v001.ma',  '002': 'E:/ss_v002.ma',  '003': 'E:/ss_v003.ma' } -> 'E:/ss_v003.ma'
    '''
    lastVersion = getLastVersion(path)
    lastFile    = getVersiondFile(path, lastVersion)
    return lastFile




def getNewFile(path, fname_format='name_v%s.txt'):
    '''
    Exp:
        name_%s.txt   -> name_v001.txt
        name_v001.txt -> name_v002.txt
        name_v00n.txt -> name_v00n+1.txt
    '''
    filePath = ''
    lastFile   = getLastFile(path)
    if not os.path.isfile(lastFile):
        filePath = conformFilePath(os.path.join(path, fname_format%string.zfill(1, VERSION_PADDING)))
  
    else:
        lastVersion = getLastVersion(path)
        newVersion  = getNewVersion(path)

        fname, fextension = os.path.splitext(lastFile)
        filePath = re.sub('%s$'%lastVersion, newVersion, fname) + fextension
    
    return filePath




def getSize(path):
    '''
    return a file or a dir size by bytes...
    '''
    size = 0
    if os.path.isfile(path):
        size = os.path.getsize(path)
    
    elif os.path.isdir(path):
        for p, d, fs in os.walk(path):
            for f in fs:
                size += os.path.getsize(os.path.join(p, f))
    return size