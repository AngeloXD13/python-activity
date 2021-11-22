
def checkIfPalindrome(input):

    reversedStr = ''.join(reversed(input))
    if (input == reversedStr):
        return True
    return False

string = input("input: ")

answer = checkIfPalindrome(string)

if (answer):
    print(string, " is a palindrome")
else:
    print(string, " is not a palindrome")