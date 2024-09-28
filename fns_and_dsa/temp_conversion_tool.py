FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    convertion = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return (f"{fahrenheit}°F is {convertion}°C")
    

def convert_to_fahrenheit(celsius):
    convertion = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return (f"{celsius}°C is {convertion}°F")
    

def main():
    # global temperature
    temperature = float(input("Enter the temperature to convert: "))
    convertion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

    if convertion == "c":
        result = convert_to_fahrenheit(temperature)
        print(result)
    
    elif convertion == "f":
        result = convert_to_celsius(temperature)
        print(result)
    else:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()


