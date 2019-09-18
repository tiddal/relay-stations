class Node(object):
    def __init__(self, station):
        """
        Requires: station is an instance of Station.

        """
        self.station = station

    def getName(self):
        """    
        Ensures: The name of the node, which is the name of the station.

        """
        return self.station.name

    def __eq__(self, other):
        """
        This method is used to compare this node to another object with the operator '=='.
        Returns: True if the station of self is equal to the station of the other object and 
        that object is an instance of Node. Returns False otherwise.

        """
        return (self.station == other.station) if isinstance(other, Node) else False

    def __hash__(self):
        """
        This method overrides the default 'hash(Node)' method creating an unique string with 
        the name of the station that this node represents.
        Ensures: An unique string with the name of the station's Node.

        """
        return hash(self.station.name)

    def __str__(self):
        """
        This method overrides the default 'str(Node)' method creating a string with the name 
        of the station that this node represents.
        Ensures: A string with the name of the station's Node.

        """
        return self.station.name
