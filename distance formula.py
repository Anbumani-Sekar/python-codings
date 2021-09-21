import math
def distance(x1,x2,y1,y2):
    dist=math.sqrt((x2-x1)**2+(y1-y2)**2)
    return dist
dist=distance(2,4,6,8)
print(dist)
