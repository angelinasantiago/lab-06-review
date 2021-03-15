tempincelsius = input("Please enter a temperature in Celsius...")
# print(tempincelsius)
# print(type(tempincelsius))

tempinfarhenheit = float(tempincelsius) * 1.8 + 32
# print(tempinfarhenheit)
# print(type(tempinfarhenheit))

roundedF = round(tempinfarhenheit, 2)

print(tempincelsius + " degrees celsius is " + str(roundedF) + " degrees farhenheit.")
