# Next number is sum of three previous numbers in sequence.
# First declare most basic numbers needed to start sequence,
# Then create a while loop that repeats code as long as
# user specified length. Variables a b c and d update
# to their corresponding values until loop is done, 
# only printing last value, d.


n = int(input("Enter the length of the sequence: ")) # Do not change this line
a = 1
b = 2
c = a+b
d = a+b+c
if n ==1:
    print(a)
elif n==2:
    print(a)
    print(b)
elif n<=0:
    print("Invalid entry.")
elif n == 3:
    print(a)
    print(b)
    print(c)
else:
    print(a)
    print(b)
    print(c)
    while n > 3:
  
        
        
        
        d = a+b+c
        print(d)
        a = b
        b = c
        c = d

        n -= 1