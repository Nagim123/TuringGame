from bot import MasterBot

class ConsoleBot(MasterBot) :
    def __init__(self) -> None:
        self.callbacks = []
    
    def send_message(self, content : str, chat_id : int) -> None :
        print("Message to " + str(chat_id) + ": " + content)
    def add_listener(self, callback) -> None :
        self.callbacks.append(callback)
    def start_bot(self) -> None :
        while True :
            self._wait_for_input()
    
    def user_name_by_chat_id(self, chat_id) -> None :
        if chat_id % 2 == 0:
            return "Ivan"
        return "Boris"
    
    def _wait_for_input(self) -> None :
        content = input()
        parsed_content = content.split(":")
        try :
            chat_id = int(parsed_content[0])
            text = parsed_content[1]
        except :
            print("Console bot supports only the following format: [id]:[message]")
            return
        
        for callback in self.callbacks :
            callback(chat_id, text)