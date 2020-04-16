import math


def information(n, y):
    print(-(n/(n+y))*math.log((n/(n+y)), 2))
    print(-(y/(n+y))*math.log((y/(n+y)), 2))
    print(-(n/(n+y))*math.log((n/(n+y)), 2)-(y/(n+y))*math.log((y/(n+y)), 2))
    return -(n/(n+y))*math.log((n/(n+y)), 2)-(y/(n+y))*math.log((y/(n+y)), 2)
