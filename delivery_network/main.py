from graph import Graph, graph_from_file, estimation_duree, kruskal, power_min_arbre_couvrant, duree_routes, sont_relies
import time

#data_path = "input/"
#file_name = "network.01.in"

#g = graph_from_file(data_path + file_name)
#print(g)

#gr = Graph([1])

#print(gr)

#gr.add_edge(2, 1, 18)

#g = graph_from_file("input/network.04.in")
#print(g.min_power(1,3))

#print(estimation_duree("input/network.01.in"))

#print(estimation_duree("input/routes.1.in"))

#g = graph_from_file("input/network.1.in")
#print(g.min_power(6,11))

"""
g = graph_from_file("input/network.04.in")
arbre = kruskal(g)
print(power_min_arbre_couvrant(arbre, 1, 2))
"""
#g = graph_from_file("input/network.1.in")
#arbre = kruskal(g)
#print(power_min_arbre_couvrant(arbre, 6, 11))


#print(duree_routes("input/routes.1.in"))
"""
t1 = time.perf_counter()
print(sont_relies(g, 8, 4))
t2 = time.perf_counter()
print(t2 - t1)
"""

#print(duree_routes2(2))
"""
g_net = graph_from_file("input/network." + str(1) + ".in")
arbre_net = kruskal(g_net)
print(arbre_net)
"""
print(duree_routes(1))