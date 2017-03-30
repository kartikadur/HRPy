if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        a, b, d, m = list(map(int, input().strip().split()))

        s = 0
        for i in range(a,b,d):
            if i % 2 == 0:
                s += a + 1
            else :
                s += a - 1
        print(s%m)
