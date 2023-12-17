from string import ascii_lowercase


def get_status_codes(filename):
    
    dictionary = {}
    
    with open(filename, 'r') as file:
        for line in file.readlines():
            column = line.split(" ")
            error_code = column[1].rstrip()

            if error_code in dictionary:
                dictionary[error_code] = dictionary[error_code] + 1
            else:
                dictionary[error_code] = 1
    
    return dictionary





"""

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
"""


status_codes_dict = get_status_codes("access_20231102.txt")
"""
print("Code", "Frequency")
for code in sorted(status_codes_dict):
    print(f"{code:6} {status_codes_dict[code]:>4}")
"""