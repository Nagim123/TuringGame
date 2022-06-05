import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from bot import MasterBot

class VKBot(MasterBot) :
    def __init__(self, token : str) -> None:
        self.token = token
        self.callbacks = []
        self.vk = vk_api.VkApi(token=token)
        self.longpoll = VkLongPoll(self.vk)

    def send_message(self, content : str, chat_id : int) -> None :
        self.vk.method("messages.send", {"user_id": chat_id, "message": content, "random_id": vk_api.utils.get_random_id()})
    
    def add_listener(self, callback) -> None :
        self.callbacks.append(callback)
    
    def user_name_by_chat_id(self, chat_id) -> None :
        user = self.vk.method("users.get", {"user_ids": chat_id})
        fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
        return fullname

    def start_bot(self) -> None :
        for event in self.longpoll.listen() :
            if event.type == VkEventType.MESSAGE_NEW and event.to_me :
                for callback in self.callbacks :
                    callback(event.user_id, event.text)