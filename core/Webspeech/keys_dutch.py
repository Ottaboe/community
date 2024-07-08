from talon import Context, Module, actions, app

from ..user_settings import get_list_from_csv


def setup_default_alphabet():
    """set up common default alphabet.

    no need to modify this here, change your alphabet using alphabet.csv"""
    initial_default_alphabet = "aap bak citroen dier ei fiets glas hoed ijs jas kast lamp mat neus oor pot quiz rok samen tak uit vos weg plex yoghurt zee".split()
    initial_letters_string = "abcdefghijklmnopqrstuvwxyz"
    initial_default_alphabet_dict = dict(
        zip(initial_default_alphabet, initial_letters_string)
    )

    return initial_default_alphabet_dict


alphabet_list = get_list_from_csv(
    "alphabet_dutch.csv", ("Letter", "Spoken Form"), setup_default_alphabet()
)