import json
from domain.listener import Listener
from repository.in_memory_repository import InMemoryRepository

class ListenerService:
    def __init__(self, repository: InMemoryRepository):
        self.__repository = repository

        try:
            with open("data/listener.json", "r") as listener_file:
                json_f = json.load(listener_file)
                listeners_f = json_f["listeners"]
                for listener_f in listeners_f:
                    self.__repository.add(
                        Listener(listener_f["id"],
                                 listener_f["name"],
                                 listener_f["age"],
                                 listener_f["song_id"])
                    )
        except FileNotFoundError:
            print("Listeners don't found! -> listener.json doesn't exist!")

    def add_listener(self, listener):
        self.__repository.add(listener)

    def delete_listener(self, id):
        position = self.__repository.find_position(Listener(id, " ", 0, 0))
        if position == -1:
            raise ValueError("The listener does not exist!")
        self.__repository.delete(position)

    def get_all_listeners(self):
        return self.__repository.get_all()

    def update_listener(self, id, new_listener: Listener):
        position = self.__repository.find_position(Listener(id, " ", 0, 0))
        if position == -1:
            raise ValueError("The listener does not exist!")
        else:
            self.__repository.update(new_listener, position)