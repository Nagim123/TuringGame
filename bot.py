from abc import ABCMeta, abstractmethod

class MasterBot() :
    """
    Abstract class for any bot
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def send_message(self, content : str, chat_id : int) -> None :
        """
        Sends message to user
        """

    @abstractmethod
    def add_listener(self, callback) -> None :
        """
        Adds callback to call when user sends a message
        """
    
    @abstractmethod
    def user_name_by_chat_id(self, chat_id) -> None :
        """
        Provides the name of user by chat id
        """

    @abstractmethod
    def start_bot(self) -> None :
        """
        Start event loop of the bot
        """