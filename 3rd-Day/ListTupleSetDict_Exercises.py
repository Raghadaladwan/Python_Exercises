# Exercise 1 ___________________________________________


list=[1,2,3,4,5]
for item in list:
    print(item)




# Exercise 2 ____________________________________________


list=[2,4,6,8]
sum=0
for item in list:
    sum+=item
print("The sum of item is : ",sum)




# Exercise 3 ____________________________________________


list=[10,100,20,9,1000]

max_number= max(list)

print("The Maximum Number is :  " ,max_number)




# Exercise 4 _____________________________________________


# USE {} Tuples
a = {10,20,30,20,10,50,60,40,80,50,40}

print(a)




# Exercise 5 ______________________________________________


list=[]

if len(list) == 0 :
    print("List is Empty")
else :
    print(len(list))


# Exercise 6 _______________________________________________


tuple = ('tuple', True , 9.2 , 1)

for item in tuple:
    print(item)




# Exercise 7 _______________________________________________


num_set = set([0, 1, 2, 3, 4, 5])

for item in num_set:
    print("Item",item)



# Exercise 8 _______________________________________________


setOne = {5,6,9,2,4,6}
setTwo = {5,6,9,4,5,23,75}

print("Intersection : ", setOne.intersection(setTwo))



# Exercise 9 ________________________________________________


setx = set(["green","blue"])
sety = set(["blue","yellow"])
seta = setx | sety

print("seta : ",seta)


    # THE OUTPUT IS :
          seta :  {'blue', 'green', 'yellow'}



# Exercise 10 _________________________________________________


seta = set([5,10,3,15,2,20])
print(len(seta))

    # THE OUTPUT IS : 6



# Exercise 11 _________________________________________________


dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)


    # THE OUTPUT IS :
     {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}




# Exercise 12 ________________________________________________


a="Hello,World!"
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.lower())
print(a.replace("H","J"))

    #THE OUTPUT IS :
        e
        llo
        orl
        12
        hello,world!
        Jello,World!





