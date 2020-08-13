from repository.in_memory_repository import InMemoryRepository
from service.music_service import MusicService
from service.statistics_service import StatisticsService
from ui.console_ui import ConsoleUI


if __name__ == '__main__':

    music_repository = InMemoryRepository()
    music_service = MusicService(music_repository)
    statistics_service = StatisticsService(music_service)
    console_ui = ConsoleUI(music_service, statistics_service)
    console_ui.run()
