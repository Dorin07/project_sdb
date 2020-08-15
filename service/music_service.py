import json
from domain.music import Music
from repository.in_memory_repository import InMemoryRepository


class MusicService:
    def __init__(self, repository: InMemoryRepository):
        self.__repository = repository

        try:
            with open("data/music.json", "r") as music_file:
                json_f = json.load(music_file)
                music_f = json_f["music"]
                for song in music_f:
                    self.__repository.add(
                        Music(song["id"],
                                 song["name"],
                                 song["artist"],
                                 song["gen"],
                                 song["duration"])
                    )
        except FileNotFoundError:
            print("Listeners don't found! -> listener.json doesn't exist!")

    def add_song(self, song):
        self.__repository.add(song)

    def delete_song(self, id):
        position = self.__repository.find_position(Music(id, " ", " ", " ", 0.0))
        if position == -1:
            raise ValueError("The song does not exist!")
        self.__repository.delete(position)

    def get_all_songs(self):
        return self.__repository.get_all()
