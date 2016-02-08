## NOTE: Area of the square, 2x2 = 4. Area of the circle (radius 1) pi*r^2, so pi, so 3.141592
##

import random

NUMBER_OF_TRIALS = 100000 # Constant
numberOfHits = 0

for i in range(NUMBER_OF_TRIALS):
    x = random.random() * 2 - 1   ##  random.random() Return the next random floating point number in the range [0.0, 1.0)
    y = random.random() * 2 - 1   ## *2 -1 will make value possible from 1 to -1 so axis can be generated

    if x * x + y * y <= 1:  ##  pi*r^2 => 1 = 3.141592 or less, I believe basic probability and logarithms missing by me...
        numberOfHits += 1

pi = 4 * numberOfHits / NUMBER_OF_TRIALS

print("PI is", pi)

###### Coordinates give the radius size, and could be up to 2 even being inside the square? Don't think so.