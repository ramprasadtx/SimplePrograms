#required output (from Lowest to Highest points)
#Newcastle 18
#Spurs 25
#Leicester 26
#Liverpool 31

team_info = { 'Leicester': 26,'Liverpool': 31,'Newcastle': 18, 'Spurs': 25 }

point_list = []
for points in team_info:
    point_list.append(team_info[points])

new_point_list = (sorted(point_list))

team_info_by_points = {}
for k,v in team_info.items():
    team_info_by_points[v]=k

final_info_list = sorted(team_info_by_points)

# print('team_info_by_points '+ str(team_info_by_points))
# print('******')
# print('final_info '+ str(final_info))

for i in final_info_list:
#    if i in team_info_by_points:
    print(f'{team_info_by_points[i]} : {i}')