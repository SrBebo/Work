string = input("Enter the string: ")
stack = []

def reverse_string(string):
    result_string=""
    for character in string:
        stack.append(character)
        print("\n",stack,"\n")
    while stack:
        
        result_string += stack.pop()
        print("\n",stack,"\n")
        print("\n",result_string,"\n")
    return result_string


print("The result of: ", string, "is: ", reverse_string(string))
