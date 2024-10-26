# Задание №3
import requests
from collections import defaultdict
from translate import Translator
# Задание №5

class TextAnalysis():   
    
    # Задание №1
    questions = {'как тебя зовут' : "Я супер-крутой-бот и мое ппредназначение помогать тебе!",
             "сколько тебе лет" : "Это слишком философский вопрос"}
    memory = defaultdict(list)
    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        if self.text.lower() in self.questions.keys():
            self.response = self.questions[text]
        else:
            self.response = self.get_answer()

    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Задание №4
            t = Translator(from_lang=from_lang, to_lang=to_lang)
            result = t.translate(text)
            return result
        except:
            return "Перевод не удался"

