# Python3
# Language code by sTiKyt
import sys
import gettext
from Defs.Configurations import readConfig


def installGetText():
    gettext.install('Prayers', './locale')


def langRussian():
    ru = gettext.translation(
        'Prayers', localedir='./locale', languages=['ru'])
    ru.install()


def langUkrainian():
    uk = gettext.translation(
        'Prayers', localedir='./locale', languages=['uk'])
    uk.install()


def langSpanish():
    """Install Spanish Language."""
    es = gettext.translation(
        'Prayers', localedir='./locale', languages=['es'])
    es.install()


def langEnglish():
    en = gettext.translation(
        'Prayers', localedir='./locale', languages=['en'])
    en.install()


def langItalian():
    it = gettext.translation(
        'Prayers', localedir='./locale', languages=['it'])
    it.install()


def checkAndSetLanguage():
    language = readConfig().get("Settings", "Language")

    if language == "en":
        langEnglish()
    elif language == "ru":
        langRussian()
    elif language == "uk":
        langUkrainian()
    elif language == "es":
        langSpanish()
    elif language == "it":
        langItalian()
    else:
        langEnglish()


def languageSelector():
    for arg in sys.argv:
        if arg in ["--language", "--lang"]:
            for arg in sys.argv:
                if arg in ["ru", "russian", "ru_RU"]:
                    langRussian()
                elif arg in["en", "eng", "english", "en_UK", "en_US"]:
                    langEnglish()
                elif arg in["uk", "ukraine", "ukrainian", "uk_UA"]:
                    langUkrainian()
                elif arg in["es", "spain", "spanish", "es_ES"]:
                    langSpanish()
                elif arg in["it", "italia", "italiano", "it_IT"]:
                    langItalian()
        else:
            exit
