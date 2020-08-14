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
