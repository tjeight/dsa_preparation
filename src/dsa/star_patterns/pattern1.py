# Accept the input from the user

n = int(input("Enter any number: "))


for i in range(n):
    # init the nested loop
    for j in range(n):
        print("*", end="")
    print()


"""
Time complexity : O(n**2)

"""
