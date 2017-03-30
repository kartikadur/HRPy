def time_to_candy(b, k):
    building, travel_time, min_tt = [], 0, 999999

    building = [i for i in range(1, len(b)) if b[i] == 1]
    for i in range(len(building) - 1):
        travel_time = building[i] + abs(building[i+1] - building[i])*k
        min_tt = min(min_tt, travel_time)
        #print(travel_time, building[i], building[i+1], min_tt)

    return min_tt
    
if __name__ == '__main__':
    n, k = list(map(int, input().strip().split()))
    buildings = list(map(int, input().strip().split()))

    print(time_to_candy(buildings, k))

    
