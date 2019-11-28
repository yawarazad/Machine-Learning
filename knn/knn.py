'''
    @author: Yawar Azad
'''
def knn(data, query, k):
    neighbor_distances_and_indices = []
    for index, example in enumerate(data):
        distance = euclidean_distance(example[:-1], query)    
        neighbor_distances_and_indices.append((distance, index))
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]
    k_nearest_labels = [data[i][1] for distance, i in k_nearest_distances_and_indices]
    kmean = sum(k_nearest_labels) / len(k_nearest_labels)
    return k_nearest_distances_and_indices , kmean

def mean(labels):
    return sum(labels) / len(labels)

def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += (point1[i] - point2[i]) ** 2
    return sum_squared_distance ** 0.5

def main():
    data = [
       [65.75, 112.99],
       [71.52, 136.49],
       [69.40, 153.03],
       [68.22, 142.34],
       [67.79, 144.30],
       [68.70, 123.30],
       [69.80, 141.49],
       [70.01, 136.46],
       [67.90, 112.37],
       [66.49, 127.45],
    ]
    
    #enter user data
    x = int(input("Enter data point to classify by knn: "))
    reg_query = [x]
    k = int(input("Enter k: "))
    reg_k_nearest_neighbors, reg_prediction = knn(data, reg_query, k=3)
    
    print(reg_prediction)

if __name__ == '__main__':
    main()