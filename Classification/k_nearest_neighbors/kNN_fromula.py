from math import sqrt
import numpy as np
a = np.array([2, 2])
b = np.array([4, 4])
print(np.linalg.norm(a - b))
x = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
print(x)
neighbors = [[2.7810836, 2.550537003, 0],
             [1.465489372, 2.362125076, 0],
             [3.396561688, 4.400293529, 0],
             [1.38807019, 1.850220317, 0],
             [3.06407232, 3.005305973, 0],
             [7.627531214, 2.759262235, 1],
             [5.332441248, 2.088626775, 1],
             [6.922596716, 1.77106367, 1],
             [8.675418651, -0.242068655, 1],
             [7.673756466, 3.508563011, 1]]

output_values = [row[-1] for row in neighbors]
print(output_values)


def euclidean_distance(d1, d2):
    actual_distance = 0.0
    for i in range(len(d1)-1):
        actual_distance += (d1[i]-d2[i])**2
    return sqrt(actual_distance)


for distanceInDataset in neighbors:
    distance = euclidean_distance(neighbors[0], distanceInDataset)
    print(distance)
