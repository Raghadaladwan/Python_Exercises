#Exercise 1 _____________________________________________ 
import numpy as np
e= np.zeros(10)
print(e)

g= np.ones(10)
print(g)

f=np.ones(10)*5
print(f) 

#Exercise 2 _____________________________________________ 

a = np.arange(30,71)
print(a)


#Exercise 3 _____________________________________________ 
a = np.arange(30,71,2)
print(a)

#Exercise 4 _____________________________________________ 
c = np.arange(4).reshape(2,2)
print(c)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#Exercise 5 _____________________________________________ 
number  = np.random.random()
print(number)
#Exercise 6 _____________________________________________ 
ee=np.arange(12).reshape(3,4)
for i in range(len(ee)): 
    print(ee[i]) 

#Exercise 7 _____________________________________________
numbers =np.arange(0,21)
numbers[9:16] *= -1
print(numbers) 

#Exercise 8 _____________________________________________ 
x=[1,8,3,5]
y=np.random.randint(0,11,4)
print(x)
print(y)
z=x.append(y)
print(z)
#Exercise 9 _____________________________________________ 
m= np.arange(10,22).reshape((3, 4))
print(m)
print(m.shape)

#Exercise 10 _____________________________________________ 
x = np.random.random((3, 3, 3))
print(x)
#Exercise 11 _____________________________________________ 
a=np.array([9,-1,2,5])
b=np.array([1,-6,0,10])
c=np.array([[1,8,2,5],[3,1,7,9]])

print("a-b: ",a-b)
print("a*b: ",a*b) 
print("a.dot(b): ",a.dot(b)) 
print("a*2: ",a*2) 
print("np.sin(a): ",np.sin(a)) 
print("a<3: ",a<3) 
print("a.sum(): ",a.sum()) 
print("a.sum(axis=0): ",a.sum(axis=0)) 
print("c.sum(): ",c.sum()) 
print("c.sum(axis=0): ",c.sum(axis=0)) 
print("a.min(): ",a.min()) 
print("a.max(): ",a.max()) 
print("a.mean(): ",a.mean()) 
print("a average(): ",np.average(a)) 
print("a median(): ",np.median(a)) 
print("a std(): ",np.std(a)) 
print("a var(): ",np.var(a)) 
print("c.cumsum(): ",c.cumsum()) 
print("a[1:2] :  ",a[1:2]) 
print("a[2:] :  ",a[2:]) 
print("c[-1] :  ",c[-1])

"""
a-b:  [ 8  5  2 -5]
a*b:  [ 9  6  0 50]
a.dot(b):  65
a*2:  [18 -2  4 10]
np.sin(a):  [ 0.41211849 -0.84147098  0.90929743 -0.95892427]
a<3:  [False  True  True False]
a.sum():  15
a.sum(axis=0):  15
c.sum():  36
c.sum(axis=0):  [ 4  9  9 14]
a.min():  -1
a.max():  9
a.mean():  3.75
a average():  3.75
a median():  3.5
a std():  3.6996621467371855
a var():  13.6875
c.cumsum():  [ 1  9 11 16 19 20 27 36]
a[1:2] :   [-1]
a[2:] :   [2 5]
c[-1] :   [3 1 7 9]
"""
#Exercise 12 _____________________________________________ 
import matplotlib.pyplot as plt
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50)) 
print("Values of Y (thrice of X):")
print(Y)
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
plt.show()

#Exercise 13 _____________________________________________ 
import matplotlib.pyplot as plt
x1 = [10,20,30]
y1 = [20,40,10]
plt.plot(x1, y1, label = "line 1")
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
plt.legend()
plt.show()
#Exercise 14 _____________________________________________ 
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
#Exercise 15 _____________________________________________ 
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()



