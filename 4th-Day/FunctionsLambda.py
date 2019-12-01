import functools

# FUNCTION LAMDA

# Exercise 1 ___________________________________________
o=lambda x=1, y=2 , z=3: x+y+z
print(o())
print(o(10))
print(o(10,20))
print()

    # THE OUTPUT IS : 6 15 33


# Exercise 2 ___________________________________________

list=[2,4,6]
def function(list):
    multiply=1
    for index in list:
        multiply *= index
        print( multiply)


function(list)
print()

# Exercise 3 ___________________________________________



def funcrion(A , B):
    print((lambda a,b : a*b )(A,B))


funcrion(5,5)
print()


# Exercise 4 ___________________________________________



filt = list(filter(lambda num : num < 0 , range(-5,5)))

print(filt)
print()



# Exercise 5 ___________________________________________

x=lambda a,b,c: a+b+c
print (x(5,6,2))
print()

    #THE OUTPUT IS : 13


# Exercise 6 ___________________________________________

x=("Joey","Monica","Ross")
y=("Chandler","Pheobe")
z=("David","Rachel","Courtney")
result=list(zip(x,y,z))
print(result)
print()

    #THE OUTPUT IS : [('Joey', 'Chandler', 'David'), ('Monica', 'Pheobe', 'Rachel')]



# Exercise 7 ___________________________________________

coin=("Bitcoin","Ether","Ripple","Litecoin")
code=("BTC","ETH","XRP","LTC")
d=dict(zip(coin,code))
print(d)
print()

    # THE OUTPUT IS : {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}





# Exercise 8 ___________________________________________


#function that filters vowels

def fun(variable):
    letters = ['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False


sequence =['g','j','e','j','k','o','p','r']

filtered = list(filter(fun, sequence))
print(filtered)
print()

    #THE OUTPUT IS : ['e','o']




# Exercise 9 ___________________________________________

x = list(map(int,input('Enter a multiple value:').split()))
print("List of students:",x)

    #THE OUTPUT IS : List of students: [1, 20, 10]



# Exercise 10___________________________________________


def newfunc(a):
    return a*a
x= list(map(newfunc,(1,2,3,4)))
print(x)
print()
    # THE OUTPUT IS : [1, 4, 9, 16]




# Exercise 11 ___________________________________________

def func(a,b):
    return a+b
a=list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)
print()


    # THE OUTPUT IS : [3, 6, 8]




# Exercise 12 ___________________________________________


c=map(lambda x:x+x,filter(lambda x:(x>=3),(1,2,3,4)))
print(list(c))
print()

    # THE OUTPUT IS : [6, 8]




# Exercise 13 ___________________________________________

c=filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))

print(list(c))
print()

    #THE OUTPUT IS : [4, 6, 8]

# Exercise 14 ___________________________________________


list =[1,2,5,8,6,7]

def function (list):
    newList=functools.reduce(lambda a,b : a if a < b else b , list)
    
    print(newList)

function(list)
print()


# Exercise 15 ___________________________________________

numbers = [ 1,2,3]
letters = ['a','b','c']
def function( numbers , letters):
    result = list(zip(numbers,letters))
    print(result)

function(numbers,letters)
print()

