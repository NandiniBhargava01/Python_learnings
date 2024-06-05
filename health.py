import random

# random.randint(a, b) Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

#inital health of a player 

health=50

print('WELCOME')

difficulty=int(input('enter the difficulty level: 1:Easy 2:medium 3:Hard \n'))

print('Let\'s have the health potion to upgrade your health')
               
potion_health=int(random.randint(25,50)/difficulty)

health=health+potion_health
print(health)
