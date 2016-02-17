sentinel_value = -5

positives = -1
negatives = 0

while sentinel_value != 0:
    if sentinel_value >0:
        positives+=1
        sentinel_value = eval(input('Enter an integer, input ends if equals to 0: '))
        print(sentinel_value)