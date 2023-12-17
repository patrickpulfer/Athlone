import sys


# Variables
headers = []
state_list = []
retiring_members_list = []
retiring_date_list = []


file_name = str(input("Enter the filename: "))


# File Handling
try:
    file = open(file_name, "r")

except FileNotFoundError:
    print("Unable to open the file " + file_name) 
    sys.exit()


headers = file.readline()


for line in file.readlines():

        line = line.rstrip("\n")

        try:
            state, retiring_members, retiring_date = line.split(",")
        except ValueError:
            print(f"Line has invalid format: {line}")
            continue


        state_list.append(state)

        try:
            retiring_members_list.append(int(retiring_members))
        except ValueError:
            print(f"Invalid or missing number of members for {state}")
            continue

        retiring_date_list.append(retiring_date)


# Calculate Mean
try:
    mean = sum(retiring_members_list) / len(retiring_members_list)
except ValueError:
    print('Unable to calculate the Mean')

# Calculate Medium
try:
    sorted_list = retiring_members_list.copy()
    sorted_list.sort()
    mid_index = int(len(sorted_list)/2)
    if len(sorted_list) % 2 == 1:
        median = sorted_list[mid_index]
    else:
        median = (sorted_list[mid_index-1] + sorted_list[mid_index])/2
except ValueError:
    print('Unable to calculate the Medium')

# Calculate Mode
try:
    values = sorted(list(set(sorted_list)))
    frequencies = [ sorted_list.count(value) for value in values ]
    max_freq = max(frequencies)
    max_index = frequencies.index(max_freq)
    mode = values[max_index]
except ValueError:
    print('Unable to calculate the Mode')


print(f"Mean Members Retiring per State: {mean:.1f}")
print(f"Median Members Retiring per State: {median:.1f}")
print(f"Mode of Members Retiring per State: {mode}")


file.close()