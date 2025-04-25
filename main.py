import heapq  # Import heapq to use priority queue in dijkstra

# Graph class
class Graph:
    def __init__(self):
        self.adjacency = {}  # Dictionary to store adjacency list {node: {neighbor: weight}}

    # Add node to graph
    def addNode(self, node):
        if node not in self.adjacency:
            self.adjacency[node] = {}  # Initialize empty dictionary for neighbors

    # Remove node and edges connected to it
    def removeNode(self, node):
        if node in self.adjacency:
            del self.adjacency[node]  # Remove node from adjacency list
        for neighbors in self.adjacency.values():
            neighbors.pop(node, None)  # Remove node from other nodes neighbor lists

    # Add directed edge from one node to another with weight
    def addEdge(self, fromNode, toNode, weight=1):
        self.addNode(fromNode)  # Ensure fromNode exists
        self.addNode(toNode)    # Ensure toNode exists
        self.adjacency[fromNode][toNode] = weight  # Add or update the edge with given weight

    # Remove directed edge from one node to another
    def removeEdge(self, fromNode, toNode):
        if fromNode in self.adjacency:
            self.adjacency[fromNode].pop(toNode, None)  # Remove edge if exists

    # Update weight of existing edge
    def updateEdgeWeight(self, fromNode, toNode, newWeight):
        if fromNode in self.adjacency and toNode in self.adjacency[fromNode]:
            self.adjacency[fromNode][toNode] = newWeight  # Update edge weight

    # Run dijkstra algorithm from a node
    def dijkstra(self, startNode):
        distances = {node: float('inf') for node in self.adjacency}  # Start with infinite distances
        distances[startNode] = 0  # Distance to self is 0
        priorityQueue = [(0, startNode)]  # Priority queue with start node

        while priorityQueue:
            currentDistance, currentNode = heapq.heappop(priorityQueue)  # Get node with lowest distance

            if currentDistance > distances[currentNode]:
                continue  # Skip if already found shorter path

            # Each neighbor of the current node
            for neighbor, weight in self.adjacency[currentNode].items():
                distance = currentDistance + weight  # Find distance to neighbor through current node
                if distance < distances[neighbor]:  # If this path shorter update it
                    distances[neighbor] = distance
                    heapq.heappush(priorityQueue, (distance, neighbor))  # Add to priority queue

        return distances  # Return shortest distances from start node

# Main menu
def main():
    graph = Graph()  # Create graph

    while True:
        print("\nGraph Menu:")
        print("1. Add Node")
        print("2. Remove Node")
        print("3. Add Edge")
        print("4. Remove Edge")
        print("5. Update Edge Weight")
        print("6. Run Dijkstra's Algorithm")
        print("7. View Graph")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            node = input("Enter node name: ")
            graph.addNode(node)  # Add node
            print(f"Node '{node}' added.")

        elif choice == "2":
            node = input("Enter node name to remove: ")
            graph.removeNode(node)  # Remove node
            print(f"Node '{node}' removed.")

        elif choice == "3":
            fromNode = input("From node: ")
            toNode = input("To node: ")
            weight = int(input("Enter weight: "))
            graph.addEdge(fromNode, toNode, weight)  # Add new edge
            print(f"Edge from '{fromNode}' to '{toNode}' added with weight {weight}.")

        elif choice == "4":
            fromNode = input("From node: ")
            toNode = input("To node: ")
            graph.removeEdge(fromNode, toNode)  # Remove edge
            print(f"Edge from '{fromNode}' to '{toNode}' removed.")

        elif choice == "5":
            fromNode = input("From node: ")
            toNode = input("To node: ")
            weight = int(input("New weight: "))
            graph.updateEdgeWeight(fromNode, toNode, weight)  # Update edge weight
            print(f"Edge from '{fromNode}' to '{toNode}' updated to weight {weight}.")

        elif choice == "6":
            startNode = input("Start node for Dijkstra's algorithm: ")
            if startNode not in graph.adjacency:
                print("Start node not found in graph.")
                continue
            distances = graph.dijkstra(startNode)  # Run dijkstra
            print("Shortest distances from", startNode)
            for node, distance in distances.items():
                print(f"  {node}: {distance}")

        elif choice == "7":
            print("Graph structure:")
            for node, edges in graph.adjacency.items():
                print(f"{node} -> {edges}")  # Print adjacency list

        elif choice == "8":
            print("Exiting program.")
            break  # Exit 

        else:
            print("Invalid choice. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()