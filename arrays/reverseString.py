def reverseString(myString):
    result = ''
    for i in range(len(myString)):
        result += myString[len(myString) -1 -i]
    return result


if __name__ == "__main__":
    print reverseString("apple")

'''
OUTPUT:
elppa
'''