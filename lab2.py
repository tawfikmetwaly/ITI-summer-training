##task1
#We need to print 0,3,6,9,12 using for loop

list= [i for i in range(0,12,3)]
print(list)

#----

#task2
#We need to print 0 ,3 ,6 ,9 ,12 and index of positions using for loop -> hint: enumerate function 

for i, value in  enumerate(range(0,12,3)):
    print(i, value)

#----

#task3
#write a program to turn every item of a list into its square
lst = [1, 2, 3, 4, 5, 6, 7]
print([i**2 for i in lst])

#----

#task4
# Calculate the sum of all numbers from 1 to an input number from user 

num = int(input("Enter a number: "))
sum =0
for i in range(1, num + 1):
    sum = sum + i
print(sum)

#----

#task5
#Count the total number of digits in a number 
	#note: don't use conversion or casting to str

num = int(input("Enter a number: "))
digits = 0

if num < 0: num = num * -1
if num == 0: digits = 1
while num > 0:
    num = int(num/10)
    digits = digits + 1

print(digits)

#----

#task6
#Write a program to use the loop to find the factorial of an input number from user
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("not exist")
elif num == 0:
    print(1)
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)

#----

#task7
#Write a program to use the loop to Reverse a given integer number

num = int(input("Enter a number: "))
rev_num = 0
while num > 0:
    rev_num = rev_num * 10 + num % 10
    num = int(num / 10)
print(rev_num)


    