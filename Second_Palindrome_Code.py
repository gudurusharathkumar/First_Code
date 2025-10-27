string = input("Enter a string: ")

# Reverse the string
rev = string[::-1]

# Check palindrome
if string == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
