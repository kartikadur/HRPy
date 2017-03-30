#clockwise: up right down left
direction = {'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1)}

def run_test():
    n, m = 3, 5
    arr = [['a','#','#','a','r'],['a','#','a','a','#'],['x','x','w','s','r']]

    print(get_message(arr,n,m))


def get_message(arr, r, c):

    curr_dir = direction['U']
    curr_r, curr_c = r - 1, 0
    next_r, next_c = r, c - 1
    rem_r, rem_c = next_r, next_c
    word = ''
##    word_list = []
    word_count = 0
    is_row = True

    while next_r > -1 or next_c > -1:
        
        #get the letter at current location    
        if arr[curr_r][curr_c] != '#':
            word += arr[curr_r][curr_c]
        else :
            if word != '':
##                word_list.append(word)
                word = ''
                word_count += 1
        
        #change counters
        if curr_dir == direction['U'] or curr_dir == direction['D']:
            rem_r -= 1
        else :
            rem_c -= 1
        curr_r += curr_dir[0]
        curr_c += curr_dir[1]

##        print('before: ', is_row, curr_dir, curr_r, curr_c, rem_r, rem_c, next_r, next_c, letter, word, word_list)

        if rem_r == 0 and rem_c == 0:
            if word != '':
##                word_list.append(word)
                word = ''
                word_count += 1
            return word_count

        #change directions and reset counters
        if is_row and rem_r <= 0:
            curr_r -= curr_dir[0]
            next_r -= 1
            rem_r = next_r
            is_row = not is_row
            if curr_dir == direction['U']:
                curr_dir = direction['R']
                curr_c += curr_dir[1]
            else :
                curr_dir = direction['L']
                curr_c += curr_dir[1]

        if not is_row and rem_c <= 0:
            curr_c -= curr_dir[1]
            next_c -= 1
            rem_c = next_c
            is_row = not is_row
            if curr_dir == direction['R']:
                curr_dir = direction['D']
                curr_r += curr_dir[0]
            else :
                curr_dir = direction['U']
                curr_r += curr_dir[0]

        
##        print('after: ', is_row, curr_dir, curr_r, curr_c, rem_r, rem_c, next_r, next_c, letter, word, word_list)
    
        
        
    
    #print(curr_direction, curr_location, curr_visited)
    



if __name__ == '__main__':
#    [n,m] = list(map(int, input().strip().split()))
#    arr = list(map(int, input().strip().split()))
##    a,b = list(map(int, input().strip().split()))
##    arr = []
##    for i in range(a):
##        temp = input().strip().split()
##        arr.extend(temp)
##    print(get_message(arr, a, b))
    run_test()
