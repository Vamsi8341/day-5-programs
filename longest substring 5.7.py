s=input("Enter the string: ")
k=int(input("Enter the integer: "))
occurance=0
l2=[]
for i in s:
    l2.append(s.count(i))

for i in range(0,len(s)):
    if l2[i]>=k:
        occurance+=1

print(occurance)
