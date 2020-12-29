#Find the the PremLeague champion and points
#Liverpool 99
team_info = { 'Arsenal':56,
              'Aston Villa':35,
              'Bournemouth ':34,
              'Brighton & Hove Albion':41,
              'Burnley':54,
              'Chelsea':66,
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
              'Watford':34,
              'West Ham United':39,
              'Wolverhampton Wanderers':58
              }
new_team_info = {}
for k,v in team_info.items():
    new_team_info[v] = k
for x in new_team_info:
    if x == max(new_team_info):
        print(new_team_info[x] + ''+ str(max(new_team_info)))