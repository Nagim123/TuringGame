from game_modes.dual_mode import DualGameMode
from game_options import Options
from text_generator import TextGenerator
from AI.prokofevich import Prokofevich

from bot import MasterBot
from bots.console_bot import ConsoleBot
from bots.vk_bot import VKBot
from bots.telegram_bot import TelegramBot

from localizator import SupportedLanguages

from game import Game

from typing import List

import json

class ConfigFile() :
    """
    Class for reading and parsing config file
    """
    def __init__(self, filepath : str) -> None:
        self._config_file = open(filepath, "r", encoding="utf-8")
        self._config_data = json.load(self._config_file)
    
    def get_games(self) -> List[Game] :
        games = []

        for game in self._config_data["games"] :
            text_generators = []
            for generator in game["AI"] :
                text_generators.append(self._get_text_generator_from_name(generator))
            found_localization = False
            for supportedLanguages in SupportedLanguages :
                if game["localization"] == supportedLanguages.value :
                    found_localization = True
                    break
            if not found_localization:
                raise Exception("Unknown localization - " + game["localization"])
            
            game_mode = None
            if game["game_mode"] == "dual" :
                game_mode = DualGameMode()
            if not game_mode :
                raise Exception("Unknown game mode - " + game["game_mode"])

            c_option = Options(game["name"], game["max_turns"], game["max_players"], text_generators,game["number_of_ai_texts"],game["passcode"], game["localization"], game_mode)
            games.append(Game(c_option))

        return games

    def get_main_bot(self) -> MasterBot :
        """
        Gives a bot depending on config file
        """
        if self._config_data["main_bot"] == "Console" :
            return ConsoleBot()
        elif self._config_data["main_bot"] == "Telegram" :
            return TelegramBot(self._config_data["token"])
        elif self._config_data["main_bot"] == "Vk" :
            return VKBot(self._config_data["token"])
        
        raise Exception("Unknown bot " + self._config_data["main_bot"])
    
    def _get_text_generator_from_name(self, generator_name : str) -> TextGenerator:
        """
        Converts name of bot to the class instance
        """
        if generator_name == "Prokofevich" :
            return Prokofevich()
        
        raise Exception("Unknown text generator - " + generator_name)
