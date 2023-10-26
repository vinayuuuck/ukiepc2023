
def calcCharge(boat2d, numcards):
    charges = {}
    for i in range(1, numcards+1):
        charges[i] = [0, 0, 0, 0]

    for event in boat2d:
        if charges[event[1]][0] == 0:
            charges[event[1]][0] = event[0]
            charges[event[1]][1] += 1
            charges[event[1]][3] = event[0]

        elif charges[event[1]][0] == event[0]:
            charges[event[1]][2] += 100
            charges[event[1]][1] += 1
            charges[event[1]][0] = 0 if (charges[event[1]][1] % 2 == 0) else event[0]

        elif charges[event[1]][0] != event[0]:
            charges[event[1]][1] += 1

            if event[0] == charges[event[1]][3]:
                charges[event[1]][2] += 100
            else:
                charges[event[1]][2] += abs(charges[event[1]][0] - event[0])
            
            charges[event[1]][0] = event[0]

    for charge in charges:
        if charges[charge][1] == 1:
            charges[charge][2] += 100

    return charges

if __name__ == '__main__':
    
    piers, cards, events = map(int, input().split())

    boat2d = []

    for _ in range(events):
        curr_event = list(map(int, input().split()))
        boat2d.append(curr_event)
    
    boatcharges = calcCharge(boat2d, cards)

    for charge in boatcharges:
        # if not at end of line
        if charge != cards:
            print(boatcharges[charge][2], end=" ")
        else:
            print(boatcharges[charge][2])