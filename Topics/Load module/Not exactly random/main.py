# place `import` statement at top of the program


# don't modify this code or variable `n` may not be available
import random

n = int(input())

# put your code here
random.seed(n)
print(random.randint(-100, 100))