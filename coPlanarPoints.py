
def crossProd (x, y):
    return [
        x[1]*y[2] - x[2]*y[1],
        x[0]*y[2] - x[2]*y[0],
        x[0]*y[1] - x[1]*y[0]
    ]

def dotProdOriginal (x, y):
    return [
        x[0]*y[0] + x[1]*y[1] + x[2]*y[2]
    ]

def dotProd (x, y):
    return [sum(list(map(lambda a, b: a * b, x, y)))]

def vector(x,y):
    return list(map(lambda a, b: b - a, x, y))

# STDIN
# for _ in range(int(input().strip())):
    
#     a = list(map(int, input().strip().split(" ")))
#     b = list(map(int, input().strip().split(" ")))
#     c = list(map(int, input().strip().split(" ")))
#     d = list(map(int, input().strip().split(" ")))
    
#     if dotProd(crossProd(a,d),crossProd(crossProd(a, b),crossProd(a,c))) == [0]:
#         print("YES")
#     else :
#         print("NO")

# FILE INPUT
with open("coPlanarPointsData/coPlanarQuestions.txt") as f:
    for _ in range(int(f.readline())):
        
        a = list(map(int, f.readline().strip().split(" ")))
        b = list(map(int, f.readline().strip().split(" ")))
        c = list(map(int, f.readline().strip().split(" ")))
        d = list(map(int, f.readline().strip().split(" ")))


        if dotProd(vector(a,d),crossProd(vector(a,b),vector(a,c))) == [0]:
            print("YES")
        else :
            print("NO")