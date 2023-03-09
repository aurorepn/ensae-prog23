from graph import Graph, graph_from_file, estimation_duree, kruskal


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

g = graph_from_file("input/network.03.in")
print(kruskal(g))