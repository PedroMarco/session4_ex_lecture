__author__ = 'acpb859'
globalVar = 1
def f1():
    localVar = 2
    print(globalVar)
    print(localVar)
f1()
print(globalVar)
print(localVar) # Out of scope. This gives an error

# READ ALL EXAMPLES AND TRY TO UNDERSTAND. SEE A VIDEO MAYBE!


