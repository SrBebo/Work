values={#create our dictionary with the values we need to convert
    'centimeters': 0.1,
    'meters':0.01,
    'kilometers':0.00001
}

valueInMillimeters_to_convert=50#value to convert, this value is in millimeters

def convert_value_to_centimeters(valueInMillimeters_to_convert) -> float:#function to convert the value to centimeters
    return valueInMillimeters_to_convert*values['centimeters']
    
def convert_value_to_meters(valueInMillimeters_to_convert) -> float:#function to convert the value to meters
    return valueInMillimeters_to_convert*values['meters']

def convert_value_to_kilometers(valueInMillimeters_to_convert) -> float: #function to convert the value to kilometers
    return valueInMillimeters_to_convert*values['kilometers']


print(str(valueInMillimeters_to_convert) + " mm is equal to " + str(convert_value_to_centimeters(valueInMillimeters_to_convert)) + " cm")
print(str(valueInMillimeters_to_convert) + " mm is equal to " + str(convert_value_to_meters(valueInMillimeters_to_convert)) + " m")
print(str(valueInMillimeters_to_convert) + " mm is equal to " + str(convert_value_to_kilometers(valueInMillimeters_to_convert)) + " km")



