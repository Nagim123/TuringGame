

class Options() :
    def __init__(self,game_name : str, max_turns : int, max_players : int, textGenerators , number_of_generated_texts : int, pass_code : str, lang , game_mode ) -> None:
        self.game_name = game_name
        self.max_turns = max_turns
        self.max_players = max_players
        self.textGenerators = textGenerators
        self.pass_code = pass_code
        self.lang = lang
        self.number_of_generated_texts = number_of_generated_texts
        self.game_mode = game_mode
        