""" 
Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.

User inputs a number, which is then stored in the max_int variable.
As user keeps inputing numbers, they are continuously compared to the current max_int
with bigger numbers becoming the new max_int. This continues until the user
submits a number less than or equal to zero.
 
 """

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code


while num_int > 0:
    #num_int = int(input("Input a number: "))    # Do not change this line
    max_int = num_int
    if max_int > num_int:
       print(max_int)
    elif max_int < num_int:
        max_int = num_int
        print(max_int)    # Do not change this line
if num_int <= 0:
    print("The maximum is", max_int)
