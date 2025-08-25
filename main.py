from converter import length, temperature
def main():
    print("1.length converter")
    print("2. Temperature converter")
    opperation = int(input("Choose an operation: "))
    if opperation == 1:
        print("1. Convert km to meters")
        print("2. Convert meters to cm")
        option1 = int(input("choose an option: "))
        
        if option1 == 1:
            km = float(input("Enter value in km: "))
            meters = length.km_to_meters(km)
            print(f"{km} km is equal to {meters} meters")
        elif option1 == 2:
            meters = float(input("Enter value in meters: "))
            cm = length.meters_to_cm(meters)
            print(f"{meters} meters is equal to {cm} cm")
        else:
            print("Invalid option")
    elif opperation == 2:
        print("1. Convert celsius to fahrenheit")
        print("2. Convert fahrenheit to celsius")
        option2 = int(input("choose an option: "))
        if option2 == 1:
            celsius = float(input("Enter value in celsius: "))
            fahrenheit = temperature.c_to_f(celsius)
            print(f"{celsius} celsius is equal to {fahrenheit} fahrenheit")
        elif option2 == 2:
            fahrenheit = float(input("Enter value in fahrenheit: "))
            celsius = temperature.f_to_c(fahrenheit)
            print(f"{fahrenheit} fahrenheit is equal to {celsius} celsius")
        else:
            print("Invalid option")
    else:
        print("Invalid operation")  
if __name__ == "__main__":
    main()
        