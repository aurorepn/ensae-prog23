class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        self.nb_edges += 1

        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
    


    def get_path_with_power(self, src, dest, power):
        
        #On définit la fonction fonc qui prend en entrée un noeud (start) et une liste de noeuds (pasacces)
        #Cette fonction renvoie le meilleur itinéaire du trajet de start à dest, sans passer par les noeuds de la liste pascces
        def fonc(start, pasacces):
            l = []
            pasacces.append(start)
            for voisin in self.graph[start]:
                if voisin[0] not in pasacces:
                    if voisin[0] == dest:
                        l.append((voisin[1], [voisin[0]]))
                    else:
                        x, y = fonc(voisin[0], pasacces + [voisin[0]])
                        l.append((max(voisin[1], x), y))
            n = len(l)
            if n > 0:
                puissancemin = l[0][0]
                noeudmin = 0
                for i in range(n):
                    if l[i][0] < puissancemin:
                        puissancemin = l[i][0]
                        noeudmin = i
                return (puissancemin, [start] + l[noeudmin][1])
            else:
                return (float("inf"), [])

        #On applique cette fonction fonc à (src, []) car au début, tous les noeuds sont atteignables
        res = fonc(src, [])
        puissmin = res[0]
        chemin = res[1]

        #On compare la puissance minimale pour ce trajet avec power et on renvoie le résultat associé :
        if puissmin > power:
            return None
        else:
            return chemin



    def connected_components(self):
        licomponents = []
        noeuds_vus = {noeud:False for noeud in self.nodes}

        def parcours_profondeur(noeud):
            component = [noeud]
            for voisin in self.graph[noeud]:
                voisin = voisin[0]
                if not noeuds_vus[voisin]:
                    noeuds_vus[voisin] = True
                    component += parcours_profondeur(voisin)
            return component

        for noeud in self.nodes:
            if not noeuds_vus[noeud]:
                licomponents.append(parcours_profondeur(noeud))

        return licomponents

