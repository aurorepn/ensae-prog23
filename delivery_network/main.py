from graph import Graph, graph_from_file, estimation_duree, kruskal, power_min_arbre_couvrant


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

g = graph_from_file("input/network.04.in")
arbre = kruskal(g)
print(power_min_arbre_couvrant(arbre, 1, 2))

g0 = graph_from_file("input/network.00.in")
arbre0 = kruskal(g0)
print(power_min_arbre_couvrant(arbre0, 1, 4))
