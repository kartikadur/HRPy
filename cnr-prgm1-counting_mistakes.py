
def run_test():
    count1 = 4
    arr1 = [3,4,7,7]

    get_errors(arr1)

    count2 = 5
    arr2 = [1,3,2,3,4]

    get_errors(arr2)

def get_errors(arr):
    err_count = 0

    if arr[0] != 1 : err_count += 1

    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != 1 : err_count +=1

    print(err_count)


if __name__ == '__main__':
    #count = map(int,input().strip())
    #arr = list(map(int, input().strip().split()))

    run_test()



