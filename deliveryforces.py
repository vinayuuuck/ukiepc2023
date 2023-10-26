
def delivery(strenth, dnum):
    
    maximal_str = 0

    strenth.sort()

    endpos = dnum - 1

    for _ in range(dnum//3):

        maximal_str += strenth[endpos - 1]

        endpos -= 2

    return maximal_str





if __name__ == '__main__':
    
    drivernum = int(input())

    driverstrength = list(map(int, input().split()))

    print(delivery(driverstrength, drivernum))
