#1.print helloworld
char=input("Enter the character:")
print(char)



#2. describe local variable and global variable code
# Global variable
global_var = "I am a global variable"

# Code block where a local variable is defined
if True:
    local_var = "I am a local variable"
    print(local_var)  # Accessing the local variable inside the block

# Accessing the global variable
print(global_var)  # Accessing the global variable outside the block


#3.Write a code that describe Indentation error

# Correctly indented global variable
global_var = "I am a global variable"
print(global_var)

# Intentional indentation error in the if block
if True:
    local_var = "I am a local variable"
    print(local_var)
   print("This line is incorrectly indented")  # This line has incorrect indentation...bcz it is not at his actual place


#4.write a code that describe local and global variable with same name


# Global variable
var = "I am a global variable"

print("Global scope before calling the block:")
print(var)  # Accessing the global variable

# Code block that redefines the same variable name locally
if True:
    var = "I am a local variable"
    print("\nInside the block:")
    print(var)  # Accessing the local variable

print("\nGlobal scope after calling the block:")
print(var)  # Accessing the global variable again

#5.Write a code for string, int and float input.

# Taking input for a string
str = input("Enter a string: ")

# Taking input for an integer
int = int(input("Enter an integer: "))

# Taking input for a float
float = float(input("Enter a float: "))

# Printing the inputs
print("\nInputs:")
print("String:", str)
print("Integer:", int)
print("Float:", float)