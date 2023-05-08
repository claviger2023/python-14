points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    k1 = 0
    distance = 0
    n = 0
    for k in coordinates:
        if n == 0:
            k1 = k
        else:
            if k > k1:
                print(points.get((k1, k)))
                distance+= points.get((k1, k))
                k1=k
            else:
                print(points.get((k, k1)))
                distance+= points.get((k, k1))
                k1=k
        
        n += 1
    return distance

print(calculate_distance([0, 1, 3, 2, 0]))
