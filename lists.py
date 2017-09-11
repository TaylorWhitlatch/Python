import random

atlanta_teams = [
    'Falcons',
    'Braves',
    'Hawks',
    'Thrashers'
]

atlanta_teams.append("Atl United")
print atlanta_teams


# atlanta_teams.pop()
# print atlanta_teams.pop(random.randint(0,len(atlanta_teams)))
# print atlanta_teams

# Split turns a list into a string ... expects a delimiter

# teams_as_strings = "Falcons, Braves, Hawks, Thrashers, Atl United"
# print teams_as_strings
# teams_as_a_list = teams_as_strings.split(',')

#sort
# atlanta_teams.sort();
# print atlanta_teams
# sorted_atlanta_teams = sorted(atlanta_teams)
# print sorted_atlanta_teams
# reverse = sorted_atlanta_teams.reverse()
# print reverse

# to copy part of the list use [x:y] start at x end at y

baseball_basketball = atlanta_teams[1:3]
print baseball_basketball

all_but_the_first = atlanta_teams[1:len(atlanta_teams)]
print all_but_the_first
#remove
atlanta_teams.remove("Braves")
print atlanta_teams
#insert
atlanta_teams.insert(1,"Braves")
print atlanta_teams
