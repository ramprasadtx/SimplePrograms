#Find the 3 teams that will be relegated with points
team_info = { 'Arsenal':56,
              'Aston Villa':35,
              'Bournemouth ':34,
              'Brighton & Hove Albion':41,
              'Burnley':54,
              'Chelsea':64,
              'Crystal Palace':43,
              'Everton':49,
              'Leicester City':62,
              'Liverpool ':99,
              'Manchester City':81,
              'Manchester United':66,
              'Newcastle United':44,
              'Norwich City ':21,
              'Sheffield United':54,
              'Southampton':52,
              'Tottenham Hotspur':59,
              'Watford':33,
              'West Ham United':39,
              'Wolverhampton Wanderers':58
              }
number_info_dict = {}
list=[]
for k,v in team_info.items():
    number_info_dict[v] = k
sorted_info_list = sorted(number_info_dict, reverse=True)
for n in sorted_info_list:
    if n < sorted_info_list[-4]:
        list.append(n)
for i in list:
    if i in number_info_dict:
       print(f'Sorry!! {number_info_dict[i]} is relegated with {i} points. See you in EFL. Cheery Bye!')