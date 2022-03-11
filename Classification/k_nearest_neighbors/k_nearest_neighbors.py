from math import sqrt


def euclidean_distance(d1, d2):
    actual_distance = 0.0
    for i in range(len(d1)-1):
        actual_distance += (d1[i]-d2[i])**2
    return sqrt(actual_distance)


def get_nearestNeighbors(testData, testRows, nearest_neighbor_value):
    distance = list()
    for test_data_rows in testData:
        euclidean_dist = euclidean_distance(testRows, test_data_rows)
        distance.append((test_data_rows, euclidean_dist))
        print(euclidean_dist)
    distance.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(nearest_neighbor_value):
        neighbors.append(distance[i][0])
    return neighbors


def predict_classification(train, test_row, num_neighbors):
    neighbors = get_nearestNeighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction


dataset = [[2.7810836, 2.550537003, 0],
           [1.465489372, 2.362125076, 0],
           [3.396561688, 4.400293529, 0],
           [1.38807019, 1.850220317, 0],
           [3.06407232, 3.005305973, 0],
           [7.627531214, 2.759262235, 1],
           [5.332441248, 2.088626775, 1],
           [6.922596716, 1.77106367, 1],
           [8.675418651, -0.242068655, 1],
           [7.673756466, 3.508563011, 1]]

intialDistance = dataset[0]
# for distanceInDataset in dataset:
#   distance = euclidean_distance(intialDistance, distanceInDataset)
#  print(distance)
# nearest_Neighbors = get_nearestNeighbors(dataset, intialDistance, 3)
# for everyNeighbor in nearest_Neighbors:
#     print(everyNeighbor)
make_prediction = predict_classification(dataset, dataset[0], 3)
print(dataset[0][-1], make_prediction)
