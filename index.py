# Advertisement:
# 
#

import os
import tkinter as tk

def select_lang():
    lang = {
        'kr': 'Korean',
        'en': 'English',
        'my': 'Malay',
        'ja': 'Japanese',
        'zh': 'Chinese'
    }
    for (key, value) in lang.items():
        print(key + ":" + value)

    raw_input = input("Select a language: ")

    if raw_input in lang:
        return raw_input
    else:
        return "na"


def add_word(lang: str, word: str, desc: str):
    with open("database/"+lang + ".txt", "a+", encoding="utf-8") as f:
        f.write(word + ":" + desc + "\n")
    print("Saved complete")

def word_desc():
    word = input("Word: ")
    desc = input("Desc: ")

    return word, desc

def add_interface():
    lang = select_lang()
    if lang == "na":
        print("Sorry the language is not supported")
        return

    word, desc = word_desc()

    add_word(lang, word, desc)
    print("passed")

def view_dict():
    lang = select_lang()

    with open("database/"+lang+".txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        print(line)


def initialise_app():
    print("""
    |=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|
    |=|             Dictionary            |=|
    |=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|
    """)
    print("1. View dictionary")
    print("2. Add Word")
    selection = input(" >> ")

    if selection == "1":
        view_dict()
    elif selection == "2":
        add_interface()
    else:
        print("The action is invalid!")

    



if __name__ == "__main__":
    for _ in range(99):
        initialise_app()