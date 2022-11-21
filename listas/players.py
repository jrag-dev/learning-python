"""
    Trabajando con parte de una lista
"""

# slicing de una lista

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1::-1])
print(players[2::-1])
print(players[::-1])
print(players[2:])
print(players[-3:])

"""
    Bucle a tráves de un slice
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\nHere are the first three players on my team: ")
for player in players[0:3]:
    print(player.title())