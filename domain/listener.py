class Listener:
    def __init__(self, id, name, age, song_id):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__song_id = song_id

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_song_id(self):
        return self.__song_id

    def set_song_id(self, value):
        self.__song_id = value

    def __repr__(self):
        return "Id: {0}, Name: {1}, Age: {2}, Favorite song: {3}".format(self.__id, self.__name, self.__age, self.__song_id)

    def __str__(self):
        return "Id: {0}, Name: {1}, Age: {2}, Favorite song: {3}".format(self.__id, self.__name, self.__age, self.__song_id)

    def __eq__(self, other):
        """
        Verif if two songs are equals
        :param other:
        :return:
        """
        return other.get_id() == self.__id

