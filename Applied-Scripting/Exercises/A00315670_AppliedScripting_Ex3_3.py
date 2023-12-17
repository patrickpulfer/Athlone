# cant use  match-case
from string import ascii_lowercase

message = str(input("Enter a message to encipher: "))
message_lowered = message.lower()
enciphered_message = ''


for character in message_lowered:

    if character.isalpha():
        character_index = ascii_lowercase.index(character)
        enciphered_character = ascii_lowercase[25 - character_index]
        enciphered_message += enciphered_character
    else:
        enciphered_message += character

print('The enciphered message is: ' + enciphered_message)