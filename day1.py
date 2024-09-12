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


