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
        
        #On d??finit la fonction fonc qui prend en entr??e un noeud (start) et une liste de noeuds (pasacces)
        #Cette fonction renvoie le meilleur itin??aire du trajet de start ?? dest, sans passer par les noeuds de la liste pascces
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

        #On applique cette fonction fonc ?? (src, []) car au d??but, tous les noeuds sont atteignables
        res = fonc(src, [])
        puissmin = res[0]
        chemin = res[1]

        #On compare la puissance minimale pour ce trajet avec power et on renvoie le r??sultat associ?? :
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
#pour n sommets et m ar??tes



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

        #On commence par tester si self et src sont bien dans une m??me composante connexe
        #Sinon, on d??cide arbitrairement de renvoyer ([], infini)
        licomponents = self.connected_components()
        for component in licomponents:
            if src in component:
                if dest not in component:
                    return ([], float("inf"))

        #On d??finit la fonction fonc qui prend en entr??e un noeud (start) et une liste de noeuds (pasacces)
        #Cette fonction renvoie le meilleur itin??aire du trajet de start ?? dest, sans passer par les noeuds de la liste pascces
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

        #On applique cette fonction fonc ?? (src, []) car au d??but, tous les noeuds sont atteignables
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
Question 10 :
"""
import time

g_net1 = graph_from_file("input/network.1.in")

#La fonction estimation_duree prend en argument un fichier contenant des routes
#Elle estime le temps mis par la fonction min_power appliqu??e ?? l'ensemble de ces routes ?? partir des 5 premi??res
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


#La fonction est_relie prend en argument un graphe g et deux noeuds n1 et n2 
#Elle renvoie le bool??en correpondant ?? si ces deux noeuds sont reli??s dans le graphe g
def est_relie(g, n1, n2):
    licomponents = g.connected_components()
    for component in licomponents:
        if n1 in component:
            if n2 in component:
                return True
            else:
                return False
        elif n2 in component:
            if n1 in component:
                return True
            else:
                return False



#La fonction kruskal prend en argument un graphe g et renvoie l'arbre couvrant de poids minimal de g

def kruskal(g):

    g_res = Graph([])
    #On cr??e tout d'abord la liste des ar??tes de g, contenant les ar??tes sous la forme (puissance, noeud1, noeud2):
    li = []
    for i in range(1, g.nb_nodes+1):
        if len(g.graph[i]) > 0:
            for voisin in g.graph[i]:
                if voisin[0] < i:
                    li.append((voisin[1], i, voisin[0]))
    li.sort() #En triant la liste, les ar??tes sont class??es par puissance croissante

    for arete in li:
        #Pour chaque ar??te de g, si les noeuds ne sont pas d??j?? reli??s, on ajoute l'ar??te ?? g_res :
        if arete[1] not in g_res.nodes or arete[2] not in g_res.nodes or not est_relie(g_res, arete[1], arete[2]):
            g_res.add_edge(arete[1], arete[2], arete[0])

    return g_res


"""
def power_min_arbre_couvrant(arbre, n1, n2):

    if not est_relie(arbre, n1, n2):
        return ([], float("inf"))
    
    def f_rec(start, noeuds_vus):
        noeuds_vus.append(start)
        for voisin in arbre.graph[start]:
            if voisin[0] not in noeuds_vus:
                noeuds_vus.append(voisin[0])
                if voisin[0] == n2:
                    return ([voisin[0]], voisin[1])
                else:
                    x, y = f_rec(voisin[0], noeuds_vus)
                    return (x, max(voisin[1], y))
        return f_rec(noeuds_vus[len(noeuds_vus)-2], noeuds_vus)

    res1, res2 = f_rec(n1, [])

    return ([n1]+res1, res2)


    pour chaque voisin de start:
    si voisin[0] nest pas deja vu :
        noeuds_vus.append(voisin[0])
        on regarde si voisin[0] == arrivee
            si oui : on renvoie ([voisin[0]], voisin[1])
            si non :
                si f(voisin[0], noeuds_vus) == ([], 0) : on renvoie f(start, noeuds_vus)
    (si ?? ce moment l?? f ne renvoie rien, cest que start na pas de voisin pas encore vu. Alors :)
    renvoyer f()
"""
#La fonction power_min_arbre_couvrant prend en argument un arbre couvrant et deux noeuds n1 et n2 de cet arbre
#Elle renvoie le chemin de n1 ?? n2 ainsi que la puissance associ??e ?? ce chemin
#(Cette puissance est forc??ment minimale car l'arbre n'est pas cyclique)
def power_min_arbre_couvrant(arbre, n1, n2):

    #On commence par tester si arbre est bien un arbre ie que arbre est connexe (sinon on renvoie une puissance infinie)
    if not est_relie(arbre, n1, n2):
        return ([], float("inf"))
    
    #La fonction f_rec prend en argument un noeud start et une liste de noeuds noeuds_vus
    #Elle renvoie la liste correspondant au chemin de start ?? n2 sans passer par les noeuds de noeuds_vus si chemin existe
    #Si ce chemin n'existe pas, elle ne renvoie rien
    def f_rec(start, noeuds_vus):
        noeuds_vus.append(start)
        for voisin in arbre.graph[start]:
            if voisin[0] not in noeuds_vus:
                if voisin[0] == n2:
                    return ([voisin[0]], voisin[1])
                else:
                    res = f_rec(voisin[0], noeuds_vus)
                    if res != None :
                        return (res[0], max(voisin[1], res[1]))
        
    #On applique cette fonction ?? (n1, []) car au d??but tous les noeuds sont accessibles
    res1, res2 = f_rec(n1, [])

    return ([n1]+res1, res2)

