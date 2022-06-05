from game import Lobby
from config_parser import ConfigFile

config = ConfigFile("config.json")
main_bot = config.get_main_bot()

lobby = Lobby(main_bot, config.get_games())

main_bot.start_bot()