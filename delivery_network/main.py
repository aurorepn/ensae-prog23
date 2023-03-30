from graph import Graph, graph_from_file, estimation_duree, kruskal, power_min_arbre_couvrant, duree_routes, sont_relies, routes_et_power_from_file, routes_from_file, trajets_realisables_opt1, trajets_realisables_opt2, camions_from_file, cout_des_routes
import time

from graph import camions_from_file, brute_force, sac_a_dos
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
#print(duree_routes(1))

camions = camions_from_file('input/trucks.0.in')

#li = cout_des_routes(1, camions)
li = [((6, 11), 200000, 9664), ((16, 13), 200000, 6872)]
budget = 5000000

#print((brute_force(budget, li)[1]))

#[((6, 11), 200000, 9664), ((16, 13), 200000, 6872), ((10, 3), 200000, 9498), ((2, 17), 200000, 4510), ((14, 1), 200000, 7383), ((20, 15), 200000, 8072), ((10, 1), 
# 200000, 5856), ((15, 5), 200000, 1350), ((4, 15), 200000, 5314), ((19, 3), 200000, 1890), ((3, 12), 200000, 7970), ((15, 12), 200000, 9619), ((15, 7), 200000, 5494),
# ((19, 4), 200000, 3120), ((2, 18), 200000, 3982), ((3, 11), 200000, 266), ((8, 14), 200000, 4441), ((9, 15), 200000, 1920), ((16, 17), 200000, 3613), ((19, 7), 200000, 6096),
# ((6, 20), 200000, 2794), ((15, 8), 200000, 5449), ((10, 12), 200000, 6982), ((12, 6), 200000, 1019), ((10, 10), 200000, 1649), ((14, 17), 200000, 2398), ((7, 18), 200000, 3585),
# ((9, 3), 200000, 742), ((19, 4), 200000, 9403), ((16, 15), 200000, 8753), ((14, 2), 200000, 9866), ((1, 16), 200000, 1213), ((19, 5), 200000, 438), ((20, 16), 200000, 2039),
# ((6, 7), 200000, 3089), ((13, 12), 200000, 9935), ((3, 7), 200000, 9437), ((3, 11), 200000, 1962), ((17, 9), 200000, 6410), ((7, 8), 200000, 1500), ((10, 3), 200000, 6065),
# ((16, 8), 200000, 1902), ((13, 9), 200000, 597), ((13, 8), 200000, 9921), ((9, 1), 200000, 355), ((18, 15), 200000, 3189), ((14, 17), 200000, 3031), ((2, 3), 200000, 2030),
# ((5, 7), 200000, 7852), ((17, 15), 200000, 3451), ((15, 11), 200000, 1001), ((20, 1), 200000, 374), ((19, 6), 200000, 8917), ((12, 12), 200000, 6974), ((1, 17), 200000, 1663),
# ((3, 2), 200000, 4259), ((12, 11), 200000, 1147), ((1, 14), 200000, 3619), ((8, 2), 200000, 1180), ((19, 18), 200000, 4933), ((10, 15), 200000, 5740), ((2, 16), 200000, 7145),
# ((9, 14), 200000, 2955), ((2, 17), 200000, 1001), ((10, 20), 200000, 8252), ((6, 20), 200000, 7654), ((9, 12), 200000, 646), ((9, 6), 200000, 9773), ((7, 4), 200000, 1654),
# ((13, 18), 200000, 6411), ((13, 14), 200000, 3267), ((8, 10), 200000, 4263), ((5, 4), 200000, 5875), ((14, 13), 200000, 7705), ((15, 12), 200000, 9336), ((11, 11), 200000, 2776),
# ((8, 15), 200000, 3333), ((6, 16), 200000, 952), ((8, 17), 200000, 2593), ((13, 12), 200000, 2654), ((17, 12), 200000, 5609), ((15, 7), 200000, 8675), ((16, 14), 200000, 4108),
# ((8, 15), 200000, 1921), ((4, 5), 200000, 9778), ((9, 19), 200000, 7247), ((7, 15), 200000, 2865), ((15, 17), 200000, 217), ((7, 5), 200000, 7728), ((18, 5), 200000, 6716),
# ((14, 7), 200000, 9325), ((14, 15), 200000, 8333), ((14, 4), 200000, 5103), ((18, 19), 200000, 5852), ((20, 4), 200000, 6368), ((18, 13), 200000, 4112), ((20, 17), 200000, 2514),
# ((7, 15), 200000, 9185), ((12, 12), 200000, 204), ((20, 3), 200000, 7504), ((11, 1), 200000, 1296), ((8, 13), 200000, 5504), ((20, 4), 200000, 749), ((17, 15), 200000, 8919),
# ((3, 6), 200000, 4602), ((8, 15), 200000, 2210), ((5, 2), 200000, 3935), ((18, 11), 200000, 7895), ((1, 9), 200000, 5771), ((11, 6), 200000, 9997), ((3, 12), 200000, 4717),
# ((9, 4), 200000, 5886), ((4, 19), 200000, 9672), ((14, 19), 200000, 2169), ((1, 11), 200000, 5084), ((14, 3), 200000, 6358), ((6, 6), 200000, 6790), ((2, 9), 200000, 1323),
# ((17, 12), 200000, 25), ((2, 7), 200000, 9742), ((6, 9), 200000, 3151), ((20, 14), 200000, 5479), ((10, 18), 200000, 2623), ((20, 6), 200000, 3923), ((20, 1), 200000, 3656),
# ((20, 18), 200000, 7343), ((7, 9), 200000, 6204), ((2, 8), 200000, 9309), ((16, 13), 200000, 6790), ((5, 4), 200000, 517), ((11, 9), 200000, 6591), ((8, 17), 200000, 9298),
# ((12, 6), 200000, 6853), ((1, 18), 200000, 767), ((11, 16), 200000, 2715), ((20, 12), 200000, 7297), ((15, 18), 200000, 1047), ((11, 4), 200000, 4248), ((18, 5), 200000, 2584),
# ((20, 12), 200000, 7314)]

print(sac_a_dos(budget, li))


