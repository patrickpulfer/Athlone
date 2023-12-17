# cant use  match-case

name = str(input("Enter the variable name: "))

for character in name:
    if not character.isalnum() and character != '_':
        print(f"Invalid character {character}")
        break
else:
    print('Valid variable name')