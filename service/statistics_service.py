from service.music_service import MusicService
from service.listener_service import ListenerService


class StatisticsService:
    def __init__(self, music_service: MusicService, listener_service: ListenerService):
        self.__music_service = music_service
        self.__listener_service = listener_service

    def average_duration(self):
        songs = self.__music_service.get_all_songs()
        s = 0
        for i in range(len(songs)):
            s += songs[i].get_duration()
        return s / len(songs)

    def most_common_gen(self):
        """
        Finds the most common gen of which songs
        :return: The gen which is most common
        """
        songs = self.__music_service.get_all_songs()
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

    def average_age(self):
        listeners = self.__listener_service.get_all_listeners()
        sum = 0
        for i in range(len(listeners)):
            sum += listeners[i].get_age()
        return sum / len(listeners)

    def count_print_songs(self):
        songs = self.__music_service.get_all_songs()
        listeners = self.__listener_service.get_all_listeners()
        contor = 0
        for i in range(len(listeners)):
            if listeners[i].get_song_id() == -1:
                contor += 1
        return contor
