
def maxWidth(tilelist):
    width = tilelist[0] * 2

    if tilelist[2] < 2:
        return width

    width += tilelist[1] * 2

    if tilelist[2] == 2:
        width += 3

    else:
        width += 3
        corners_remaining = tilelist[2] - 2

        if corners_remaining % 2 != 0:
            corners_remaining -= 1

        width += corners_remaining * 2 - (corners_remaining // 2)

    return width


if __name__ == "__main__":

    tilelist = list(map(int, input().split()))

    print(maxWidth(tilelist))