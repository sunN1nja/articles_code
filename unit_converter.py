def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def main():
    print("Конвертер единиц")
    print("1. Километры в Мили")
    print("2. Мили в Километры")
    print("3. Футы в Метры")
    print("4. Метры в Футы")
    
    choice = input("Выберите операцию (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        value = float(input("Введите значение для конвертации: "))
        
        if choice == '1':
            print(f"{value} км = {km_to_miles(value):.2f} миль")
        elif choice == '2':
            print(f"{value} миль = {miles_to_km(value):.2f} км")
        elif choice == '3':
            print(f"{value} футов = {feet_to_meters(value):.2f} метров")
        elif choice == '4':
            print(f"{value} метров = {meters_to_feet(value):.2f} футов")
    else:
        print("Неправильный ввод")

if __name__ == "__main__":
    main()
