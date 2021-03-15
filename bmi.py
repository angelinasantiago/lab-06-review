import sys # coding: utf-8

print("Welcome to BMI: Body Mass Index Calculator v.0.1 beta")
userWeight = input("Enter your weight (in pounds): ")
userHeight = input("Enter your height (in inches): ")
userHeightFloat = userHeight

myBMIpy = round((703 * float(userWeight)) / (userHeightFloat * userHeightFloat), 2)

print("Your body mass index (BMI) is " + str(myBMIpy) + "%")
