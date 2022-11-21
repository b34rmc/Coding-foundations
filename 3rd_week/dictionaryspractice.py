nfl_teams = {
    'Baylor' : 'bears',
    'Iowa' : 'Cyclones',
    'Texas' : 'Longhorns'
}

title = '***** NFL Teams *****'
intro_list = nfl_teams.items()

print(title)

for city, team in intro_list:
    print(city, team)

while True:
    ui = input('\nwhat would you like to do? \n(A)dd a new team\n (R)emove a team\n (Q)uit\n')
    if ui.upper() == 'A':
        tl = input('\nteam location: ')
        tm = input('\nteam mascot: ')
        nfl_teams[tl.title()] = tm.title()
    elif ui.upper() == 'R':
        while True:
            team_remove = input('\nwhich team would you like to remove?\n')
            if team_remove.title() not in nfl_teams.keys():
                print('enter team name:')
            else:
                break
        del nfl_teams[team_remove.title()]
    elif ui.upper() == 'Q':
        print('\n goodbye')
        break
    else:
        print('invalid response')
        
    print(f'\n{title}')
    for city, team in intro_list:
        print(city, team)