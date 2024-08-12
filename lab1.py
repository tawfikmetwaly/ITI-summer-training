#task1
#write 3 variable and check for it's data types using type() function
var1, var2, var3 = 10, 'hi', 3.14
print(type(var1), type(var2), type(var3))

#----

#task2
#write 3 variable and take it in one line using split() function and print it

var1, var2, var3 = input("Enter 3 variable: ").split()
print(var1, var2, var3)

#----

#task3
#write program take number from user then convert it to string " casting " then print lenth of this string using len() function

num = int(input("Enter a number: "))
num = str(num)
print(len(num))

#----

#task4
#you have number and you want to remove last k number from this number implement python program do that and print result

number, k =  map(int,input("Enter Your number and k number: ").split())
print(number // 10**k)

#----

#task5
#take integer multiple number in one line then print maximum and minimum number from it 
num1, num2, num3, num4 = map(int,input("Enter 4 numbers: ").split())
print("max number is" , max(num1, num2, num3,num4))
print("min number is" , min(num1, num2, num3,num4))

#----

#task6
# Write a Python program that finds the minimum of two values a and b
num1, num2 = map(int,input("Enter 2 numbers: ").split())
if num1 > num2: print(num2)
else: print(num1)

#----

#task7
#Write a program that reads an integer salary then:
#- if salary < 1000, print "you are poor"   
#- if salary < 20000, print "good salary"
#- if salary > 20000, print "you are rich"

salary = int(input("Enter your salary: "))
if salary < 1000:
    print('you are poor')
elif salary < 20000:
    print('good salary')
elif salary > 20000: print('you are rich')

#----

#task8
#Write a Python program that receives the age and display whether he can drive a car. 
#If the user is above 18 years old, he can drive.

age = int(input("Enter your age: "))
if age > 18:
    print('you can drive')
else : print('you can not drive')