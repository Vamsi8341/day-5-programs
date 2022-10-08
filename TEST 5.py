def removeChar(s, c) :
    counts = s.count(c)
    s = list(s)
    while counts :
        s.remove(c)
        counts -= 1
    s = '' . join(s)
     
    print(s)
 
# Driver code
if __name__ == '__main__' :
     
    s = "1234556"
    removeChar(s,'5')
