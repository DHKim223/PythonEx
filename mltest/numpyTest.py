# Numpy
import numpy as np

t = ( 10 , 20, 30, 40, 50 )
#print( t[1] )
tt = np.array(t)
#print(type(tt))
#print(tt[1])

s = { 10, 20, 30, 40, 50 }
print(type(s))
ss = np.array(s)
print(type(ss))

m = [10, 20, 30, 40, 50]
print(type(m))
mm = np.array(m)
print(type(mm))

for m in mm :
    print(m, end = "\t")
print()

print(np.shape(mm))     # (5, ) 1차원 / (5, 1) 2차원

w = [-5, 0, 3 ,7, -3, 1, 4, 2, -1,  -8]
print(np.shape(w))
print(np.abs(w))
print(np.sqrt(np.abs(w)))
print(np.square(w))
print(np.sqrt(np.square(w)))
print( np.isnan(w))
print( np.sum(w))
print( np.mean(w))
print( np.max(w))
print( np.min(w))
print( np.sort(w))
print(np.sort(w)[::-1])
print(np.std(w))    # 표준편차

m = [[1,2,3],[4,5,6]]
print(type(m))
mm = np.array(m)
print(type(mm))
print(np.shape(mm))

print( mm )
print(mm.reshape( 3, 2 ))

print(np.sum(mm))
print(np.sum(mm, axis = 0))     # 열의 합계
print(np.sum(mm, axis = 1))     # 행의 합계
print( np.mean(mm))
print( np.mean(mm, axis = 0))   #열
print( np.mean(mm, axis = 1))   #행
        
print(np.std(mm))           # sqrt of variance 제곱근
print(np.var(mm))           # 거리의 제곱의 평균 mena of dist squared

m = [[1,2,3],[4,5,6]]
w = [[10,20,30],[40,50,60]]
print(np.add(m,w))
print(np.subtract(w,m))
print(np.multiply(m,w))
print(np.divide(m,w))

print( m * 2)
#print( m ** 2)

#w = w.reshape(3,2)
#print(m.dot(w))     # (2,3) . (3,2)

print(np.zeros(5))
print(np.zeros((3,4)))
print(np.ones((2,3)))

x = np.random.randn(10)
print(x)
y = np.random.randn(10)
print(y)
print(np.maximum(x,y)) # x, y 비교해서 큰 숫자 출력
print(np.minimum(x,y))

z = np.random.randn(5,5)
print(z)
print(np.sum(z))

a = [ i for i in range(10,20)]  #list
print(a)
print(a[0:5])
print(a[:])
print(a[:-1])
print(a[5:8])

b = np.arange(10,20)    #Array
print(b)

a = [[1,2,3,4],[5,6,7,8]]
print(a)
print(a[1][1])
print(a[:][:])
print(a[1][:])
print("###############")
print(a[0:2][0:2])

b = np.array(np.arange(1,16)).reshape(3,5)
print(b)
print(b[2][2])
print(b[1][:])
print(b[1][0:2])
print(b[0:2,0:2])

