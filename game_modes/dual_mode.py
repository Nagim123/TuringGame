from game_mode import GameMode
from game_process import PlayerRoles
import localizator

class DualGameMode(GameMode) :
    """
    Game mode for only two players!
    """
    def _main(self) :
        game = self.process
        lang = self.options.lang

        #Get player 1
        player1 = game.get_random_player()

        while not game.is_game_end() :
            
            #Make player 1 detective
            game.change_role(player1, PlayerRoles.DETECTIVE)
            
            #Get player 2
            player2 = game.get_players_with_role(PlayerRoles.NONE)[0]
            #Make player 2 imposter
            game.change_role(player2, PlayerRoles.IMPOSTER)

            #Announce start of a game
            game.send_message_all(localizator.PHRASE_GAME_START[lang])

            game.send_message(localizator.PHRASE_ASK_FOR_FRAGMENT[lang], player1)

            game.send_message(localizator.PHRASE_ASK_FOR_FRAGMENT_WAITING[lang], player2)

            #Get fragment from detective player
            fragement = game.wait_player_response_text(player1)

            #Generate some variants of full text
            texts = game.generate_texts(fragement)

            game.send_message(game.decorate_with_delimeter(texts, "\n-------\n"), player2)
            game.send_message(localizator.PHRASE_ASK_FOR_COMPLETE_TEXT[lang], player2)

            game.send_message(localizator.PHRASE_ASK_FOR_COMPLETE_TEXT_WAITING[lang], player1)

            full_text = game.wait_player_response_text(player2)
            game.send_message(localizator.PHRASE_ASK_FOR_GUESS_WAITING[lang], player2)

            texts.append(full_text)

            
            guessed_text = game.wait_player_response_for_list_choice(player1, texts, after_msg=localizator.PHRASE_ASK_FOR_GUESS[lang])

            if guessed_text == full_text :
                game.increase_score(1, player1)
                game.send_message(localizator.PHRASE_SUCCESS[lang], player1)
                game.send_message(localizator.PHRASE_UNSUCCESS_HIDE[lang], player2)
            else :
                game.send_message(localizator.PHRASE_UNSUCCESS[lang], player1)
                game.send_message(localizator.PHRASE_SUCCESS_HIDE[lang, player2])

            game.next_turn()
            #Remove roles and swap players
            game.change_role(player1, PlayerRoles.NONE)
            game.change_role(player2, PlayerRoles.NONE)
            player1, player2 = player2, player1
        
        winner_name = game.get_best_player().get_name()
