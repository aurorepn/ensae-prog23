import sys 
sys.path.append("delivery_network")

from graph import graph_from_file, kruskal, power_min_arbre_couvrant
import unittest   # The test framework

class Test_MinPower(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        arbre = kruskal(g)
        self.assertEqual(power_min_arbre_couvrant(arbre, 1, 4)[1], 11)
        self.assertEqual(power_min_arbre_couvrant(arbre, 2, 4)[1], 10)

    def test_network1(self):
        g = graph_from_file("input/network.04.in")
        arbre = kruskal(g)
        self.assertEqual(power_min_arbre_couvrant(arbre, 1, 4)[1], 4)

if __name__ == '__main__':
    unittest.main()