import json
from domain.listener import Listener
from repository.in_memory_repository import InMemoryRepository


class ListenerService:
    def __init__(self, repository: InMemoryRepository):
        """
        Constructor of MusicService class
        Upload data from JSON file
        """
        self.__repository = repository

        try:
            with open("data/listener.json", "r") as listener_file:
                json_f = json.load(listener_file)
                listeners_f = json_f["listeners"]
                for listener in listeners_f:
                    self.__repository.add(
                        Listener(listener["id"],
                                 listener["name"],
                                 listener["age"],
                                 listener["song_id"])
                    )
        except FileNotFoundError:
            print("Listeners don't found! -> listener.json doesn't exist!")

    def add_listener(self, listener):
        """
        Add a listener to the list
        :param listener: The new listener
        """
        self.__repository.add(listener)

    def delete_listener(self, id):
        """
        Delete a listener after id
        :param id: Id after the listener will be delete from the list
        """
        position = self.__repository.find_position(Listener(id, " ", 0, 0))
        if position == -1:
            raise ValueError("The listener does not exist!")
        self.__repository.delete(position)

    def get_all_listeners(self):
        """
        Returns all listeners
        :return: All listeners
        """
        return self.__repository.get_all()

    def update_listener(self, id, new_listener: Listener):
        """
        Update a listener after id, and modify the json file: listener.json
        :param id: id of old listener
        :param new_listener: New listener entity
        """
        position = self.__repository.find_position(Listener(id, " ", 0, 0))
        if position == -1:
            raise ValueError("The listener does not exist!")
        else:
            self.__repository.update(new_listener, position)

        json_file = open("data/listener.json", "r")  # Open the JSON file for reading
        data = json.load(json_file)  # Read the JSON into the buffer
        listeners_f = data["listeners"]
        json_file.close()  # Close the JSON file

        # Save our changes to JSON file
        for listener in listeners_f:
            if id == listener["id"]:
                json_file = open("data/listener.json", "w+")
                listener["id"] = new_listener.get_id()
                listener["name"] = new_listener.get_name()
                listener["age"] = new_listener.get_age()
                listener["song_id"] = new_listener.get_song_id()
                json_file.write(json.dumps(data))
                json_file.close()
