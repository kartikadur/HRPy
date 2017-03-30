from collections import OrderedDict

##def giant_numbers(arr, q):
##
##    for _ in range(q):
##        x, k = list(map(int, input().strip().split()))
##        d = len(list(filter(lambda i: x % i == 0, arr)))
##        if d >= k:
##            print('Yes')
##        else :
##            print('No')

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arr_dict = {}

    for i in arr:
        if i in arr_dict:
            arr_dict[i] += 1
        else :
            arr_dict[i] = 1

    arr_dict = OrderedDict(sorted(arr_dict.items()))
    print(arr_dict)
    
    q = int(input().strip())
    
    for _ in range(q):
        x, k = list(map(int, input().strip().split()))
        d = 0
        for i, j in arr_dict.items():
            if i > x: break
            if x % i == 0:
                d += j
        if d >= k:
            print('Yes')
        else :
            print('No')
