import unittest
from main import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        # setup before every test
        self.graph = Graph()
        self.graph.makeNode("A")
        self.graph.makeNode("B")
        self.graph.linkNodes("A", "B", 5)

    def test_add_node(self):
        # check if node add works
        self.graph.makeNode("C")
        self.assertIn("C", self.graph.graphData)  # should be in graph

    def test_add_edge(self):
        # check if edge added right
        self.assertIn("B", self.graph.graphData["A"])  # should be linked
        self.assertEqual(self.graph.graphData["A"]["B"], 5)  # weight should be 5

    def test_delete_node(self):
        # remove node and check gone
        self.graph.deleteNode("B")
        self.assertNotIn("B", self.graph.graphData)  # should be removed
        self.assertNotIn("B", self.graph.graphData["A"])  # link also gone

    def test_change_weight(self):
        # test if weight change works
        self.graph.changeWeight("A", "B", 2)
        self.assertEqual(self.graph.graphData["A"]["B"], 2)  # should be 2 now

    def test_unlink_nodes(self):
        # remove edge only
        self.graph.unlinkNodes("A", "B")
        self.assertNotIn("B", self.graph.graphData["A"])  # edge should be gone

    def test_dijkstra_simple(self):
        # test shortest path A -> B -> C
        self.graph.makeNode("C")
        self.graph.linkNodes("B", "C", 2)
        result = self.graph.runDijkstra("A")
        self.assertEqual(result["C"], 7)  # 5 + 2 = 7

    def test_dijkstra_missing_node(self):
        # run dijkstra on node that not there
        result = self.graph.runDijkstra("Z")
        self.assertEqual(result, {})  # should return empty

    def test_change_weight_invalid_edge(self):
        self.graph.makeNode("C")
        self.graph.changeWeight("A", "C", 10)
        self.assertNotIn("C", self.graph.graphData["A"])  # should not create the edge

if __name__ == "__main__":
    unittest.main()
