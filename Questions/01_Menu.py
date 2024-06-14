# Write a menu driven program to convert the given temperature from Fahrenheit to Celsius and vice versa depending upon users choice.

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("\n[Temperature Conversion Menu]")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
print("3. Exit")

choice = int(input("Enter your choice (1/2): "))

if (choice == 1):
    far = int(input("Enter Fahrenheit: "))
    print(fahrenheit_to_celsius(far))
elif(choice == 2):
    cel = int(input("Enter Celsius: "))
    print(celsius_to_fahrenheit(cel))
elif(choice == 3):
    print("Exiting the program. Goodbye!")
else:
    print("Invalid choice.")