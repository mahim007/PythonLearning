def findMax(array):
    res = array[0]
    for item in array:
        if item > res:
            res = item
    return res


def calculateSquare(n):
    return n*n