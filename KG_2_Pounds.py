print("          Kilograms to Pounds\n")

print('Kilograms    ','Pounds\n')


for i in range(1, 199):
    print(i, end = '')
    for j in range(1, 10):
        # Display the product and align properly
        print(format(i * j, '4d'), end = '') ### 4d is the 4 characters for the value
    print()# Jump to the new line
