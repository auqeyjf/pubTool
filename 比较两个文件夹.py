'''
�Ƚ������ļ�������ļ�������в�ͬ���ļ��������������������ļ���
'''
import sys, os,shutil
from os.path import walk,join,normpath

PathA = 'D:\\BaiduYunDownload\\�йȽ���Python\\'
PathB = 'D:\\BaiduYunDownload\\Python\\�й�\\�йȽ���Python\\'
PathC= 'D:\\�й�Goal\\'

def visit(arg,dirname,names):
    print  dirname
    dir = dirname.replace(PathA,"")
    dirnameB = os.path.join(PathB,dir)
    dirnameC = os.path.join(PathC,dir)
    
    if os.path.isdir(dirnameB):
        for file in names:
            if os.path.isfile(os.path.join(dirname,file)) and not os.path.isfile(os.path.join(dirnameB,file)):
                if not os.path.isdir(dirnameC):
                    os.system("mkdir %s"%(dirnameC))
                shutil.copy2(os.path.join(dirname,file),os.path.join(dirnameC,file))
            elif os.path.isdir(os.path.join(dirname,file)) and not os.path.isdir(os.path.join(dirnamB,file)):
                if not os.path.isdir(os.path.join(dirnameC,file)):
                    os.system("mkdir %s"%(os.path.join(dirnameC,file)))
    else:
        if not os.path.isdir(dirnameC):
            os.system("mkdir %s"%(dirnameC))
        for file in names:
            shutil.copy2(os.path.join(dirname,file),os.path.join(dirnameC,file))