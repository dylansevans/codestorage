import sys

#Scope describes the section of code in which data can be accessed. 
#A variable created within a function has a local scope to that function
#Python Parameters
#Best practice: Don’t modify parameters
#The global keyword can be used to specify that a variable refers to an outer scope.
x = 10

def function_1():
   x = 17
   print(sys._getframe().f_code.co_name, "x", x)

def function_2():
   global x
   x = 17
   print(sys._getframe().f_code.co_name, "x", x)

def double_and_remove(nums:list, word:str)->list[int]:
   nums.remove(2)
   nums.remove(6)
   word = word[::-1]

if __name__ == "__main__":
   print("----------Scope----------")
   function_1()
   print("__main__", "x", x)
   function_2()
   print("__main__", "x", x)

   print("----------Mutating Paramters----------")
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
   word = "HELLO"
   double_and_remove(numbers, word)
   # numbers has been changed
   print(numbers, word)