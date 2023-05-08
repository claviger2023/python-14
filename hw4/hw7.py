points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    if len(coordinates) <= 1:
        return 0
    distance = 0
    for i in range((len(coordinates)-1)):
        print("Coor. i = ", coordinates[i], "Coor. i+1 = ", coordinates[i+1], "Distance = ", distance)
        if (coordinates[i], coordinates[i+1]) in points:
            distance += points.get((coordinates[i], coordinates[i+1]))
        if (coordinates[i+1], coordinates[i]) in points:
            distance += points.get((coordinates[i+1], coordinates[i]))
    return distance

print(calculate_distance([0, 1, 3, 2, 0]))