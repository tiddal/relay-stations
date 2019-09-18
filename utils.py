from copy import deepcopy


def printPath(path):
    """
    Requires: path a list of nodes

    """
    result = ''

    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def DFS(graph, start, end, time, path, path_time, fastest):
    """
    Requires:
    graph a Digraph;
    start and end nodes;
    time the time between start and end;
    path a list of nodes;
    path_time the time of the list of nodes;
    fastest is the fastest path found;
    Ensures:
    a fastest path from start to end in graph

    """
    path = path + [start]
    path_time = path_time + time

    #print('Current DFS path: ', printPath(path))
    #print('Time: ', duration(graph, path), '\n')

    if start == end:
        return path

    for node in graph.childrenOf(start):
        next_node = node[0]
        next_time = node[1]

        if next_time != 0:
            if next_node not in path:  # avoid cycles
                if fastest == None or path_time + next_time < duration(graph, fastest):
                    newPath = DFS(graph, next_node, end,
                                  next_time, path, path_time, fastest)
                    if newPath != None:
                        fastest = newPath
                elif path_time + next_time > duration(graph, fastest):
                    graph.childrenOf(start).remove(node)
        else:
            graph.childrenOf(start).remove(node)

    return fastest


def duration(graph, path):
    """
    Requires:
    graph a Digraph;
    a path
    Ensures:
    the duration of the path or None it there are nodes in the given path that do not 
    communicate.

    """
    duration = 0
    copy_path = deepcopy(path)
    try:
        for node in path:
            copy_path.remove(node)
            for child in graph.childrenOf(node):
                if child[0] in copy_path:
                    duration += child[1]

        return duration
    except:
        return None


def search(graph, start, end):
    """
    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    fastest path from start to end in graph

    """
    if graph.getNodeByName(start) == None:
        return f'{start} out of the network'
    elif graph.getNodeByName(end) == None:
        return f'{end} out of the network'

    start = graph.getNodeByName(start)
    end = graph.getNodeByName(end)

    if checkCommunication(start.station, end.station):
        result = DFS(graph, start, end, 0, [], 0, None)
        if result == None:
            return f'{start} and {end} do not communicate'
        return duration(graph, result)
    else:
        return f'{start} and {end} do not communicate'


def checkCommunication(A, B):
    """
    Requires:
    A, B are stations
    Ensures: communication between stations. Returns true if there is and false otherwise. Two stations do not communicate if one and only one of them has a 97G connection.

    """
    if (A.gen == 97 or B.gen == 97) and A.gen != B.gen:
        return False
    return True
