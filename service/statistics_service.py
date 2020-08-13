from service.music_service import MusicService


class StatisticsService:
    def __init__(self, music_service: MusicService):
        self.__music_service = music_service

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