#cout de la fonction exploration : C(n,m) = O(1) + nb_voisins(s) * cout(exploration)
#pour n sommets et m arêtes



    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        
        return set(map(frozenset, self.connected_components()))
    


    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """

        #On commence par tester si self et src sont bien dans une même composante connexe
        #Sinon, on décide arbitrairement de renvoyer ([], infini)
        licomponents = self.connected_components()
        for component in licomponents:
            if src in component:
                if dest not in component:
                    return ([], float("inf"))

        #On définit la fonction fonc qui prend en entrée un noeud (start) et une liste de noeuds (pasacces)
        #Cette fonction renvoie le meilleur itinéaire du trajet de start à dest, sans passer par les noeuds de la liste pascces
        def fonc(start, pasacces):
            l = []
            pasacces.append(start)
            for voisin in self.graph[start]:
                if voisin[0] not in pasacces:
                    if voisin[0] == dest:
                        l.append((voisin[1], [voisin[0]]))
                    else:
                        x, y = fonc(voisin[0], pasacces + [voisin[0]])
                        l.append((max(voisin[1], x), y))
            n = len(l)
            if n > 0:
                puissancemin = l[0][0]
                noeudmin = 0
                for i in range(n):
                    if l[i][0] < puissancemin:
                        puissancemin = l[i][0]
                        noeudmin = i
                return (puissancemin, [start] + l[noeudmin][1])
            else:
                return (float("inf"), [])

        #On applique cette fonction fonc à (src, []) car au début, tous les noeuds sont atteignables
        res = fonc(src, [])
        puissmin = res[0]
        chemin = res[1]

        return (chemin, puissmin)


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename) as file:
        ligne1 = file.readline().split()
        n = int(ligne1[0])
        m = int(ligne1[1])
        noeuds = [i for i in range(1, n+1)]
        graphe = Graph(noeuds)
        for i in range(m):
            ligne = file.readline().split()
            noeud1 = int(ligne[0])
            noeud2 = int(ligne[1])
            power_min = int(ligne[2])
            if len(ligne) > 3:
                dist = int(ligne[3])
                graphe.add_edge(noeud1, noeud2, power_min, dist)
            else:
                graphe.add_edge(noeud1, noeud2, power_min)

    return graphe



"""
SEANCE 2
"""
import time

g_net1 = graph_from_file("input/network.1.in")
#La fonction estimation_duree prend en argument un fichier contenant des routes
#Elle estime le temps mis par la fonction min_power appliquée à l'ensemble de ces routes à partir des 5 premières
def estimation_duree(file_routes):
    with open(file_routes) as file:
        ligne1 = file.readline().split()
        n = int(ligne1[0])
        somme = 0
        for i in range(5):
            ligne = file.readline().split()
            n1 = int(ligne[0])
            n2 = int(ligne[1])
            t0 = time.perf_counter()
            res = g_net1.min_power(n1, n2)
            t1 = time.perf_counter()
            somme = somme + t1 - t0
    return (n * somme/5)

#Notre fonction min_power n'est pas assez optimisée, on ne peut donc pas calculer sa durée d'exécution



#La fonction sont_relies prend en argument un graphe g et deux noeuds n1 et n2 
#Elle renvoie le booléen correpondant à si ces deux noeuds sont reliés dans le graphe g
def sont_relies(g, n1, n2):

    noeuds_vus = {noeud:False for noeud in g.nodes}

    #La fonction parcours prend en argument un noeud appelé noeud
    #Elle parcours le graphe g et renvoie True si noeud et n2 sont reliés dans le graphe g et False sinon
    def parcours(noeud):
        for voisin in g.graph[noeud]:
            if voisin[0] == n2:
                return True
            if not noeuds_vus[voisin[0]]:
                noeuds_vus[voisin[0]] = True
                if parcours(voisin[0]):
                    return True
        return False

#On évalue cette fonction en n1
    return (parcours(n1))



#La fonction kruskal prend en argument un graphe g et renvoie l'arbre couvrant de poids minimal de g
def kruskal(g):

    g_res = Graph([])
    #On crée tout d'abord la liste des arêtes de g, contenant les arêtes sous la forme (puissance, noeud1, noeud2):
    li = []
    for i in range(1, g.nb_nodes+1):
        if len(g.graph[i]) > 0:
            for voisin in g.graph[i]:
                if voisin[0] < i:
                    li.append((voisin[1], i, voisin[0]))
    li.sort() #En triant la liste, les arêtes sont classées par puissance croissante
    
    #Cette première partie de la fonction kruskal est en O(n^2) où n est le nombre de noeuds.

    for arete in li:
        #Pour chaque arête de g, si les noeuds ne sont pas déjà reliés, on ajoute l'arête à g_res :
        if arete[1] not in g_res.nodes or arete[2] not in g_res.nodes or not sont_relies(g_res, arete[1], arete[2]):
            g_res.add_edge(arete[1], arete[2], arete[0])
    #Cette deuxième partie de la fonction est en O(m^2) où m est le nombre d'arêtes du graphe

    return g_res

    #La complexité de la fonction kruskal est donc en O(n^2 + m^2)



#La fonction power_min_arbre_couvrant prend en argument un arbre couvrant et deux noeuds n1 et n2 de cet arbre
#Elle renvoie le chemin de n1 à n2 ainsi que la puissance associée à ce chemin
#(Cette puissance est forcément minimale car l'arbre n'est pas cyclique)
def power_min_arbre_couvrant(arbre, n1, n2):

    #Avant tout on traite le cas particulier où le noeud de départ est le noeud d'arrivée
    if n1 == n2:
        return ([n1], 0)

    #On commence par tester si arbre est bien un arbre ie que arbre est connexe (sinon on renvoie une puissance infinie)
    if not sont_relies(arbre, n1, n2):
        return ([], float("inf"))
    #La fonction f_rec prend en argument un noeud start et une liste de noeuds noeuds_vus
    #Elle renvoie la liste correspondant au chemin de start à n2 sans passer par les noeuds de noeuds_vus si chemin existe
    #Si ce chemin n'existe pas, elle ne renvoie rien
    noeuds_vus = {noeud:False for noeud in arbre.nodes}
    def f_rec(start):
        noeuds_vus[start] = True
        for voisin in arbre.graph[start]:
            if not  noeuds_vus[voisin[0]]:
                if voisin[0] == n2:
                    return ([voisin[0]], voisin[1])
                else:
                    res = f_rec(voisin[0])
                    if len(res[0]) > 0 :
                        return ([voisin[0]] + res[0], max(voisin[1], res[1]))
        return ([], float("inf"))
        
    #On applique cette fonction à n1
    res1, res2 = f_rec(n1)

    return ([n1]+res1, res2)

#La fonction power_min_arbre_couvrant est en O(m) où m est le nombre d'arêtes de l'arbre considéré



#La fonction duree_routes prend en argument un entier x entre 1 et 10
#Elle renvoie la succession des puissances correspondant aux routes du fichier routes.x.in ainsi que la durée d'exécution du code
def duree_routes(x):
    g_net = graph_from_file("input/network." + str(x) + ".in")
    arbre_net = kruskal(g_net)
    with open("input/routes." + str(x) + ".in") as file:    
        ligne1 = file.readline().split()
        n = int(ligne1[0])
        somme = 0
        for i in range(n):
            ligne = file.readline().split()
            n1 = int(ligne[0])
            n2 = int(ligne[1])
            t0 = time.perf_counter()
            res = power_min_arbre_couvrant(arbre_net, n1, n2)
            print(res[1])
            t1 = time.perf_counter()
            somme = somme + t1 - t0
    return (somme)

#On obtient alors pour x=1 une durée d'execution de 0.0026s





"""
SEANCE 3
"""

budget = 25 * 10^9

#La fonction camions_from_file prend en argument un fichier et renvoie la liste des camions figurant sur ce fichier sous la forme (puissance, prix)
def camions_from_file(file_camion):
    with open(file_camion) as file:
        ligne1 = file.readline().split()
        n = int(ligne1[0])
        res = [(0,0)]*n
        for i in range(n):
            ligne = file.readline().split()
            power = int(ligne[0])
            prix = int(ligne[1])
            res[i] = (power, prix)
    return (res)


#La fonction routes_et_power_from_file prend en argument un entier entre 1 et 10 et renvoie la liste des routes figurant sur le fichier routes.x.in sous la forme (départ, arrivée, puissance_min, utilité)
def routes_et_power_from_file(x):
    g_net = graph_from_file("input/network." + str(x) + ".in")
    arbre_net = kruskal(g_net)
    with open("input/routes." + str(x) + ".in") as file:
        ligne1 = file.readline().split()
        n = int(ligne1[0])
        res = [(0,0,0,0)]*n
        for i in range(n):
            ligne = file.readline().split()
            n1 = int(ligne[0])
            n2 = int(ligne[1])
            power = power_min_arbre_couvrant(arbre_net, n1, n2)[1]
            profit = int(ligne[2])
            res[i] = (n1, n2, power, profit)
    return (res)










