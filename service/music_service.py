import json
from domain.music import Music
from repository.in_memory_repository import InMemoryRepository


class MusicService:
    def __init__(self, repository: InMemoryRepository):
        """
        Constructor of MusicService class
        Upload data from JSON file
        """
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
            print("Music don't found! -> music.json doesn't exist!")

    def add_song(self, song):
        """
        Add a song to the list
        :param song: The new song
        """
        self.__repository.add(song)

    def delete_song(self, id):
        """
        Delete a song after id
        :param id: id after the song will be delete
        """
        position = self.__repository.find_position(Music(id, " ", " ", " ", 0.0))
        if position == -1:
            raise ValueError("The song does not exist!")
        self.__repository.delete(position)

    def get_all_songs(self):
        """
        Returns all songs to the ConsoleUI
        :return: the list of all songs
        """
        return self.__repository.get_all()

    def update_song(self, id, new_song: Music):
        """
        Update a song, and modify the json file: music.json
        :param id: The id after song will be  update
        :param new_song: The new data of song
        :return: None
        """
        position = self.__repository.find_position(Music(id, " ", " ", " ", 0.0))
        if position == -1:
            raise ValueError("The song does not exist!")
        else:
            self.__repository.update(new_song, position)

        json_file = open("data/music.json", "r")  # Open the JSON file for reading
        data = json.load(json_file)  # Read the JSON into the buffer
        music_f = data["music"]
        json_file.close()  # Close the JSON file

        # Save our changes to JSON file
        for song in music_f:
            if id == song["id"]:
                json_file = open("data/music.json", "w+")
                song["id"] = new_song.get_id()
                song["name"] = new_song.get_name()
                song["artist"] = new_song.get_artist()
                song["gen"] = new_song.get_gen()
                song["duration"] = new_song.get_duration()
                json_file.write(json.dumps(data))
                json_file.close()
