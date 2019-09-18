class Station:
    '''
    This is a class to creare a Station.

    Arguments:
        id {int} -- The id of the station.
        name {string} -- The name of the station.
        power {int} -- The power of the station.
        gen {int} -- The generation of the station.
        conns {list} -- A list with the ids of the stations this station is connected to.

    '''

    def __init__(self, id, name, power, gen, conns):
        '''
        The constructor for the Station class.

        Arguments:
            id {int} -- The id of the station.
            name {string} -- The name of the station.
            power {int} -- The power of the station.
            gen {int} -- The generation of the station.
            conns {list} -- A list with the ids of the stations this station is connected to.

        '''

        self._id = id
        self._name = name
        self._power = power
        self._gen = gen
        self._conns = conns

    # Getters
    @property
    def id(self):
        '''
        Gets the id of the station.

        Returns:
            int -- id of the station.

        '''

        return self._id

    @property
    def name(self):
        '''
        Gets the name of the station.

        Returns:
            string -- name of the station.

        '''

        return self._name

    @property
    def power(self):
        '''
        Gets the power of the station.

        Returns:
            int -- power of the station.

        '''

        return self._power

    @property
    def gen(self):
        '''
        Gets the gen of the station.

        Returns:
            int -- gen of the station.

        '''

        return self._gen

    @property
    def conns(self):
        '''
        Gets the list with the ids of the stations this station is connected to.

        Returns:
            list -- a list of ids.

        '''

        return self._conns

    # Setters
    @id.setter
    def id(self, id):
        '''
        Sets the id of the Station.

        Arguments:
            id {int} -- id of the Station.

        '''

        self._id = id

    @name.setter
    def name(self, name):
        '''
        Sets the name of the Station.

        Arguments:
            name {string} -- Name of the Station.

        '''

        self._name = name

    @power.setter
    def power(self, power):
        '''
        Sets the power of the Station.

        Arguments:
            power {int} -- power of the Station.

        '''

        self._power = power

    @gen.setter
    def gen(self, gen):
        '''
        Sets the generation of the Station.

        Arguments:
            gen {int} -- generation of the Station.

        '''

        self._gen = gen

    @conns.setter
    def conn(self, conns):
        '''
        Sets a a list with the ids of the stations this station is connected to.

        Arguments:
            conns {list} -- a list of ids.

        '''

        self._conns = conns

    # Overriding default methods
    def __str__(self):
        '''
        This method overrides the default 'str(Station)' method creating a string as 'id, 
        name, power, gen, (conns)'.

        Returns:
            string -- A string in 'id, name, power, gen, (conns)' format.

        '''

        return f'{self.id}, {self.name}, {self.power}, {self.gen}, ({self.conns})'.replace('[', '').replace(']', '')

    def __eq__(self, other):
        '''
        This method is used to compare this station to another object with the operator '=='.

        Arguments:
            other {Obj} -- Another object, Station is expected but not required.

        Returns:
            bool -- Returns True if the id and the name of self are equal to the id and name 
            of the other object and that object is an instance of Station. Returns False 
            otherwise.

        '''

        return (self.id == other.id) and (self.name == other.name) if isinstance(other, Station) else False

    def __lt__(self, other):
        '''
        This method is used to compare this Station to another Station with the operators '<' 
        and '>'.

        Arguments:
            other {Station} -- Another Station is requiered to compare to this (self) station.

        Returns:
            bool -- Returns True if the self's id is lower than the other stations's id. 
            Returns False otherwise.

        '''

        return self.id < other.id
