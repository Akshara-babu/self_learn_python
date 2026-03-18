"""
8. Find Largest of Two Numbers

Store two numbers in variables and find the largest.
"""
num1 =40

num2 =80

# print("num1 is largest",num1>num2)
# print("num2 is largest",num2>num1)

#____________________________________________

if num1>num2:

    print("num1 is largest",num1)

else:

    print(num2,"num2 is largest")

#____________________________________________


num1=int(input("enter num1:"))

num2=int(input("enter num2:"))

largest= num1 if  num1>num2  else num2

print("largest num", largest)

