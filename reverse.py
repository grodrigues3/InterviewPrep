def reverse_string(myString):
    myLength = len(myString)
    newString = ''
    for i in range(myLength):
        newString += myString[myLength-i-1]
    return newString

print reverse_string("hello")
