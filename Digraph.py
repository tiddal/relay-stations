class Digraph(object):

    def __init__(self):
        """
        Ensures: 
        self.nodes is a list of the nodes in the graph.
        self.edges is a dict mapping each node to a list of its children.

        """
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        """
        Adds the given node to the list of nodes (self.nodes) and creates a key, value pair 
        for the edges dictionary (self.edges) where the key is the given node and the value 
        is an empty list.
        Requires: node is an instance of Node.

        """
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge):
        """
        Takes the given edge and gets the source and the destination node of it as well as 
        the duration. Then appends a tuple with the destination node and the duration to it 
        to the list of nodes the source is connected to: {source: [(destination, duration)]}
        Requires: edge is an instance of Edge.

        """
        src = edge.getSource()
        dest = edge.getDestination()
        duration = edge.duration
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        if (dest, duration) not in self.edges[src]:  # Prevents repeating edges
            self.edges[src].append((dest, duration))

    def childrenOf(self, node):
        """
        Requires: node is an instance of Node and is a key of the edges dictionary.
        Ensures: A list with all the nodes the given node is connected to and the duration to 
        them.

        """
        return self.edges[node]

    def hasNode(self, node):
        """
        Requires: node is an instance of Node.
        Returns: True if the given node is in this Digraph, returns False other wise.

        """
        return node in self.nodes

    def getNodeByName(self, name):  # Added method to get a node by its name
        """
        Finds a node by its name in the Digraph.
        Requires: name is a string.
        Ensures: The node in the Digraph with the given name it it exists.

        """
        for node in self.nodes:
            if node.getName() == name:
                return node

    def __str__(self):
        """
        This method overrides the default 'str(Digraph)' method creating a string as 'Source 
        name -> Destination name, duration' for each node in the Digraph.

        """
        result = ''
        for src in self.nodes:
            for (dest, duration) in self.edges[src]:
                result += f'{src.getName()} -> {dest.getName()}, {duration}\n'
        return result
