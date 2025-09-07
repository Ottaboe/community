from talon import Module, actions

from ..user_settings import get_list_from_csv

dictionary = get_list_from_csv("bad_word_list.csv",["words"])

mod=Module()
@mod.action_class
class Actions:
    def insert_nl(text:str):
        """insertion function dutch dictation"""
        
        words=text.split()
        for i in range(len(words)):
            word=words[i]
            if word.lower() in dictionary:
                words[i]="*****"
        text=" ".join(words)


        actions.insert(text+" ")

