from domain.music import Music
from repository.in_memory_repository import InMemoryRepository


class MusicService:
    def __init__(self, repository: InMemoryRepository):
        self.__repository = repository
        self.__repository.add(Music(1, "Lalala", "Y2k", "pop", 2.40))
        self.__repository.add(Music(2, "Natural", "Imagine Dragons", "pop", 3.09))
        self.__repository.add(Music(3, "Dance Monkey", "Tones And I", "pop", 3.29))

    def add_song(self, song):
        self.__repository.add(song)

    def delete_song(self, id):
        position = self.__repository.find_position(Music(id, " ", " ", " ", 0.0))
        if position == -1:
            raise ValueError("The song does not exist!")
        self.__repository.delete(position)

    def get_all_songs(self):
        return self.__repository.get_all()

    def average_duration(self):
        songs = self.__repository.get_all()
        s = 0
        for i in range(len(songs)):
            s += songs[i].get_duration()
        return s / len(songs)

    def most_common_gen(self):
        """
        Finds the most common gen of which songs
        :return: The gen which is most common
        """
        songs = self.__repository.get_all()
        global gen
        max = 0
        for i in range(len(songs)):
            c = 0
            genul = songs[i].get_gen()
            for index in range(len(songs)):
                if songs[index].get_gen() == genul:
                    c += 1
            if (c > max):
                max = c
                gen = genul
        return gen