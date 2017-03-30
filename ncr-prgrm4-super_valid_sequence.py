def k_super_valid(term, k):
    count = 0
    for i in range(len(term) - 1):
        if (term[i] != term[i+1]):
            count += 1

##    print(count, count>=k)
    if (count >= k) : return True
    else : return False


def bracket_seq(n, k):
    from itertools import product
    super_k = 0
    brackets = '()'
    combinations = ['('.join(i) for i in product(brackets, repeat=n-1)]
    print(combinations)
    for i in range(1,int((2**n)/2)):
        stack = []
        rem = ''
        add = ''
        for j in combinations[i]:
            if j == '(':
                stack.append('(')
            if j == ')':
                if stack:
                    stack.pop()
                else :
                    rem = combinations[i]
                    break
        if rem:
            combinations.remove(rem)
        elif stack == []:
            if k_super_valid(combinations[i],k): super_k += 1

    print(super_k%(10**9+7))

if __name__ == '__main__':
    q = int(input().strip())
    for i in range(q):
        n,k = list(map(int,input().strip().split()))
        bracket_seq(n,k)
        
        
