__author__ = 'acpb859'
sum = 0
for i in range(1, 10):
    sum += i
print("Sum from 1 to 10 is", sum)


##############################
#Another one inside this one##
##############################

def sum(i1, i2):  ###  i1 and i2 are variable names, can be anything
    result = 0
    for i in range(i1, i2):
        result += i
    return result
def main():
    print("Sum from 1 to 10 is", sum(1, 10))
    print("Sum from 20 to 37 is", sum(20, 37))
    print("Sum from 35 to 49 is", sum(35, 49))

main() # Call the main function