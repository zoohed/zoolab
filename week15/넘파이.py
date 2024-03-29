#행렬 구하기 (넘파이랑 리스트 비교해서 넘파이가 편하다는 걸 알아야해 !)

import numpy as np
a=np.array([[2, 5, 10], [12, 20, 15], [3, 12, 15]])
a
#array([[ 2,  5, 10],
#       [12, 20, 15],
#       [ 3, 12, 15]])


b=np.array([[10, 11, 12], [21, 22, 25], [11, 22, 33]])
b
#array([[10, 11, 12],
#       [21, 22, 25],
#       [11, 22, 33]])


a.T #전치행렬
#array([[ 2, 12,  3],
#       [ 5, 20, 12],
#      [10, 15, 15]])


np.linalg.inv(a) #역행렬
#array([[ 2.96296296e-01,  1.11111111e-01, -3.08641975e-01],
#       [-3.33333333e-01, -3.96508223e-18,  2.22222222e-01],
#       [ 2.07407407e-01, -2.22222222e-02, -4.93827160e-02]])


a+b #두 행렬을 합해줌
#array([[12, 16, 22],
#       [33, 42, 40],
#       [14, 34, 48]])


a
#array([[ 2,  5, 10],
#       [12, 20, 15],
#       [ 3, 12, 15]])


np.mean(a) #평균
#10.444444444444445


np.std(a) #표준편차
#5.717635702341603


np.var(a) #분산
#32.691358024691354


np.median(a) #중앙값
#12.0


np.mean(a, axis=0) #열 평균
#array([ 5.66666667, 12.33333333, 13.33333333])

#2215848 박주희 numpy패키지로 프로그램 작성 -> 속도가 빠르당 ~

import numpy as np #numpy 모듈을 가지고 와서 np라는 별명을 붙임

a=[2, 50, 14, 3, 10]
b=[15, 20, 30, 11, 13]
print(a+b) #리스트끼리 결합

a1=np.array(a) #백터 ? 그냥 계산하면 됨 for문보다 속도가 훨 ~ 빠름
b1=np.array(b)
print(a1+b1) #원소 원소가 합쳐짐

print(a1*b1) #원소 원소가 곱해짐