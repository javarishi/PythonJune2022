def greet(name='Unknown User'):
    print("Hello", name.upper())

# function can have another function - internal / inner functions
# local functions
def calculator(varOne, varTwo, operation):

    def add():
        return varOne + varTwo

    def multiply():
        return varOne * varTwo

    if operation == "add":
        return add
    else:
        return multiply


# tax calculator for list of items
# see the item - food, non_food  = tax_2% non_food=12.36% total
# use local functions


math_ops = calculator(5,10, 'add')
print(math_ops())


greet("Rishi")
hello = greet
hello("Students")
