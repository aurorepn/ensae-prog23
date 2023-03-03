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
    
#Ceci est un test

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
        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
    

    def get_path_with_power(self, src, dest, power):
        
        licomponents = connected_components(self)
        for component in licomponents:
            if src in component:
                if not dest in component:
                    return None
                else:
                    noeuds_atteignables = component


        #puissance = float("inf")


        #def parcours(noeud, noeuds_vus, compte):
            #noeuds_vus += [noeud]
            #for voisin in self.graph[noeud]:
                #if parcours(voisin, noeuds_vus, compte) < puissance:

                #noeud_etudie = voisin[0]
                #if

# parcours renvoie le chemin et la puissance

        #parcours(src, [], 0)

        #----------------

        #noeuds_vus = []

        #start = noeud
        #end = end
        #fonction(start, end, composantespasaccessibles) renvoie le trajet de start à end et renvoie le cout associé
        #l = liste vide
        #pour chque voisin du noeud pas encore vu
        #si voisin = arrivée -> l.append(power_min du trajet noeud/arrivee , [arrivee])
        #sinon -> on ajoute noeud a la liste des noeuds vus puis on ajoute à l : (cout obtenu par la fonction appliquee avec voisin comme depart + power_min du trajet noeud/voisin , [trajet obtenu par la fonction jusqua larrivée])
        #on regarde où est minimisée l (concernant la premiere composante des couples)
        
        #---------

        def fonc(start, end, composantespasaccessibles):
            l = []
            composantesnonaccessibles = [start]
            for voisin in self.graph[noeud]:
                if voisin[0] not in composantesnonaccessibles:
                    composantesnonaccessibles.append(voisin[0])
                    if voisin[0] == end:
                        l.append(voisin[1], [voisin[0]])
                    else:
                        longueur = len(fonction(voisin[0], end, composantespasaccessibles)[1])
                        m = [voisin[0]]*(longueur+1)
                        for i in range(longueur):
                            m[i+1] = fonction(voisin[0], end, composantespasaccessibles)[1][i]
                        l.append(voisin[1] + fonction(voisin[0], end, composantespasaccessibles)[0], m)
            n = len(l)
            puissancemin = l[0][0]
            noeudmin = 0
            for i in range(n):
                if l[i][0] < puissancemin:
                    puissancemin = l[i][0]
                    noeudmin = i
            return(puissancemin, l[i][1])

        
            



        
        


        raise NotImplementedError
    

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
        raise NotImplementedError


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