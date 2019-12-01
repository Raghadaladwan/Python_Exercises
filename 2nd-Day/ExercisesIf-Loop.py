#Exercise 1

firstNum=input('Enter First Number ')
secondNum=input('Enter Second Number ')

if firstNum > secondNum:
    print(firstNum ,' is the greatest')
else : 
    print(secondNum ,' is the greatest' )    




#Exercise 2
    
Number=int(input('Enter any Number '))
for num in range(11):
    print(Number , "x",  num  ,"=" , (Number*num), '\n')
    
    
    
    
#Exercise 3

star = "*"
x=1
while x <=4 :
   print(star * x)
   x +=1  
   
while x >= 1:
    print(star * x)
    x -=1
    
  
    

#Exercise 4
    
    letters =['x','y','z','a','b','c']
for i in letters:
    if i =='a':
        continue
    elif i =='c':
        break
    print(i)
    
    
    #THE OUTPUT 
        
        x
        y
        z
        b
        
    
    
#Exercise 5
        
for x in range (12,25,3):
    print(x)
    
       #THE OUTPUT  
        
        12
        15
        18
        21
        24
    

    
#Exercise 6
        
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
    
     #THE OUTPUT
        1
        2
        3
     
        
        
        
#Exercise 7
        
one= int(input('enter a number '))
sum=0
for a in range(1,one+1):
    sum+=a
print(sum)  




#Exercise 8

Number= int(input('enter a number '))
if Number % 2 == 0:
    print('Number', Number , 'is Even')
else: 
    print('Number', Number , ' is Odd')
        
        
#Exercise 9  
    
    
    
for i in range(5):
    print((5-i)*' ' +(2*i+1)* '*')
for i in range(5-1,-1,-1):
    print((5-i)* ' ' +(2*i+1)* '*')
    
    
    
#Exercise 10
    
    
while True:
    try:
        n=int(input('Enter integer number'))
        break
    except ValueError:
        print('Pleass try again ')    


print("ENTERD VALUE",n)  


#Exercise 11

try :
    a=3
    if a<4:
        b=a/(a-3)
    print("Value of b= " ,b)
except(ZeroDivisionError,NameError):
    print("\nError Occurred and Handled")
      
    # THE OUTPUT IS 
        Error Occurred and Handled
        
        
        
        
        
        
        
        
        
        
        