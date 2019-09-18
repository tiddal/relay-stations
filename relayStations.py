import sys
from StationCatalog import StationCatalog
from Node import Node
from Edge import Edge
from Digraph import Digraph
from copy import deepcopy
from utils import *


def main():
    """
    This function is responsible for runing the application. First stores the name of the 
    files given by the user. Then creates an instance of Digraph, initiates a StationCatalog 
    and loads it with the network file given. Then creates the Nodes and the Edges for the 
    Digraph and lastly performs the tests required by the tests file and saves the result in 
    the results file.

    """

    # Storing the name of the files
    network_file = sys.argv[1]
    tests_file = sys.argv[2]
    results_file = sys.argv[3]

    # Initiate
    digraph = Digraph()
    stations = StationCatalog()

    # Load stations
    stations.load(network_file)

    # Create Nodes
    for station in stations.catalog:
        digraph.addNode(Node(station))

    # Create Edges
    for src in digraph.nodes:
        for id in src.station.conns:
            dest = digraph.getNodeByName(stations.getStation(id).name)
            digraph.addEdge(Edge(src, dest))
            # Guarantees simetrie between connections
            digraph.addEdge(Edge(dest, src))

    # Tests
    testSet = open(tests_file, 'r')
    results = open(results_file, 'w')
    for line in testSet:
        cityA = line.strip().split(' ')[0]
        cityB = line.strip().split(' ')[1]
        graph = deepcopy(digraph)
        results.write(f'{search(graph, cityA, cityB)}\n')

    testSet.close()
    results.close()


if __name__ == '__main__':
    main()
