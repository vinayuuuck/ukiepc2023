
def whowins(player1arr, player2arr):
    timercount = 0
    player1arr[0] -= player2arr[1]
    player2arr[0] -= player1arr[1]
    timercount += 0.5

    while player1arr[0] > 0 and player2arr[0] > 0:

        if (timercount+0.5) % player1arr[2] == 0:
            player2arr[0] -= player1arr[1]

        if (timercount+0.5) % player2arr[2] == 0:
            player1arr[0] -= player2arr[1]

        timercount += 1

    if player1arr[0] <= 0 and player2arr[0] <= 0:
        return "draw"
    elif player1arr[0] == 0:
        return "player two"
    else:
        return "player one"


if __name__ == "__main__":

    player1arr = list(map(int, input().split()))
    player2arr = list(map(int, input().split()))

    print(whowins(player1arr, player2arr))