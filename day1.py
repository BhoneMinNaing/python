#Variables (String, Integer, Float, Boolean) is a container for a value.


#1. String
first_name = "Bhone Min"
last_name = "Naing"
print (f"Your name is: {first_name} {last_name}");

#2. Integer
age = 19
height = 179
print (f"You are {age} years old. Your height is: {height}");

#3. Float
GPA = 4.2
height_inch = 5.10
print(f"Your GPA is: {GPA} and you are {height_inch} tall");

#4. Boolean
Student = True;
Graduate = False;
if Student:
    print(f"You are a student!");
else:
    print(f"You are not a student!");

if Graduate:
    print(f"You are graduated");
else:
    print(f"You are not graduated");

#--------------------------------------------------------------

#Typecasting (str(), int(), float(), bool()) is the process of converting a variable from one data type to another data type

name = "Bhone Min Naing"
AGE = 19
score = 100
employee = True
score = int(score)
print(type(score));

#--------------------------------------------------------------

#input() = A function that prompts that user to enter data. Returns the entered data type as String.

name = input("What is your name?: ")
print(f"Hello {name}")

age1 = input("What is your age?: ")
age1 = int(age1)
age1 = age1 + 1
print(f"Your age is {age1}")

height1 = input("What is your height(cm)?: ")
height1 = str(height1)
# height1 = "Your height is {height1}"
print(f"Your height is: {height1}cm")

stu = input("Are you a student?(true or false):").lower()
stu1 = stu == "true"
if stu1:
    print("You are a student")
else:
    print("You are not a student!")

#--------------------------------------------------------------

#Arithmetic operators

#1. Addition (+)
a = 0
a += 1
#a = a + 1 is the same as a += 1
print(a)

#2. Subtraction (-)
b=0
b-=2
print(b)

#3. Multiplication (*)
c=10
c*=2
print(c)

#4. Division (/)
d=5
d/=3
print(d)

#5. Exponentiation (**)
e=4
e**=3
print(e)

#6. Modulus (%)
f=9
f%=2
print(f)

#--------------------------------------------------------------

#Math Functions

#1. round()
g = 3.14
g = round(g)
print(g) #Ans: 3

#2. abs() [abs = absolute]
h = -4
i = 10
h = abs(h)
i = abs(i)
print(h,i) #Ans: 4 10

#3. pow() [pow = power]
j = 5
j = pow(j, 3)
print(j) #Ans: 125

#4. max()
k = 10
m = 5
n = 15
result_max = max(k, m, n)
print(result_max) #Ans: 15


#5. min()
o = 20
p = 21
q = 19
result_min = min (o, p, q)
print(result_min) #Ans: 19

#--------------------------------------------------------------

#Math  Module Function [need to declar "import math"]
import math

print(math.pi)
print(math.e)

#1. math.sqrt() [sqrt = square root]
r = 9
r = math.sqrt(r)
print(r) #Ans: 3.0

#2. math.ceil() [ceil = ceiling (round upward to the nearest integer)]
s = 5.1
s = math.ceil(s)
print(s) #Ans: 6

#3. math.floor() [floor = floor (round downward to the nearest integer toward zero)]
t = 5.9
t = math.floor(t)
print(t) #Ans: 5
