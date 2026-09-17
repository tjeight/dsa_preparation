number = int(input("Enter any number: "))

# increasing pattern
for row in range(1, number):
    print("*" * row)

# decreasing stars
for row in range(number - 1, 0, -1):
    print("*" * row)


"""
Time complexity O(N2)
"""
