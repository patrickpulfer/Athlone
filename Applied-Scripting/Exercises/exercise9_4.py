import re, sys

http_code_regex = 'HTTP\/1.\d"\s(\d+)'


def FileToDictionary(file_name):
    status_codes_dict = {}

    try:
        file = open(file_name, "r")

    except FileNotFoundError:
        print("Sorry file not found")
        sys.exit()

    for line in file.readlines():
        line = line.rstrip()

        http_code = re.search(http_code_regex, line).group(1)
        
        if http_code in status_codes_dict.keys():
            current_count = status_codes_dict[http_code]
            status_codes_dict.update({http_code: current_count + 1})
        else:
            status_codes_dict[http_code] = 1

    return status_codes_dict


def PrintCodeFrequencies(status_codes_dict):
    print('Code Frequency')
    for code in sorted(status_codes_dict):
        print(f"{str(code):6} {status_codes_dict[code]:>6}")


file_name = input('Enter the filename: ')
responses_dict = FileToDictionary(file_name)

PrintCodeFrequencies(responses_dict)