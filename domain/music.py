class Music:

    def __init__(self, id, name, artist, gen, duration):
        self.__name = name
        self.__artist = artist
        self.__gen = gen
        self.__duration = duration
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id(self):
        self.__id = id

    def get_name(self):
        return self.__name

    def get_artist(self):
        return self.__artist

    def get_gen(self):
        return self.__gen

    def get_duration(self):
        return self.__duration

    def set_name(self, name):
        self.__name = name

    def set_artist(self, artist):
        self.__artist = artist

    def set_gen(self, gen):
        self.__gen = gen

    def set_duration(self, duration):
        self.__duration = duration

    def __repr__(self):
        return "Id: {0}, Name: {1}, Artist: {2}, Gen: {3}, Duration: {4}".format(self.__id, self.__name, self.__artist,
                                                                                 self.__gen,
                                                                                 self.__duration)

    def __str__(self):
        return "Id: {0}, Name: {1}, Artist: {2}, Gen: {3}, Duration: {4}".format(self.__id, self.__name, self.__artist,
                                                                                 self.__gen,
                                                                                 self.__duration)

    def __eq__(self, other):
        """
        Verif if two songs are equals
        :param other:
        :return:
        """
        return other.get_id() == self.__id
