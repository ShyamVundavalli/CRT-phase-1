d={
    1:"A1",
    2:"A2",
    3:"A3",
    4:"A4",
    "101":"A5"}
d[1]="A7"
d[6]="SIX"
print(d[3])
for i in d:
    print(i)
for i in d.values():
    print(i)
for i,j in d.items():
    print(i,j)
d.pop(3)
print(d)
