# Return the max between two numbers 
import random
### NOT A GOOD IDEA! max already exists as built-in or we break it! Better take another name!!
def max(num1, num2):  ##  These are variable names, however when calling the function we can use any value
    if num1 > num2:
        result = num1
    else:
        result = num2

    return result

def main():
    i = random.randint(5,99)
    j = random.randint(11, 119)
    k = max(i, j) # Call the max function
    print("The maximum between", i, "and", j, "is", k)

main() # Call the main function
