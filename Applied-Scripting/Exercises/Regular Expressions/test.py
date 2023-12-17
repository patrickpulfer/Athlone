import re

regex = '[0-9]{7}[A-Z]{2}'

def CheckPPSNumber(text : str):
    match = re.fullmatch(regex, text)

    if match:
        return('Valid PPS Number')
    else:
        return('Not a valid PPS Number')
    

while True:
    text = input('Enter the PPS Number or q to quit: ')
    if text == 'q':
        break
    else:
        result = CheckPPSNumber(text)
        print(result)