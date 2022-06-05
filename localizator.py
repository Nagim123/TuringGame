from enum import Enum

class SupportedLanguages(Enum) :
    RUSSIA = "russia"
    ENGLISH = "english"


PHRASE_GAME_START = {"russia":"Игра началась!", "english":"The game has begun!"}
PHRASE_ASK_FOR_FRAGMENT = {"russia":"Отправьте начало предложения, которое в последствии дополнит второй игрок.","english":"Send the beginning of the sentence, which the second player will later complete."}
PHRASE_ASK_FOR_FRAGMENT_WAITING = {"russia":"Ожидайте пока второй игрок придумывает для вас часть предложения.","english":"Wait while the second player comes up with part of the sentence for you."}
PHRASE_ASK_FOR_COMPLETE_TEXT = {"russia":"Продолжите начало предложения так, чтобы его не возможно было отличить от предложенных ИИ вариантов.\nНачало предложения (Обязательно скопируйте его в начало вашего сообщения): ", "english":"Continue the beginning of the sentence in such a way that it cannot be distinguished from the AI-suggested text options.\nBeginning of the sentence(Be sure to copy it to the beginning of your message): "}
PHRASE_ASK_FOR_COMPLETE_TEXT_WAITING = {"russia":"Подождите пока второй игрок придумает полный текст.", "english":"Wait for the second player to come up with the full text."}
PHRASE_ASK_FOR_GUESS = {"russia":"Угадайте предложение написанное человеком.","english":"Guess the sentence written by the human."}
PHRASE_ASK_FOR_GUESS_WAITING = {"russia":"Ожидайте пока другой игрок пытаятся определить ваш текст.","english":"Wait while the other player tries to recognize your text."}
PHRASE_SUCCESS = {"russia":"Вы отгадали! + 1 очко", "english":"You guessed it! + 1 point"}
PHRASE_UNSUCCESS = {"russia":"Вы ошиблись.", "english":"It's wrong!"}
PHRASE_SUCCESS_HIDE = {"russia": "Ваш текст не угадан!", "english":"Your text was NOT recognized!"}
PHRASE_UNSUCCESS_HIDE = {"russia": "Ваш текст угадан :(", "english":"Your text was recognized :("}
PHRASE_ROUND_ENDS = {"russia":"Раунд окончен. Роли поменялись.", "english": "The round is over. The roles have been reversed"}
PHRASE_GAME_WINNER = {"russia": "Игра окончена! Победитель - ", "english":"The game is over! Winner -"}
PHRASE_GAME_DRAW = {"russia":"Игра окончена! Оба игрока набрали одинаковое кол-во очков. Ничья.", "english":"The game is over! Both players scored the same number of points. Draw."}
PHRASE_INDEX_ERROR = {"russia":"Ошибка индекса", "english": "Index error"}