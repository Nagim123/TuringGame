from random import randint, shuffle

from player import Player
from typing import List
from enum import Enum
from game_options import Options

import localizator

'''
This file contains all actions that can be performed during game play process
'''

class PlayerRoles(Enum) :
    """
    All game roles of a player
    """
    IMPOSTER = "Imposter"
    DETECTIVE = "Detective"
    NONE = "None" #System role (do not delete this!!!)


class GameProcess() :
    def __init__(self, players : List[Player], options : Options) -> None:
        self.players = players
        self.options = options
        self.max_turn = options.max_turns
        self.turn = 0
        self.points = {}
        self.roles = {}
        for player in self.players :
            self.points[player.chat_id] = 0
            self.roles[player.chat_id] = PlayerRoles.NONE
    
    def _is_num(self, text) :
        try :
            test = int(text)
            return True
        except :
            return False

    def wait_player_response_text(self, player : Player) -> None :
        '''
        Wait until user enters message
        '''
        content = player.read_message()
        while content == None :
            content = player.read_message()
        return content

    def wait_player_response_for_list_choice(self, player : Player, list_options : List[str], before_msg : str = None, after_msg : str = None, randomize : bool = False) -> None :
        '''
        Wait until player enters any number
        '''
        if before_msg :
            player.notify_user(before_msg)
        if randomize :
            shuffle(list_options)
        player.notify_user(self.decorate_with_delimeter(list_options, "\n-------\n"))
        if after_msg :
            player.notify_user(after_msg)
        while True :
            text = self.wait_player_response_text(player)
            if(self._is_num(text)) :
                num = int(text)
                if num > 0 or num <= len(list_options) :
                    return list_options[num-1]
                else :
                    player.notify_user(localizator.PHRASE_INDEX_ERROR_2[self.options.lang])    
            else :
                player.notify_user(localizator.PHRASE_INDEX_ERROR_1[self.options.lang])
                    

    def send_message(self, content : str, player : Player) :
        '''
        Send message to specified player
        '''
        player.notify_user(content)
    
    def send_message_all(self, content : str) :
        '''
        Send message to all players
        '''
        for player in self.players :
            player.notify_user(content)

    def decorate_with_delimeter(self, str_list : List[str], delimeter : str) :
        result = ""
        for s in str_list :
            result += s + delimeter
        return result

    def change_role(self, player : Player, role : PlayerRoles) :
        '''
        Changes role of specified player
        '''
        
        self.roles[player.chat_id] = role

    def get_players_with_role(self, role : PlayerRoles) -> List[Player] :
        '''
        Get all players with specified role
        '''
        
        matched_players = []
        for player in self.players :
            if self.roles[player.chat_id] == role :
                matched_players.append(player)
        
        return matched_players
    
    def next_turn(self) :
        '''
        Force game to the next turn
        '''
        self.turn += 1

    def increase_score(self, value : int, player : Player) :
        self.points[player.chat_id] += value

    def is_game_end(self) :
        '''
        Checks if game finished
        '''

        return self.turn >= self.max_turn

    def get_best_player(self) -> Player :
        '''
        Gets the player with the largest score
        '''

        best_player = self.players[0]
        for player in self.players :
            if self.points[player.chat_id] > self.points[best_player.chat_id] :
                best_player = player
        return best_player

    def get_random_player(self) -> Player :
        return self.players[randint(0,len(self.players)-1)]


    def generate_texts(self, fragment : str) -> List[str] :
        '''
        Generates text using AI
        '''
        return self.options.textGenerators[self.turn % len(self.options.textGenerators)].get_text(fragment, self.options.number_of_generated_texts)

    def get_moment() :
        '''
        Packs state of a game into one compact instance of a class
        '''
        pass
class GameMoment() :
    def __init__(self) -> None:
        pass