from domain.listener import Listener
from domain.music import Music
from service.listener_service import ListenerService
from service.music_service import MusicService
from service.statistics_service import StatisticsService


class ConsoleUI:
    def __init__(self, music_service: MusicService, listener_service: ListenerService,  statistics_service: StatisticsService):
        """
        The constructor of the ConsoleUI class
        :param music_service: the service of the app (Service)
        """
        self.__music_service = music_service
        self.__listener_service = listener_service
        self.__statistics_service = statistics_service

    # def __valide_duration(self, duration):
    #     try:
    #         duration = int(duration)
    #     except Exception:
    #         raise ValueError("Duration of the song must be interger!")

    def __add_song(self):
        id = int(input("Enter the id of the song: "))
        name = input("Enter the name of the song: ")
        artist = input("Enter the artist of the song: ")
        gen = input("Enter the gen of the song: ")
        duration = float(input("Enter the duration of the song: "))
        self.__music_service.add_song(Music(id, name, artist, gen, duration))

    def __delete_song(self):
        id = int(input("Id of the song you want to delete: "))
        self.__music_service.delete_song(id)

    def __print_most_common(self):
        gen = self.__statistics_service.most_common_gen()
        print("The most common gen is {0}".format(gen))

    def __print_average_duration(self):
        duration = self.__statistics_service.average_duration()
        print("The average duration is {0}".format(duration))

    def __print_all_songs(self):
        songs = self.__music_service.get_all_songs()
        for i in songs:
            print(i)

    def __add_listener(self):
        id = int(input("Id of listener: "))
        name = input("Name of listener: ")
        age = int(input("Age of listener: "))
        song_id = int(input("Song-Id of favorite song: "))
        self.__listener_service.add_listener(Listener(id, name, age, song_id))

    def __print_all_listeners(self):
        listeners = self.__listener_service.get_all_listeners()
        for i in listeners:
            print(i)

    def __print_menu(self):
        print("1. Add a song")
        print("2. Remove a song after id")
        print("3. Print most common musical gen")
        print("4. Print average duration")
        print("5. Print all songs")
        print("6. Add a listener")
        print("7. Remove a listener")
        print("8. Print all listeners")
        print("0. Exit")

    def run(self):
        while True:
            self.__print_menu()
            command = input("\nEnter the command ").strip()
            try:
                if command == '0':
                    break
                elif command == '1':
                    self.__add_song()
                elif command == '2':
                    self.__delete_song()
                elif command == '3':
                    self.__print_most_common()
                elif command == '4':
                    self.__print_average_duration()
                elif command == '5':
                    self.__print_all_songs()
                elif command == '6':
                    self.__add_listener()
                elif command == '7':
                    self.__print_all_songs()
                elif command == '8':
                    self.__print_all_listeners()
                else:
                    print("Not a valid comand!")
            except Exception as ex:
                print(ex)
