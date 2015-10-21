# "sps" Python PostScript Interpreter Part 1 & 2

# The operand stack: define the operand stack and its operations in this notebook cell
opstack = []

# now define functions to push and pop values on the opstack according to your decision about which
# end should be the hot end.

# Pops an operator. Default pop(0) from the top
def opPop(): 
    if len(opstack) > 0:
        return opstack.pop()

# Pushes value to opstack
def opPush(value):
    opstack.append(value)

# Remember that there is a Postscript operator called "pop" so we choose different names for these functions.

# The dictionary stack: define the dictionary stack and its operations in this cell
dictstack = [{}]
# now define functions to push and pop dictionaries on the dictstack, to define name, and to lookup a name

# Pops an entry in dictstack. Default pop(0) from the top
def dictPop():
    if dictstack == []:
        print("dictstack is empty")
    return dictstack.pop()

# Pushes value to dictstack
def dictPush(value):
    dictstack.append(value)

# **Renamed psDef according to given test cases
def psDef():
    right = opPop()
    left = opPop()
    # If dictstack is empty
    if dictstack == []:
        # Append an empty dict
        dictstack.append({})
    value = dictPop()
    value[left[1:]] = right
    dictPush(value)
    
# If statement function
def psIf():
    right = opPop()
    left = opPop()
    tmpList = []
    # If condition satisfied
    if left == True:
        args.clear()
        for x in right:
            tmpList.append(x)
        interpret(tmpList)

# If else statement function
def psIfElse():
    right = opPop()
    middle = opPop()
    left = opPop()
    tmpList = []  
    # If condition satisfied: execute if argument
    if left == True:
        args.clear()
        for x in middle:
            tmpList.append(x)
        interpret(tmpList)
    # Else condition satisdied: execute else argument    
    else:                                           
        args.clear()
        for x in right:
            tmpList.append(x)
        interpret(tmpList)

# Search the dictionaries on the dictionary stack starting at the hot end to find one that contains name and return 
# the value associated with name
def lookup(name):
    var = 0
    tmp = []
    
    for x in dictstack:
        tmp.append(x)

    tmp.reverse()
    
    for y in tmp:
        var = y.get(name, 0)
        if var != 0:
            return var
    if var == 0: 
        print("Variable not found")
    return var

    # return the value associated with name
    # what is your design decision about what to do when there is no definition for name

# Arithmetic operators: define all the arithmetic operators in this cell -- add, sub, mul, div, eq, lt, gt

# Adds first two items on opstack
def add():
    first = opPop()
    second = opPop()
    opPush(first + second)

# Subtracts first two items on opstack
def sub():
    first = opPop()
    second = opPop()
    opPush((-1) * (first - second))
     
# Multiplies first two items on opstack
def mul():
    first = opPop()
    second = opPop()
    opPush(first * second)
    
# Divides the first item on opstack by the second item
def div():
    first = opPop()
    second = opPop()                    
    opPush(second / first)                      
    
# True if first item equals second item
def eq():
    first = opPop()
    second = opPop() 
    opPush(first == second)

# True if first item < second item
def lt():
    first = opPop()
    second = opPop() 
    opPush(first > second)

# True if first item > second item
def gt():
    first = opPop()
    second = opPop() 
    opPush(first < second)  

# Boolean operators: define all the boolean operators in this cell -- and, or, not

# Logical bitwise and (both must be 1 to be true)
def andd():
    first = opPop()
    second = opPop()
    opPush(first and second)

# Logical bitwise or (one must be 1 to be true)
def orr():
    first = opPop()
    second = opPop()
    opPush(first or second)

# Reverses whatever the value on opstack was
def nott():
    opPush(not opPop())

# Define the stack manipulation operators in this cell: dup, exch, pop

# Pops a value off opstack and pops it back on twice
def dup():
    first = opPop()
    opPush(first)
    opPush(first)

# Pops values off opstack and pops them on in reverse order
def exch():  
    first = opPop()
    second = opPop()
    opPush(first)
    opPush(second)

# Define the dictionary manipulation operators in this cell: dictz, begin, end, def
# name the function for the def operator psDef because def is reserved in Python

# Creates and returns a new dictionary
def dictz():
    newdict = {}
    opstack.append(newdict)

# Appends a new dictionary to dictstack
def begin():
    d = opstack.pop()
    if d != {}:
        print("Error. Not a dictionary");
        exit(0)
    dictstack.append(d) 

# Removes a dictionary from dictstack
def end():
    return dictstack.pop()

# = printing function. Only prints the top item of the opstack
def pop_and_print():
    print("Top element of opstack:")
    first = opstack.pop()
    print(first)
    opstack.append(first)
    
def stack():
    tmp = []
    print("")
    print("opstack:")
    while opstack != []:
        tmp.append(opstack.pop())
        print(tmp[-1])
    while tmp != []:
        opstack.append(tmp.pop())
    
def printdictstack():
    tmp = []
    print("")
    print("dictstack:")
    while dictstack != []:
        tmp.append(dictstack.pop())
        print(tmp[-1])
    while tmp != []:
        dictstack.append(tmp.pop())

