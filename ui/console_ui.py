from domain.listener import Listener
from domain.music import Music
from service.listener_service import ListenerService
from service.music_service import MusicService
from service.statistics_service import StatisticsService


class ConsoleUI:
    def __init__(self, music_service: MusicService, listener_service: ListenerService,  statistics_service: StatisticsService):
        """
        The constructor of the ConsoleUI class
        :param music_service: the service of the music entity service
        :param listener_service: the service of the listener entity service
        :param statistics_service: the service of statistics
        """
        self.__music_service = music_service
        self.__listener_service = listener_service
        self.__statistics_service = statistics_service

    def __add_song(self):
        """
        Add a new song on the list
        """
        id = int(input("Enter the id of the song: "))
        name = input("Enter the name of the song: ")
        artist = input("Enter the artist of the song: ")
        gen = input("Enter the gen of the song: ")
        duration = float(input("Enter the duration of the song: "))
        self.__music_service.add_song(Music(id, name, artist, gen, duration))

    def __delete_song(self):
        """
        Delete a song of the list after id
        """
        id = int(input("Id of the song you want to delete: "))
        self.__music_service.delete_song(id)

    def __print_most_common(self):
        """
        Print most common gen of music on the list
        """
        gen = self.__statistics_service.most_common_gen()
        print("The most common gen is {0}".format(gen))

    def __print_average_duration(self):
        """
        Print average duration of all song on the list
        """
        duration = self.__statistics_service.average_duration()
        print("The average duration is {0}".format(duration))

    def __print_all_songs(self):
        """
        Print all songs on the list
        """
        songs = self.__music_service.get_all_songs()
        for i in songs:
            print(i)

    def __add_listener(self):
        """
        Add a new listener on the list
        """
        id = int(input("Id of listener: "))
        name = input("Name of listener: ")
        age = int(input("Age of listener: "))
        song_id = int(input("Song-Id of favorite song: "))
        self.__listener_service.add_listener(Listener(id, name, age, song_id))

    def __print_all_listeners(self):
        """
        Print all listeners
        """
        listeners = self.__listener_service.get_all_listeners()
        for i in listeners:
            print(i)

    def __delete_listener(self):
        """
        Delete a listener after id
        """
        id = int(input("Id of the listener you want to delete: "))
        self.__listener_service.delete_listener(id)

    def __update_song(self):
        """
        Update a song after id
        """
        id = int(input("Id of the song you want to edit: "))
        new_id = int(input("Enter the new id of the song: "))
        name = input("Enter the new name of the song: ")
        artist = input("Enter the new artist of the song: ")
        gen = input("Enter the new gen of the song: ")
        duration = float(input("Enter the new duration of the song: "))
        self.__music_service.update_song(id, Music(new_id, name, artist, gen, duration))

    def __update_listener(self):
        """
        Update a listener after id
        """
        id = int(input("Id of listener you want to edit: "))
        new_id = int(input("Enter the new id of listener: "))
        name = input("Enter the new name of listener: ")
        age = int(input("Enter the new age of listener: "))
        song_id = int(input("Enter the new song-id of favorite song: "))
        self.__listener_service.update_listener(id, Listener(new_id, name, age, song_id))

    def __print_average_age(self):
        age = self.__statistics_service.average_age()
        print("The average age of all listeners is {0}".format(age))

    def __print_all_songs_without_listener(self):
        contor = self.__statistics_service.count_print_songs()
        print("The number of songs without a listener is {0}".format(contor))

    def __print_menu(self):
        print("1. Add a song")
        print("2. Remove a song after id")
        print("3. Print most common musical gen")
        print("4. Print average duration")
        print("5. Print all songs")
        print("6. Add a listener")
        print("7. Remove a listener")
        print("8. Print all listeners")
        print("9. Update a song")
        print("10. Update a listener")
        print("11. Average age of listeners")
        print("12. Number of song without a listener")
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
                    self.__delete_listener()
                elif command == '8':
                    self.__print_all_listeners()
                elif command == '9':
                    self.__update_song()
                elif command == '10':
                    self.__update_listener()
                elif command == '11':
                    self.__print_average_age()
                elif command == '12':
                    self.__print_all_songs_without_listener()
                else:
                    print("Not a valid comand!")
            except Exception as ex:
                print(ex)



