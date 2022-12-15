alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


#automatically generate aliens in an array
aliens = []

#make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points':5, 'speed': 'slow'}
    aliens.append(new_alien)

#show the first 5 aliens
print(f"First five aliens: ")
for alien in aliens[:5]:
    print(alien)

#total num of aliens
print(f"There are {len(aliens)} aliens in the fleet, commander")

for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

i = 0
for alien in aliens:
    i+=1
    print(f"Alien number {i}: {alien}")





