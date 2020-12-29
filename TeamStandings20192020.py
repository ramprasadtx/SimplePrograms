#Find Teamstandings from Highest to Lowest
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
number_info = {}
list=[]
for k,v in team_info.items():
    number_info[v] = k
x = sorted(number_info, reverse=True)
for i in x:
    if i in number_info:
        print(f'{number_info[i]} : {i}')