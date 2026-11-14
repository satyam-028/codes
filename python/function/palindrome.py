string = "madam"

def palindrome(string):
    copy_string = ""
    for i in string:
        copy_string = string[::-1]
        if copy_string == i:
            return "The is palindrome"
        else:
            return "This not palindrome"
        

print(palindrome(string))