from Station import Station


class StationCatalog(Station):
    '''
    This is a class to create a Station catalog or a collection of stations.

    Keyword Arguments:
        catalog {list} -- A list that should contain instances of Station. (default: {[]})

    '''

    def __init__(self, catalog=[]):
        '''
        The constructor for the StationCatalog class.

        Keyword Arguments:
            catalog {list} -- A list that should contain instances of Station (default: {[]})

        '''

        self._catalog = catalog

    # Getters
    @property
    def catalog(self):
        '''
        Gets the stations catalog.

        Returns:
            list -- The stations catalog.

        '''

        return self._catalog

    def getStation(self, id):
        '''
        Gets a station by its id.

        Arguments:
            id {int} -- The id of a station.

        Returns:
            Station -- The station with the respective id.

        '''

        return self.asdict()[id]

    # Setters
    @catalog.setter
    def catalog(self, catalog):
        '''
        Sets the stations catalog.

        Arguments:
            catalog {list} -- A list with instances of Station.

        '''

        self._catalog = catalog

    # Methods
    def add(self, station):
        '''
        This method adds a station to the stations catalog.

        Arguments:
            station {Station} -- station should be an instance of Station.

        '''

        self.catalog.append(station)

    def asdict(self):
        '''
        This method creates a dictionary representation of the catalog.

        Returns:
            dict -- A dictionary in '{station_id: station}' format.

        '''

        d = {}
        for station in self.catalog:
            d[station.id] = station
        return d

    def load(self, file_name):
        '''
        This method loads a catalog from a file. Takes the first line and then creates an 
        instance of Station for each line in the file and appends it to the catalog. 

        Arguments:
            file_name {string} -- The name of the file to be laoded.

        '''

        with open(file_name) as f:
            next(f)
            for line in f:
                id, name, power, gen = line.split(', (')[0].split(', ')
                conns = line.split(
                    ', (')[1].strip().replace(')', '').split(', ')
                self.add(Station(int(id), name, int(
                    power), int(gen), map(int, conns)))

    # Overriding default methods
    def __str__(self):
        '''
        This method overrides the default 'str(StationCatalog)' method creating a string as 
        '['id, station_name, power, gen, (conns)', ...]'.

        Returns:
            string -- A string in the format described above with every station in the 
            catalog.

        '''

        return f'{list(map(str, self.catalog))}'
