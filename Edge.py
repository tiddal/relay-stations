class Edge(object):
    def __init__(self, src, dest):
        """
        Requires: src and dst are instances of nodes.

        """
        self.src = src
        self.dest = dest
        self.duration = self.calculateDuration()

    def getSource(self):
        """
        Ensures: The source node of the edge.

        """
        return self.src

    def getDestination(self):
        """
        Ensures: The destination node of the edge.

        """
        return self.dest

    # Added method to calculate the duration of the edge.
    def calculateDuration(self):
        """
        Calculates the duration from the source of the edge to its destination.
        A station using 97G can only communicate to a station using 97G as well.
        Ensures: The duration from the source of the edge to its destination.

        """
        A = self.src.station
        B = self.dest.station
        if (A.gen == 97 or B.gen == 97) and A.gen != B.gen:
            # One and only one station is using 97G
            return 0
        elif A.gen+B.gen == 198:
            # Both stations are using 99G since 99+99 = 198
            return 1/A.power
        elif A.gen+B.gen == 194:
            # Both stations are using 97G since 97+97 = 194
            return 4*(1/A.power)
        else:
            # At least one of the Stations is using 98G
            return 2*(1/A.power)

    def __str__(self):
        """
        This method overrides the default 'str(Edge)' method creating a string as 'Source 
        name -> Destination name, duration'.

        """
        return f'{self.src.getName()}->{self.dest.getName()}, duration: {self.duration}'
