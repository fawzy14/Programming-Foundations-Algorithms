# use a recursive algorithm to find a maximum value


# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_max(items):
    # TODO: breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]

    # TODO: otherwise get the first item and call function
    # again to operate on the rest of the list
    op1 = items[0]
    op2 = find_max(items[1:])

    # TODO: perform the comparison when we're down to just two
    if op1 > op2:
        return op1
    else:
        return op2

    # test the function
print(find_max(items))
