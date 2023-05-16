
values={
    'centimeters': 100,
    'meters':1000,
    'kilometers':100000
}

option=input("Enter the option number that you prefer:\n"
      "1. Centimeters to meters\n"
      "2. Centimeters to kilometers\n"
      "3. Meters to centimeters\n"
      "4. Meters to kilometers \n"
      "5. Kilometers to centimeters\n"
      "6. Kilometers to meters\n"
             )
option='1'
def validate_option(option):
    if option in ['1','2','3','4','5','6']:
        return True
    else:
        return False

if validate_option(option)==True:
        value=float(input("Enter the value to convert: \n"))
        if option == '1':
            value=value/values['centimeters']
            print("The result is:\n", value)
        elif option == '2':
            value=value/values['centimeters']/values['kilometers']
            print("The result is:\n", value)
        elif option == '3':
            value=value*values['meters']
            print("The result is:\n", value)
        elif option == '4':
            value=value/values['meters']
            print("The result is:\n", value)
        elif option == '5':
            value=value*values['kilometers']
            print("The result is:\n", value)
        elif option == '6':
            value=value*values['meters']/values['kilometers']
            print("The result is:\n", value)
        else:
            print("Invalid option, please try again")
else:
    print("Invalid option, please try again")
