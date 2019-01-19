import string                        #Import the string module


def isValidVarName(strng):           #Implement the isValidVarName  method
    if (strng[0].isdigit()):
        return False

    else:
        invalidChars = set(string.punctuation.replace("_", ""))
        if any(char in invalidChars for char in strng):
            return False
        else:
            return True


def main():                              #Implement main method
    strng = input('Enter the string: ')  #Getting input from user


    finalString = ""

    if (isValidVarName(strng)):
         enhString = strng.title()
         finalString = finalString.join(enhString.split())
         finalString = finalString[0].lower() + finalString[1:]
         print('Output Variable Name: ' + finalString)
    else:
        print('Input string will not produce a valid Python variable name')

if __name__ == "__main__":
    main()                         # Call main method