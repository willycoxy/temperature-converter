# Temperature Converter

# Ask user what temperature 
def celsius_to_fahrenheit(cels):
    return (cels * 9/5) + 32

def celsius_to_kelvin(cels):
    return (cels + 273.15)

def fahrenheit_to_celsius(fahr):
    return (fahr - 32 ) * 5/9

def fahrenheit_to_kelvin(fahr):
    return (fahr - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelv):
    return kelv - 273.15

def kelvin_to_fahrenheit(kelv):
    return (kelv - 273.15) * 9/5 + 32


print("Thank you for using the Temperature Converter!")
# Asks user what the temperature is

temp = float(input("Please enter the temperature "))

# Ask user what unit of temperature they are using 
print("\nWhat Unit of Temperature are you using ")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")


current_unit = input ("Enter 1, 2, or 3 ")

# Ask user what unit they are converting too

print("\nWhat Unit of Temperature do you want to convert to ")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

new_unit = input ("Enter 1, 2, or 3 ")

if current_unit == '1' and new_unit == '2':
    conversion = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is {conversion:.2f} °F")

elif current_unit == '1' and new_unit == '3':
    conversion = celsius_to_kelvin(temp)
    print(f"{temp}°C is {conversion:.2f} K")

elif current_unit == '2' and new_unit == '1':
    conversion = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is {conversion:.2f} °C")

elif current_unit == '2' and new_unit == '3':
    conversion = fahrenheit_to_kelvin(temp)
    print(f"{temp}°F is {conversion:.2f} K")

elif current_unit == '3' and new_unit == '1':
    conversion = kelvin_to_celsius(temp)
    print(f"{temp}K is {conversion:.2f} °C")

elif current_unit == '3' and new_unit == '2':
    conversion = kelvin_to_fahrenheit(temp)
    print(f"{temp}K is {conversion:.2f} °C")

elif current_unit == new_unit:
    print("You selected the same unit, no conversion needed!")

else:
    print("Invalid selection, please enter a valid option")












