from entities import Muzica
from service import Service


class ConsoleUI:
    def __init__(self, service: Service):
        """
        The constructor of the ConsoleUI class
        :param service: the service of the app (Service)
        """
        self.__service = service

    # def __valide_duration(self, duration):
    #     try:
    #         duration = int(duration)
    #     except Exception:
    #         raise ValueError("Duration of the song must be interger!")

    def __add_song(self):
        name = input("Enter the name of the song: ")
        artist = input("Enter the artist of the song: ")
        gen = input("Enter the gen of the song: ")
        duration = input("Enter the duration of the song: ")
        # self.__valide_duration(duration)
        self.__service.add_song(Muzica(name, artist, gen, duration))

    def __delete_song(self):
        name = input("Name of the song you want to delete: ")
        self.__service.delete_song(name)

    def __print_most_common(self):
        gen = self.__service.most_common_gen()
        print("The most common gen is {0}".format(gen))

    def __print_average_duration(self):
        duration = self.__service.average_duration()
        print("The average duration is {0}".format(duration))

    def __print_stars(self):
        stars = self.__service.get_stars()
        print("The stars is {0}".format(stars))

    def __print_all_songs(self):
        songs = self.__service.get_all_songs()
        for i in songs:
            print(i)

    def __print_menu(self):
        print("1. Add a song")
        print("2. Remove a song after name")
        print("3. Afisarea celui mai comun gen muzical")
        print("4. Afisarea duratei medii")
        print("5. Afisarea Stelelor")
        print("6. Afisarea melodiilor")
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
                    self.__print_stars()
                elif command == '6':
                    self.__print_all_songs()
                else:
                    print("Not a valid comand!")
            except Exception as ex:
                print(ex)
