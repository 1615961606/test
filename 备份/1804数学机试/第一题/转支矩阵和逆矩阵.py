#coding=utf8
import numpy as np

a = np.array([[3,1,-1,2],
             [-5,1,3,-4],
             [2,0,1,-1],
             [1,-5,3,-3]])


b = np.array([[-2,-1,1,-2],
             [5,0,-3,4],
             [-2,0,0,1],
             [-1,5,-3,4]])
A = np.mat(a)
B = np.mat(b)   #转化为矩阵

print(A)
print(B)
#第二第三小题
print(A.T)      #A 矩阵的转置矩阵：
print(A.T.I)
print(A.I)      #A 矩阵的逆矩阵：

print(B.T)      #B 矩阵的转置矩阵：
print(B.T.I)
print(B.I)   #B 矩阵的逆矩阵：

print('===')
#第四小题
C1 = A+B
C2 = A*B
C3 = B*A

print(C1,C2,C3)