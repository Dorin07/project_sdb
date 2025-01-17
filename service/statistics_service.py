from service.music_service import MusicService
from service.listener_service import ListenerService


class StatisticsService:
    def __init__(self, music_service: MusicService, listener_service: ListenerService):
        self.__music_service = music_service
        self.__listener_service = listener_service

    def average_duration(self):
        """
        Calculate the average duration of all songs
        :return: The average duration
        """
        songs = self.__music_service.get_all_songs()
        s = 0
        for i in range(len(songs)):
            s += songs[i].get_duration()
        return s / len(songs)

    def most_common_gen(self):
        """
        Finds the most common gen of all songs
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
        """
        Calculate the average age of all listeners
        :return: The average age of all listeners
        """
        listeners = self.__listener_service.get_all_listeners()
        sum = 0
        for i in range(len(listeners)):
            sum += listeners[i].get_age()
        return sum / len(listeners)

    def count_all_songs(self):
        """
        Count the songs who does't have any listeners
        :return: The number of songs
        """
        listeners = self.__listener_service.get_all_listeners()
        contor = 0
        for i in range(len(listeners)):
            if listeners[i].get_song_id() == -1:
                contor += 1
        return contor

    def print_all_songs_without_listener(self):
        """
        Print all songs who does't have any listener
        :return: A new list, only with songs without a listener
        """
        songs = self.__music_service.get_all_songs()
        listeners = self.__listener_service.get_all_listeners()
        list_id = []
        new_list = []
        for i in range(len(listeners)):
            if listeners[i].get_song_id() != -1:
                list_id.append(listeners[i].get_song_id())
        for i in range(len(songs)):
            sem = 0
            for j in range(len(list_id)):
                if songs[i].get_id() == list_id[j]:
                    sem = 1
            if sem == 0:
                new_list.append(songs[i])
        return new_list

    def most_common_artist(self):
        """
        Finds the most common artist of all songs
        :return: The artist which is most common
        """
        songs = self.__music_service.get_all_songs()
        global artist
        max = 0
        for i in range(len(songs)):
            c = 0
            the_artist = songs[i].get_artist()
            for index in range(len(songs)):
                if songs[index].get_artist() == the_artist:
                    c += 1
            if (c > max):
                max = c
                artist = the_artist
        return artist

    def the_older_listener(self):
        """
        Finds the oldest listener
        :return: The name of oldest listener
        """
        listeners = self.__listener_service.get_all_listeners()
        max_age = 0
        for i in range(len(listeners)):
            if listeners[i].get_age() > max_age:
                max_age = listeners[i].get_age()
                name = listeners[i].get_name()
        return name

    def the_younger_listener(self):
        """
        Finds the younger listener
        :return: The name of younger listener
        """
        listeners = self.__listener_service.get_all_listeners()
        min_age = 256
        for i in range(len(listeners)):
            if listeners[i].get_age() < min_age:
                min_age = listeners[i].get_age()
                name = listeners[i].get_name()
        return name

