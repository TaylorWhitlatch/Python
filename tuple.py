# # Tuple is a list that:
#     # 1. values cannot be changed
#     # 2. it uses () instead of []
#
# a_tuple = (1,2,3)
# print a_tuple
#
# # Dictionaries are lists that have alpha indicies not mumerical
#
# name = "Rob"
# gender = "Male"
# height = "Tall"
#
# # A list makes no sense to tie together.
#
# person = {
#     "name": "Rob",
#     "gender": "Male",
#     "heigt": "Tall"
# }
#
# print person

zombie = {}

zombie["weapon"] = "axe"
zombie["health"] = 100
zombie["speed"] = 10

print zombie

for key,value in zombie.items():
    print "Zombie has a key of %s with a value of %s" % (key, value)
del zombie["speed"]
print zombie

is_nighttime = True
zombies = []
if(is_nighttime):
    zombie["health"] +50
zombies.append({
    'speed':15,
    'weapon':'fist',
    'name: peter'
})
zombies.append({
    'speed':25,
    'weapon':'knee',
    'name: will',
    'victims': [
        'jane',
        'bill',
        'harry'
    ]
})

print zombies[1]['victims'[1]
