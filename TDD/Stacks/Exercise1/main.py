def balance(string): # Function to check if the string is balanced
    stack = [] # Stack to store the special characters
    balances = {'(': ')', '[': ']', '{': '}'} # Dictionary with the special characters
    
    for special_character in string: # For loop to check if the special characters are in the string
        if special_character in balances.keys(): # If the special character is in the keys of the dictionary
            stack.append(special_character) # Append the special character to the stack
        elif special_character in balances.values(): # If the special character is in the values of the dictionary
            if not stack or balances[stack.pop()] != special_character: # If the stack is empty or the special character is not equal to the last element of the stack
                return False
    
    return len(stack) == 0 # Return if the length of the stack is equal to 0

string = "()[]{}"
if balance(string):
    print("There is a balance")
else:
    print("There is not a balance")
