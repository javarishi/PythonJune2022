test_list = [1,2,3,4,5,6]
print("Before error")

try:
    int_num = int(input("Enter a Number: "))
    print(test_list[0])
    division = len(test_list) / int_num
    print(division)
except IndexError as ier:
    print("There was some exception :: ", ier)
except ZeroDivisionError as zer:
    print("Replacing 0 with 1 because of ", zer)
    print((len(test_list)/1))
except Exception as ex:
    print("There is something wrong, unidentified error ", ex)
else:
    print("This statement will execute only when try completes successfully")
finally:
    print("This code will execute regardless of error")

print("After error")

'''
try:
    risky block of code (might throw an exception)
except OptionalException:
    block of code executes when exception occurs
    
1. Except block without specific exception accepts everything
2. You can have any number of except blocks
3. Generic exceptions are handled by Exception class
4. Specific First, Generic Later (Child First , Parent Later)
5. Exceptions can be combined with | in single except block
6. finally - block of code executes if there is an error or not
7. else block - executes only when try completes without errors
'''