# Q1)Write a Python program to do arithmetical operations addition and division. 

num1 = float(input('enter the first number for edition'))
num2 = float(input('enter the second number for edition'))
sum = float(num1+num2)
print('sum',sum)
division = float(num1/num2)
print('division',division)
power = int(num1**num2)
print('power ',power)
floor_divident = int(num1%num2)
print('floor_division',floor_divident)
# Q2)Write a Python program to find the area of a triangle.
length = float(input('enter the length of a triangle'))
height = float(input('enter the height of a triangle'))
area = float(length*height/2)
print('the area of triangle is',area)
# Q3)Write a Python program to convert Celsius to Fahrenheit.
celsius = float(37)
fehranhite  = float((celsius*(9/5))+32)
print('37 degree fehranhite is equal to 98.6 degree farenheite',fehranhite)
# Q4)Write a Python program that return all datatypes that we discussed in the class.
print('the data type of 19 is:',type(19))
print('the data type of 16.5 is:',type(16.5))
print('the data type of muhammad arqum is:',type('muhammad arqum'))
print('the data type of true is:',type(True))
print('the data type of true is:',type([1,2,3]))
print('the data type of true is:',type((1,2,3)))
print('the data type of true is:',type({1,2,3}))