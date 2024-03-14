# var1 = 1        # Numbers: Signed integers
# var2 = 10.0     # Numbers: floating point real values
# str = 'Hello World!'      # String
# tinylist = [123, 'john']  # List
# tinytuple = (123, 'john') # Typle
# dict = {'name': 'john'}   # Dict

print("Hello")

#Example list:
print("***********Example list***********")
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print(list)          # Prints complete list
print(list[0])       # Prints first element of the list
print(list[1:3])     # Prints elements starting from 2nd till 3rd 
print(list[2:])      # Prints elements starting from 3rd element

#Example tuple:
print("***********Example tuple***********")
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
print(tuple)           # Prints complete list
print(tuple[0])        # Prints first element of the list
print(tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print(tuple[2:])       # Prints elements starting from 3rd element

#Example dictionary:
print("***********Example dictionary***********")
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values

#Example Decision Making:
print("***********Example Decision Making***********")
var = 49
if var < 200:   # if statement.
   print("Expression value is less than 200")
   if var == 150:
      print("Which is 150")
   elif var == 100: # nested if statement
      print("Which is 100")
   elif var == 50:
      print("Which is 50")
   elif var < 50:
      print("Expression value is less than 50")
else: # if...else statement
   print("Could not find true expression")

# Example for loop.
print("***********Example Loops***********")
for letter in 'Python':
    print('The letter: ', letter)

# Example while loop.
print("***********Example while Loop***********")
i = 2
while(i < 10):
   j = 2
   while(j <= (i/j)): # nested
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print("{} is prime".format(i))
   i = i + 1
else:
    print("Else of while!")
print("End!")

# Example functions.
print("***********Example function def***********")
#def sum(arg1 = 1, arg2): # SyntaxError: non-default argument follows default argument
def sum(arg1, arg2 = 1):
   # arg2 default value = 1.
   total = arg1 + arg2
   print("Inside the function : ", total)
   return total;

# Now you can call sum function
sum(3, 4);
sum(5); # Using default value for arg2.
sum(arg1 = 6);
#sum(arg2 = 7); # TypeError: sum() missing 1 required positional argument: 'arg1'
total = sum(arg1 = 8, arg2 = 9);
print("Outside the function : ", total)

# Example modules.
print("***********Example modules***********")
import module_operations
# now you can use functions defined in the module
result = module_operations.add(10, 5)
print(result)  # 15

# or import specific functions
from module_operations import subtract

# use the imported function directly
result = subtract(10, 5)
print(result)  # 5

# Example class.
print("***********Example class***********")
class myclass():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name) 

p1 = myclass("Huy", 21)

print(p1)
print(p1.name)
print(p1.age)
p1.myfunc()
# It does not have to be named self , you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()