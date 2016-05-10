__author__ = 'Administrator'
'''
L1=[1,2]
L2=['a','b','c']
print [[str(i)+j for j in L2] for i in L1]
'''
'''
a = 8
int(a)
print [[str(i)+str(j) for j in range(8)] for i in  range(8)]
'''


# print [[[ (str(i)+str(j)+str(k)) for j in range(8)] for k in  range(8)] for i in range(8)]

print ((( (str(i)+str(j)+str(k)) for j in range(8)) for k in  range(8)) for i in range(8))
