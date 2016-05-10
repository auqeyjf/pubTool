import time, tempfile, os

author = 'changlong.zang'
mail = 'zclongpop@163.com'
timeStr = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
information = '#{0}\r\n# author: {1}\r\n#   mail: {2}\r\n#   date: {3}\r\n#{0}'.format('='*45,author, mail, timeStr)

tempPath = tempfile.mktemp('.txt')

f = open(tempPath, 'w')
f.write(information)
f.close()


os.system('explorer.exe %s'%tempPath)