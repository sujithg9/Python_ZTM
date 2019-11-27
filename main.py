### Data Types
''' 
Data Type is a value in Python. Program stores information in these datatypes and modifies the values in them by actions (create, store, read, modify, remove). 

Fundamental datatype (core to the language)
int 
float
str
boot
list
set
tuple
dict 

Custom datatypes (Create our own datatype)
Class

Specialized datatypes
These datatypes are not build into python and are used from libraries. They are something like
1. Packages
2. Modules

These are used when there is not a predefined datatype or cannot create custom datatype we can used the specialized datatype from modules.

None 
None is nothing like a null value. 
'''


def switch(operation):
    switcher = {
        "ADD": "addition",
        "SUBSTRACT": "substraction",
        "DIVIDE": "division",
        "MULTIPLY": "multiplication",
    }
    return switcher.get(operation, "Invalid Operation")


def print_result(result):
    print("Result is %s of type %s" % (str(result), str(type(result))))


def get_data_type(a, b, operation):
    action = switch(operation)
    print("Performing %s on %s and %s" % (action, a, b))
    if action == "addition":
        c = a + b
        print_result(c)
    elif action == "substraction":
        c = a - b
        print_result(c)
    elif action == "multiplication":
        c = a * b
        print_result(c)
    else:
        c = a / b
        print_result(c)


a = int(input("Enter value for a : "))
b = int(input("Enter value for b : "))

get_data_type(a, b, "ADD")
get_data_type(a, b, "SUBSTRACT")
get_data_type(a, b, "MULTIPLY")
get_data_type(a, b, "DIVIDE")
