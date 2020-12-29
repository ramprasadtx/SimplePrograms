point_list = []
team_info = {'Liverpool': 31, 'Spurs': 25, 'City': 26}
for team in team_info:
    point_list.append(team_info[team])

for team2 in team_info:
    if team_info[team2] == min(point_list):
        print (f'{team2} is getting relegated from the elite division. Point_list is {point_list}')
    else:
        print(f'{team2} stay in the elite division. Point_list is {point_list}')