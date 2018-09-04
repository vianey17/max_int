""" Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.
 
Make sure that you write up the algorithm before starting to code.
Then implement the algorithm in Python. Put your algorithmic description as a comment in the program file.
 
During the design of your algorithm and your implementation, you should use git:
Create an account on github.com (if you don't already have it).
Initialize a local directory with git init.
Write the text of your algorithm in a file called max_int.py
Expect the result of git status
Use git add . to move changes to the staging area.
Commit your changes with git commit -m “Algorithm written for max_int”
Then start implementing your algorithm
During your implementation, make sure you do git status, git add, and git commit regularly.
You can see a log of all your commits with git log.
When you have finished your implementation:
Create a public repository on github
Follow the instructions under "push an existing repository from the command line"
Push your changes to the remote repo with: git push
Inspect your commits on github """

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
