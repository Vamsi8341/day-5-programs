def lengthOfLastWord(a):
    l = 0
    x = a.strip()
 
    for i in range(len(x)):
        if x[i] == " ":
            l = 0
        else:
            l += 1
    return l
 
# Driver code
if __name__ == "__main__":
    inp = "45&29 8*6^4"
    print("The length of last word is",lengthOfLastWord(inp))
