
def countAds(playlist, breaktime) -> int:

    ads = 0
    time = 0

    for i, e in enumerate(playlist):
        if (time + e) >= breaktime:
            if i == len(playlist) - 1:
                ads += 0
            else:
                ads += 1
            time = 0
        else:
            time += e

    return ads

def numAds(playlist, breaktime) -> list:

    ads = []

    for i, e in enumerate(playlist):
        otherplaylist = playlist[i:] + playlist[:i]
        ads.append(countAds(otherplaylist, breaktime))

    return ads

if __name__ == '__main__':
    
    numsongs, breaktime = map(int, input().split())
    playlist = list(map(int, input().split()))

    ads = numAds(playlist, breaktime)

    for i, e in enumerate(ads):
        if i == len(ads) - 1:
            print(e)
        else:
            print(e, end=" ")