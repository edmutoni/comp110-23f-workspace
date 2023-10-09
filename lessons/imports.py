"""Practice Importing from other Modules"""

#from <package name> import <module name>

from lessons import importing_modules
from lessons.importing_modules import addition

print(addition(1,2))

#print(importing_modules.addition(1, 2))

#Function: from <module name>.<fucntion name>(arguments)
#Variable: <module name>.<variable name>

#print(importing_modules.my_variable)
 
if __name__ == "__main__":
    print("Howdy")

