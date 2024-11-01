from functools import reduce

def pair(oksana):
    pairs = []
    for i in range(0, len(oksana) - 1, 2):
        if i >= 2:
           pairs.append((oksana[i], oksana[i+1]-oksana[i-1]))
        else:
           pairs.append((oksana[i],oksana[i+1]))
    return pairs

def distance(t):
    return t[0]*t[1] 

input = [10,1,20,2]

odometer = reduce(lambda acc,x: acc + distance(x), pair(input),0)

print(odometer) # 30