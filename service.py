from entities import Muzica, Video


class Service:
    def __init__(self):
        self.__songs = []
        # read from file / database
        # self.read_from_file()
        self.__songs.append(Muzica("Lalala", "Vicent", "pop", 3.25))
        self.__songs.append(Muzica("Dive", "Alberto", "pop", 4.1))
        self.__songs.append(Muzica("Gucci", "Abi", "trap", 3.07))

    def get_all_songs(self):
        """
        Returns the list of all songs
        :return: Returns the list of all songs
        """
        return self.__songs

    def add_song(self, new_song):
        """
        Add a song to the song list
        If the song already exist, raise a ValueError
        :param song: param to add to the list of songs (Muzica)
        """
        for song in self.__songs:
            if song == new_song:
                raise ValueError("Song already exist!")
        self.__songs.append(new_song)

    def average_duration(self):
        s = 0
        for i in range(len(self.__songs)):
            s += self.__songs[i].get_duration()
        return s / len(self.__songs)

    def delete_song(self, name):
        """
        Delete a song after name
        :param name: Name of the song who will be deleted
        :return: Nothing
        """
        position = self.__find_song_by_name(name)
        if position == -1:
            raise ValueError("The song named {0} doesn't exist in the list!".format(name))
        else:
            del self.__songs[position]

    def __find_song_by_name(self, name):
        """
        Finds the position oh the song
        :param name: Name of the song
        :return:the position where song is or -1 if the song isn't in the list(int)
        """
        for i in range(len(self.__songs)):
            if self.__songs[i].get_name() == name:
                return i
        return -1

    def most_common_gen(self):
        """
        Finds the most common gen of which songs
        :return: The gen which is most common
        """
        global gen
        max = 0
        for i in range(len(self.__songs)):
            c = 0
            genul = self.__songs[i].get_gen()
            for index in range(len(self.__songs)):
                if self.__songs[index].get_gen() == genul:
                    c += 1
            if (c > max):
                max = c
                gen = genul
        return gen

    def get_stars(self, song: Video):
        return self.__get_stars(song)
