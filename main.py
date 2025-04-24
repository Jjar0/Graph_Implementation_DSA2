import heapq

class Graph:
    def __init__(self):
        self.adjacency = {}  # {node: {neighbor: weight}}

    def add_node(self, node):
        if node not in self.adjacency:
            self.adjacency[node] = {}

    def remove_node(self, node):
        if node in self.adjacency:
            del self.adjacency[node]
        for neighbors in self.adjacency.values():
            neighbors.pop(node, None)

    def add_edge(self, from_node, to_node, weight=1):
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency[from_node][to_node] = weight

    def remove_edge(self, from_node, to_node):
        if from_node in self.adjacency:
            self.adjacency[from_node].pop(to_node, None)

    def update_edge_weight(self, from_node, to_node, new_weight):
        if from_node in self.adjacency and to_node in self.adjacency[from_node]:
            self.adjacency[from_node][to_node] = new_weight

    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.adjacency}
        distances[start_node] = 0
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.adjacency[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 1)
    g.add_edge("C", "B", 2)
    g.add_edge("B", "D", 1)
    g.add_edge("C", "D", 5)

    distances = g.dijkstra("A")
    for node, dist in distances.items():
        print(f"Distance from A to {node}: {dist}")