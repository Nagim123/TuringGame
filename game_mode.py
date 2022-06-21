from game_options import Options
from game_process import GameProcess
import threading


class GameMode() :
    """
    Parent class for any game mode
    """
    def __init__(self) :
        #Why we need this stupid бюрокритческие принципы
        pass
    
    def start_game(self, g_process : GameProcess, options : Options) -> None :
        self.process = g_process
        self.options = options
        t = threading.Thread(target=self._main)
        t.start()
    
    def _main() :
        pass