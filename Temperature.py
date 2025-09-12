def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    while True:
        print("\nTemperature Conversion Menu:")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit)}°C")
        elif choice == "2":
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()