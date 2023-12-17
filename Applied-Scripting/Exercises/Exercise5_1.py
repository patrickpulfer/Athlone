disk_file = "lgfa.csv"

# Lists
headers = []
teams_list = []
wins_list = []
last_final_won_list = []
runner_ups_list = []
last_final_lost_list = []
total_final_appearances_list = []
win_percentage_list = []

file_name = open(disk_file, "r")
headers = file_name.readline()


for line in file_name.readlines():

    line = line.rstrip("\n")
    split_line = line.split(",")

    teams_list.append(split_line[0])
    wins_list.append(int(split_line[1]))
    last_final_won_list.append(split_line[2])
    runner_ups_list.append(int(split_line[3]))
    last_final_lost_list.append(split_line[4])
    total_final_appearances_list.append(int(split_line[5]))

    win_percentage_list.append( int( 100 * int(split_line[1]) / int(split_line[5]) ) )


average_wins = sum(wins_list) / len(teams_list)
current_winner = teams_list[last_final_won_list.index("2023")]

most_wins = max(wins_list)
most_wins_index = wins_list.index(most_wins)
most_wins_team = teams_list[most_wins_index]
most_wins_team_last_won = last_final_won_list[most_wins_index]

highest_win = max(win_percentage_list)
highest_win_index = win_percentage_list.index(highest_win)
highest_win_team = teams_list[highest_win_index]
highest_win_year = last_final_won_list[highest_win_index]

# Output
print(f"Number of Counties: {len(teams_list)}")
print(f"Total number of All-Ireland finals: {sum(wins_list)}")
print(f"Average number of wins per county: {average_wins:.1f}")
print(f"Current champions (winners in 2023): {current_winner}")
print(f"Most wins: {most_wins_team} with {most_wins} wins, most recently in {most_wins_team_last_won}")
print(f"Highest Win Ratio: {highest_win_team} with {highest_win:.0f}%, most recently in {highest_win_year}")