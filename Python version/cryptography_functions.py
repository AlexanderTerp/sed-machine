#------------------------------------------------------------------------------
# Original author:  Terpal47
# Creation date:    26/05/2016
# Description:      Contains the functions that generates keys and encrypts and
#                   decrypts messages.
#------------------------------------------------------------------------------

import os
from random import choice

CHARACTERS = """AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!@#$%^&*()_+.,;<>/:=|\\[]{}`~?-\'\" """

def generate_key():
    key = []
    characters_remaining = list(CHARACTERS)
    while characters_remaining:
        key.append(choice(characters_remaining))
        characters_remaining.remove(key[-1])
    return "".join(key)

def encrypt(message, key):
    encrypted = ""
    for character in message:
        index = CHARACTERS.index(character)
        encrypted += key[index]
    return encrypted

def decrypt(message, key):
    decrypted = ""
    for character in message:
        index = key.index(character)
        decrypted += CHARACTERS[index]
    return decrypted