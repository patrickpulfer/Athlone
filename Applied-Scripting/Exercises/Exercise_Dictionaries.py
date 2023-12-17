from string import ascii_lowercase


dictionary = {}

def get_frequencies(filename):
    
    dictionary = {}

    with open(filename, 'r') as file:
        data = file.read().rstrip().lower()

    for character in data:
        character.lower()
        if character in dictionary:
            dictionary[character] = dictionary[character] + 1
        elif character in ascii_lowercase:
            dictionary[character] = 1
    
    return dictionary



frequencies = get_frequencies("alice.txt")
print("Letter Frequency")
for letter, frequency  in sorted(frequencies.items()):
    print(f"   {letter:<3} {frequency:>5}")

