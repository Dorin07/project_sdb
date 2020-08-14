from domain.listener import Listener
from repository.in_memory_repository import InMemoryRepository


class ListenerService:
    def __init__(self, repository: InMemoryRepository):
        self.__repository = repository
        self.__repository.add(Listener(1, "Dorin", 17, 2))
        self.__repository.add(Listener(2, "Tudor", 22, 1))
        self.__repository.add(Listener(3, "Vlad",  14, 3))

    def add_listener(self, listener):
        self.__repository.add(listener)

    def delete_listener(self, id):
        position = self.__repository.find_position(Listener(id, " ", 0, 0))
        if position == -1:
            raise ValueError("The song does not exist!")
        self.__repository.delete(position)

    def get_all_listeners(self):
        return self.__repository.get_all()
