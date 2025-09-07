# [(1,2),(3,4),(5,6),(4,3)]
# the symmetric pairs among the data is
# (4, 3)

def symmetric(data):
    se=set()
    print("the symmetric pairs among the data is")
    for (x,y) in data:
        se.add((x,y))
        if (y,x) in se:
            print((x,y))

s=input()
data=eval(s)
symmetric(data)
