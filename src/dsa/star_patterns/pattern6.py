# Accept the input from the user

number = int(input("Enter any number: "))


# Trick find the rows and columns.

# The iterations are simple make that much rows when there are that much columns

for row in range(number):
    for column in range(number, row, -1):
        print("*", end="")

    print()

"""
Time complexity:O(N**2)
"""
