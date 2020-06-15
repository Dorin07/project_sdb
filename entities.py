class Muzica:
    def __init__(self, name, artist, gen, duration):
        self.__name = name
        self.__artist = artist
        self.__gen = gen
        self.__duration = duration

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
        return "Name: {0}, Artist: {1}, Gen: {2}, Duration: {3}".format(self.__name, self.__artist, self.__gen,
                                                                        self.__duration)

    def __str__(self):
        return "Name: {0}, Artist: {1}, Gen: {2}, Duration: {3}".format(self.__name, self.__artist, self.__gen,
                                                                        self.__duration)

    def __eq__(self, other):
        """
        Verif if two songs are equals
        :param other:
        :return:
        """
        return other.get_name() == self.__name and self.__artist == other.get_artist() and self.__gen == other.get_gen() and self.__duration == other.get_duration()


class Video(Muzica):
    __stars: Muzica

    def __init__(self, name, artist, gen, duration, stars):
        super().__init__(name, artist, gen, duration)
        self.__stars = stars

    def get_stars(self):
        return self.__stars

piesa1 = Muzica("Lalala", "Vicent", "pop", 4.25)
piesa2 = Muzica("Lalala", "Vicent", "pop", 4.25)

# print(piesa1 == piesa2)
