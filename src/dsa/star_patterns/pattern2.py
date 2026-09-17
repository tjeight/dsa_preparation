# Accept the input from the user

n = int(input("Enter any number: "))


# Trick find the rows and columns.

# The iterations are simple make that much rows when there are that much columns

for row in range(n):
    for column in range(row + 1):
        print("*", end="")
    print()


"""
Time Complexity :O(n**2)
"""
