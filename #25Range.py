# Range Function --> Range Function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and stops before a specific number

# range(start?, stop, step?)
# The range() function can take up to three arguments:
# 1. start (optional) - The starting value of the sequence (default is 0).
# 2. stop (required) - The value at which the sequence stops (not included in the sequence).
# 3. step (optional) - The difference between each number in the sequence (default is 1).

seq = range(10)  # This creates a range object that includes numbers from 0 to 9.

print(type(seq))  # <class 'range'> - The type of the 'seq' object is 'range'.

for i in seq:
    print(i)  # This prints numbers from 0 to 9.

# We can write range in three ways

range(10)  # This means from 0 to 9 with step size 1 (default).

range(2, 10)  # This means from 2 to 9 with step size 1 (default).

range(1, 10, 2)  # This means from 1 to 9 with step size 2.

for i in range(1, 10, 2):
    print(i)  # This prints numbers from 1 to 9 with a step size of 2, i.e., 1, 3, 5, 7, 9.
