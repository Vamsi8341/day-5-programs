def getMinSquares(n):
    if n <= 3:
        return n;
    res = n
    for x in range(1, n + 1):
        temp = x * x;
        if temp > n:
            break
        else:
            res = min(res, 1 + getMinSquares(n
                                  - temp))
     
    return res;
 
# Driver code
print(getMinSquares(12))
print(getMinSquares(13))
print(getMinSquares(1))
print(getMinSquares(4))
print(getMinSquares(3))
