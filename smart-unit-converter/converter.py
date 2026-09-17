print("Smart Unit Converter")
print("--------------------")
print("1. Temperature")
print("2. Distance")
print("3. Weight")

choice = input("What do you want to convert? ")

if choice == "1":
    temperature = float(input("Enter the temperature: "))
    unit = input("Is this in Celsius or Fahrenheit? ").lower()

    if unit == "celsius":
        result = (temperature * 9 / 5) + 32
        print(f"{temperature}°C is {result:.2f}°F")

    elif unit == "fahrenheit":
        result = (temperature - 32) * 5 / 9
        print(f"{temperature}°F is {result:.2f}°C")

    else:
        print("Please enter Celsius or Fahrenheit.")

elif choice == "2":
    distance = float(input("Enter the distance in kilometers: "))
    result = distance * 0.621371
    print(f"{distance} km is {result:.2f} miles")

elif choice == "3":
    weight = float(input("Enter the weight in kilograms: "))
    result = weight * 2.20462
    print(f"{weight} kg is {result:.2f} pounds")

else:
    print("That is not a valid choice.")
