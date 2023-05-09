string = input("Ingrese una cadena de caracteres: ")
flag = True

def balance(string):
    stack = []
    balances  = {'(': ')', '[': ']', '{': '}'}
    for special_character  in string:
        if special_character in balances.values():
            stack.append(special_character)
        elif special_character in balances.keys():
            if not stack or balances[special_character] != stack.pop():
                print("There is not a balance")
                return False
    if not stack:
        print("There is not a balance")
        return True
    else:
        print("There is a balance")
        return False

balance(string)
