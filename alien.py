alien_0 = {'color': 'green', 'points':5}
points = alien_0['points']


alien_0['x_position'] = 0
alien_0['y_position'] = 25


##change value in dictionary
alien_0['color'] = 'red'
alien_0['points'] = 20


##new alien
alien_1 = {
           'x_position': 0, 
           'y_position': 25, 
           'speed':'medium', 
           'color': 'yellow', 
           'points':10
           }


print(f"Current position is [{alien_1['x_position']}, {alien_1['y_position']}]")

##move the alien to the right
##Determine how far to move the alien based on its current speed.

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    #this gon be a fast alien boi
    x_increment = 3

#the new position is the old position plus the increment
alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"New position is [{alien_1['x_position']}, {alien_1['y_position']}]")

#to remove key-value pairs
del alien_1['color']


