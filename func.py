# Adding function

def myFunction(a ,b):
    return a+b;

print(myFunction(10,20));

a = myFunction(1 ,2);
print(a);

# types of functions in python
# 
# 1. Built in functions
# 
# print()  # Output to console
# len()    # Get length of sequence
# type()   # Check object type
# input()  # Get user input
# int(), float(), str()  # Type conversion
# sum(), min(), max()    # Math operations 

#2.User Defined functions
def greet(name):
    return f"Hello, {name}!"
# Call the function
print(greet("Anil"));

# 3. Class based function

class Dog:
    def __init__(self ,name):
        self.name = name;
    def bark(self):
        return f"{self.name} woooff!" # this is Formmated print that will print variabels inside also no need to use + and close gthe string ok \
Do = Dog("Bob");
print(Do.bark());    


# the lambda((Anonymous Functions)) function

A = lambda a,b : a+b ;
print(A(2,3));

#4. Recursive Functions

def factorial(n):
    if n==1:
        return 1 # it is a base case
    else:
        return n*factorial(n-1); # recursive call means it calls it self agin and again until it reaches base case 
print(factorial(5));

#7. Nested Functions

def outer():
    x = 10
    def inner():
        print(x)
    return inner()

print(outer());