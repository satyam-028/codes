x = 10 # -> global variable

def my_function():
    global x 
    x = 4 # -> this will change the value by x = 10 value
    y = 5  # -> local variable
    print(y)


my_function()
print(x)  # -> print 5
# print(y)

