# Initialize sum
sum = 0

# Add 0.01, 0.02, ..., 0.99, 1 to sum
### NOTE!!! The 49.50 value is not an error, just due to SUM being different than i!!
i = 0.01
while i <= 1.0:
    sum += i
    i = i + 0.01

# Display result
print("The sum is", sum)