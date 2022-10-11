s1 = input()
s2 = input()
p = int(input())
s = ""
for i in range(0,p-1):
    s = s + s1[i]
s = s + s2
for i in range(p-1,len(s1)):
    s = s + s1[i]
print(s)