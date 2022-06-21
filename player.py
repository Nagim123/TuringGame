
from pprint import pprint
from bot import MasterBot


class Player() :
    """
    Class represents a player in a game
    """
    def __init__(self, chat_id : int, bot : MasterBot) -> None:
        self.chat_id = chat_id
        self.bot = bot
        self.is_playing = False
        self.game = None
        self._last_message = None
        self._read = False
    
    def notify_user(self, message : str) -> None:
        """
        Sends a message to user
        """
        self.bot.send_message(message ,self.chat_id)

    def provide_message(self, content : str) -> None :
        """
        Bot calls this method when user send any message
        """
        print(content)
        
        self._read = False
        self._last_message = content

    def kick_from_game(self) -> None:
        """
        Kicks a player from the current game
        """
        self.game = None
        self.is_playing = False
    
    def get_name(self) -> str :
        """
        Returns the name of player
        """
        return self.bot.user_name_by_chat_id(self.chat_id)

    def read_message(self) -> str :
        if self._last_message :
            if not self._read :
                self._read = True
                return self._last_message
        return None
