import telebot
from bot import MasterBot

class TelegramBot(MasterBot) :
    def __init__(self, token : str) -> None:
        self.token = token
        self.callbacks = []
        self.t_bot = telebot.TeleBot(token)
        @self.t_bot.message_handler()
        def get_message(message) :
            for callback in self.callbacks :
                callback(message.chat.id, message.text)

    def send_message(self, content : str, chat_id : int) -> None :
        self.t_bot.send_message(chat_id, content)

    def add_listener(self, callback) -> None :
        self.callbacks.append(callback)
    
    def user_name_by_chat_id(self, chat_id) -> None :
        fullname = self.t_bot.get_chat(chat_id).first_name + " " + self.t_bot.get_chat(chat_id).last_name
        return fullname

    def start_bot(self) -> None :
        self.t_bot.infinity_polling()