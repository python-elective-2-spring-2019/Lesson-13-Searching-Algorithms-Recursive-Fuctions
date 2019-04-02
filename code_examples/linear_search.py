
""" Linear search on an unsorted list """
def linear_search(l, e):
    for i in range(len(l)):
        if e == l[i]:
            return True
    return False

print(linear_search([1, 2, 65, 4, 7, 6, 7], 10))

""" Linear search on a sorted list """
def search(l, e):
    for i in range(len(l)):
        if l[i] == e:
            return True
        if l[i] > e:
            return False
    return False
