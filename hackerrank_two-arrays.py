q = int(input())

for i in range(q):
    n, k = map(int, input().strip().split())

    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    a.sort()
    b.sort(reverse=True)

    z = [1 for x,y in zip(a,b) if x + y < k]
    if sum(z) > 0:
        print('NO')
    else :
        print('YES')
            

    
