import heapq  # Import heapq to use priority queue in dijkstra

# Graph class
class Graph:
    def __init__(self):
        self.graphData = {}  # Dictionary to store adjacency list

    # Add node to graph
    def makeNode(self, node):
        if node not in self.graphData:
            self.graphData[node] = {}  # Init empty dictionary for neighbors

    # Remove node and edges
    def deleteNode(self, node):
        if node in self.graphData:
            del self.graphData[node]  # Remove node from adjacency list
        for neighbors in self.graphData.values():
            neighbors.pop(node, None)  # Remove node from other nodes neighbor lists

    # Add directed edge between nodes with weight
    def linkNodes(self, fromNode, toNode, weight=1):
        self.makeNode(fromNode)  # Check fromNode exists
        self.makeNode(toNode)    # Check toNode exists
        self.graphData[fromNode][toNode] = weight  # Update the edge with given weight

    # Remove directed edge from one node to another
    def unlinkNodes(self, fromNode, toNode):
        if fromNode in self.graphData:
            self.graphData[fromNode].pop(toNode, None)  # Remove edge if exists

    # Update weight of existing edge
    def changeWeight(self, fromNode, toNode, newWeight):
        if fromNode in self.graphData and toNode in self.graphData[fromNode]:
            self.graphData[fromNode][toNode] = newWeight  # Update edge weight

    # Run dijkstra from a node
    def runDijkstra(self, startNode):
        distances = {node: float('inf') for node in self.graphData}  # Start with infinite distances
        distances[startNode] = 0  # Distance to self is 0
        pq = [(0, startNode)]  # Priority queue with start node

        while pq:
            currDist, currNode = heapq.heappop(pq)  # Get node with lowest distance

            if currDist > distances[currNode]:
                continue  # Skip if already found shorter path

            # Each neighbor of the current node
            for neighbor, weight in self.graphData[currNode].items():
                newDist = currDist + weight  # Find distance to neighbor through current node
                if newDist < distances[neighbor]:  # If this path shorter update it
                    distances[neighbor] = newDist
                    heapq.heappush(pq, (newDist, neighbor))  # Add to priority queue

        return distances  # Return shortest distances from start node

# Main menu
def main():
    g = Graph()  # Create graph

    while True:
        print("\n--== Graph Menu ==--")
        print("[1] Add Node")
        print("[2] Remove Node")
        print("[3] Add Edge")
        print("[4] Remove Edge")
        print("[5] Update Edge Weight")
        print("[6] Run Dijkstra's Algorithm")
        print("[7] View Graph")
        print("[8] Exit")

        choice = input("[1-8]> ")

        if choice == "1":
            node = input("[Enter node name]> ").strip()
            if node == "":
                print("Node name cannot be empty.")
                continue
            g.makeNode(node)  # Add node
            print(f"Node '{node}' added.")

        elif choice == "2":
            node = input("[Enter node name to remove]> ").strip()
            if node not in g.graphData:
                print(f"Node '{node}' not found.")
                continue
            g.deleteNode(node)  # Remove node
            print(f"Node '{node}' removed.")

        elif choice == "3":
            fromNode = input("[From node]> ").strip()
            toNode = input("[To node]> ").strip()
            if fromNode == "" or toNode == "":
                print("Node names cannot be empty.")
                continue
            try:
                weight = int(input("[Enter weight]> ")) # Make sure weight is positive number
                if weight < 0:
                    raise ValueError
            except ValueError:
                print("Weight must be a positive integer.")
                continue
            g.linkNodes(fromNode, toNode, weight)  # Add new edge
            print(f"Edge from '{fromNode}' to '{toNode}' added with weight {weight}.")

        elif choice == "4":
            fromNode = input("[From node]> ").strip()
            toNode = input("[To node]> ").strip()
            if fromNode not in g.graphData: # Check if node is in graph
                print(f"Node '{fromNode}' not found.")
                continue
            if toNode not in g.graphData[fromNode]:
                print(f"Edge from '{fromNode}' to '{toNode}' not found.")
                continue
            g.unlinkNodes(fromNode, toNode)  # Remove edge
            print(f"Edge from '{fromNode}' to '{toNode}' removed.")

        elif choice == "5":
            fromNode = input("[From node]> ").strip()
            toNode = input("[To node]> ").strip()
            if fromNode not in g.graphData or toNode not in g.graphData[fromNode]:
                print(f"Edge from '{fromNode}' to '{toNode}' does not exist.")
                continue
            try:
                weight = int(input("[New weight]> "))
                if weight < 0:
                    raise ValueError
            except ValueError:
                print("Weight must be a non-negative integer.")
                continue
            g.changeWeight(fromNode, toNode, weight)  # Update edge weight
            print(f"Edge from '{fromNode}' to '{toNode}' updated to {weight}.")

        elif choice == "6":
            startNode = input("[Start node for Dijkstra's algorithm]> ").strip()
            if startNode not in g.graphData:
                print("Start node not found")
                continue
            distances = g.runDijkstra(startNode)  # Run dijkstra
            print(f"Shortest distances from {startNode}:")
            for node, distance in distances.items():
                print(f"  {node}: {distance}")

        elif choice == "7":
            print("[Graph structure]:")
            if not g.graphData:
                print("Graph is empty.")
            for node, edges in g.graphData.items():
                print(f"{node} -> {edges}")  # Print adjacency list

        elif choice == "8":
            print("[Exiting program]")
            break  # Exit 

        else:
            print("Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()

