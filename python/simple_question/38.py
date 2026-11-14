# try:
#     x = 1/0
# except ValueError:
#     x = 0

# print(x)




try:
    x = 1/0
except ZeroDivisionError:
    x = 0

print(x)