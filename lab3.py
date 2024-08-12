#task1
#Write a function to count the number of vowels in a given string.
def vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels: count += 1
    return count

str = input("string: ")
count = vowels(str)
print(count)

#----

#task2
#Write a function to capitalize the first letter of each word in a given sentence.

def captalize(string):
    return string.title()

str = input("string: ")
captalized_str = captalize(str)
print(captalized_str)

#----

#task3
#Create a Rectangle class with attributes "length" and "width" to calculate the area and perimeter.
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

width = int(input("width: "))
height = int(input("height: "))

print(rectangle(width, height).perimeter())

#----

#task4
# Write a Python function to sum all the numbers in a list using for loop not sum() function

def sum (list):
    sum = 0
    for i in list:sum += i
    return sum

list = [1, 2, 3, 4, 5]
print(sum(list))

#----

#task5
#Write a Python function that accepts a string and counts the number of upper and lower case letters.

def UandL(string):
    U_count = 0
    L_count = 0
    for char in string:
        if char.isupper(): U_count += 1
        elif char.islower(): L_count += 1
    return U_count, L_count

str = input("string: ")
upper_count, lower_count = UandL(str)
print(f"upper letters : {upper_count}")
print(f"lower letters : {lower_count}")

