#count down using recursion

def count_down(x):
    if x == 0:
        print('Done!')
        return
    else:
        print(x, '....')
        count_down(x-1)

count_down(6)