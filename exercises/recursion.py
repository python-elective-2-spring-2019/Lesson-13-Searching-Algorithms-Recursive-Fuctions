# print out all numbers from n down to zero 
# Do it with a recursive approach and after that the same with a loop. 
# When this is done you should change the code so it will print out 0 to n instead
# (the numbers in accending order).


def number_recursion(n):
    # Base Case print(0) 
    if n == 0:
        print(0)

    # Recursive case    
    else:
        number_recursion(n-1)
        print(n)
        



def number_loop(n):
    for i in range(0, n, -1):
        print(i)


def main():
    number_recursion(5)

    #number_loop(5)


if __name__ == "__main__":
    main()