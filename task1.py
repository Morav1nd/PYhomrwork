a = input
a = str.split(a)
print(a)
b = str("а")
с2 = 0
с1 = 0
for i in range(len(a)):
    c = a[0].count(b)
    if c == a[i].count(b):
        с1 += 1
    else:
        с2 += 1
if с2 > 0:
    print("NO")
else:
    print("yes")