import re

# Given function Tokenize, which well, tokenizes the inputted program which prepares it for being parsed.
def Tokenize(s):
    programTokens = re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|%.*|[^ \t\n]", s)
    return Parse(programTokens)

# In this cell, write your parsing code; it takes a list of tokens produced by tokenize
# and returns a code array; copy this cell into your sps.ipynb notebook and write the 
# necessary code. Of course you may create additional functions to help you write parse()

# In this cell, write your parsing code; it takes a list of tokens produced by tokenize
# and returns a code array; copy this cell into your sps.ipynb notebook and write the 
# necessary code. Of course you may create additional functions to help you write parse()
# The parsing function will format all the tokens and check for bracket matching.
bracketsMatch = 0
# Takes a list of tokens, correctly parses it, and returns a code array.
def Parse(programTokens):
    code = []   # Code array
    while programTokens != []:
        
        code.append(programTokens.pop(0))
        # If it is a number
        try:
            code[-1] = int(code[-1])
        except:
            pass
        # If left bracket
        if code[-1] == "{":
            CheckBrackets(1 ,1)
            code.pop()
            code.append(Parse(programTokens))
        # Close with right bracket
        elif code[-1] == "}":
            CheckBrackets(-1, 1)
            code.pop()
            return code
    CheckBrackets(0, 0)
    bracketsMatch = 0
    return code

# Helper function that checks if the brackets are paired up and for any mismatched brackets.
def CheckBrackets(n, run):
    global bracketsMatch
    
    bracketsMatch = bracketsMatch + n
    if run == 1:
        if bracketsMatch < 0:  # Checks for negative value 
            print("Error with brackets, please check input")
            exit(0)
    elif run == 0:             # Checks at the end
        if bracketsMatch != 0: # Should == 0
            print("Error with brackets, please check input")
            exit(0)

# Function dict that stores and maps all the functions to strings
functionDict = {}
def InitializeFunctionDict():
    global functionDict  
    functionDict["pop"] = opPop
    functionDict["def"] = psDef
    functionDict["if"] = psIf     
    functionDict["ifelse"] = psIfElse
    functionDict["add"] = add
    functionDict["sub"] = sub
    functionDict["mul"] = mul
    functionDict["div"] = div
    functionDict["eq"] = eq   
    functionDict["lt"] = lt
    functionDict["gt"] = gt
    functionDict["and"] = andd
    functionDict["or"] = orr
    functionDict["not"] = nott   
    functionDict["dup"] = dup
    functionDict["exch"] = exch
    functionDict["dictz"] = dictz
    functionDict["begin"] = begin
    functionDict["end"] = end
    functionDict["pop_and_print"] = pop_and_print
    functionDict["="] = pop_and_print
    functionDict["stack"] = stack

# Copy this cell to your sps.ipynb and write the necessary code; again write
# auxiliary functions if you need them. This will probably be the largest
# function of the whole project, but it will have a very regular and obvious
# structure if you've followed the plan of the assignment.

# Function that takes a code array and reads and executes them
def interpret(code):
    while code != []:
        try:
            Execute(code.pop(0))
        except:
            print("Attempting to evaluate invalid argument")

# Helper/auxiliary function to call all the functions in the right order
def interpreter(program):
    opstack.clear()
    dictstack.clear()
    InitializeFunctionDict()
    code = Tokenize(program)
    interpret(code)
    stack()
    printdictstack()

# More utility functions in this cell for reading and executing the given arguments

args = [] # List for storing arguments that aren't complete postscript statements
# Reads and execute the arguments
# Credit/Citation: collaborated with Jesse Chrisholm off github for the idea of these functions below
def Execute(Argument):
    global functionDict
    global args
    
    exception = Execute2
    args.append(Argument)
    try:        # Check if the argument is in the dict
        exception = functionDict.get(Argument, Execute2)
    except:
        pass
    exception() # If not, use args
    args.clear()
    
# Handles everything thats not a complete postscript command
def Execute2(): 
    global args
    
    if type(args[0]) == str:
        # Var args
        if args[0][0] == "/":
            opPush(args[0])
        # If bool == true
        elif args[0] == "true":
            opPush(True)
        # If bool == false
        elif args[0] == "false":
            opPush(False)
        else:
            # Look up var name in args list
            var = lookup(args[0])
            # If it has arguments
            if type(var) == list: 
                varArgs = []  
                for each in var:
                    varArgs.append(each)
                args.clear()
                interpret(varArgs)
                return
            opPush(var) # Result goes on the stack
                       
    elif type(args[0]) == list:
        opPush(args[0])
    elif type(args[0]) == int:
        opPush(args[0])
    args.clear()
    
# If, If Else, the dictstack printing function are all found above the "Interpreter Part 2" line and their respective cells.

interpreter(
"""
/fact{
   dictz exch exch begin
      /n exch def
         n 2 lt
         { 1}
         {n 1 sub fact n mul }
      ifelse
   end
}def
5 fact =
"""
)