import heapq

def dijkstra(graph, start_node):
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0

    q = [(start_node, 0)]

    while q:
        current_node, current_distance = heapq.heappop(q)

        if current_distance > distances[current_node]:
            continue


        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(q, (neighbor, distance))
                    
    return distances
    

graph = {
            "A": {"B": 1, "C": 4},
            "B": {"A": 1, "C": 2, "D": 5},
            "C": {"A": 4, "B": 2, "D": 1},
            "D": {"B": 5, "C": 1},
        }

print(dijkstra(graph, "A")) #should be: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

