# 03_input_output.py
# Learning input and output in Python

name = input("Enter your name: ")
age = input("Enter your age: ")

print(name)
print(age)

print(type(name))
print(type(age))

age = int(age)

print(age + 1)
print(type(age))

# Example Study
Height = input("Enter Your Height (meters): ")
Weight = input("Enter Your Weight (kg): ")

Height = float(Height)
Weight = float(Weight)

BMI = Weight / (Height * Height)
print("Your BMI Score Is: ", BMI)

print(Weight, type(Weight), Height, type(Height), BMI, type(BMI))
