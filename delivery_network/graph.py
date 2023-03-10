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
        
        #licomponents = self.connected_components()
        #for component in licomponents:
            #if src in component:
                #if dest not in component:
                    #return None
                #else:
                    #noeuds_atteignables = component
        

        def fonc(start, pasacces):
            l = []
            pasacces.append(start)
            for voisin in self.graph[start]:
                if voisin[0] not in pasacces:
                    if voisin[0] == dest:
                        l.append((voisin[1], [voisin[0]]))
                    else:
                        l.append((max(voisin[1], fonc(voisin[0], pasacces + [voisin[0]])[0]), fonc(voisin[0], pasacces + [voisin[0]])[1]))
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

        res = fonc(src, [])

        puissmin = res[0]
        chemin = res[1]

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

        licomponents = self.connected_components()
        for component in licomponents:
            if src in component:
                if dest not in component:
                    return ([], float("inf"))
                #else:
                    #noeuds_atteignables = component

        def fonc(start, pasacces):
            l = []
            pasacces.append(start)
            for voisin in self.graph[start]:
                if voisin[0] not in pasacces:
                    if voisin[0] == dest:
                        l.append((voisin[1], [voisin[0]]))
                    else:
                        l.append((max(voisin[1], fonc(voisin[0], pasacces + [voisin[0]])[0]), fonc(voisin[0], pasacces + [voisin[0]])[1]))
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




def kruskal(g):

    g_res = Graph([])

    li = []
    for i in range(1, g.nb_nodes+1):
        if len(g.graph[i]) > 0:
            for voisin in g.graph[i]:
                if voisin[0] < i:
                    li.append((voisin[1], i, voisin[0]))
    li.sort()

    for arete in li:
        if arete[1] not in g_res.nodes or arete[2] not in g_res.nodes or not est_relie(g_res, arete[1], arete[2]):
            g_res.add_edge(arete[1], arete[2], arete[0])

    return g_res

