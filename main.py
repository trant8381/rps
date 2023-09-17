import random

combinations = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}
name = input('Enter your name: ')
file = open('rating.txt', 'r')
x = file.read()
c = 0
rating = ''
for char in x.replace('\n', ' ').split():
    if c == 1:
        rating = int(char)
        break
    if char == name:
        c = 1
        continue
print(f'Hello, {name}')
n = input()
if n == '':
    m = ['rock', 'paper', 'scissors']
else:
    m = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']
commands = m + ['!exit', '!rating']
print("Okay, let's start")
while True:
    n = input()
    x = random.choice(m)
    if n not in commands:
        print('Invalid input')
    elif n == '!exit':
        print('Bye!')
        break
    elif n == '!rating':
        print(f'Your rating: {str(rating)}')
    elif n != x:
        if x in combinations[n]:
            print(f'Well done. The computer chose {x} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {x}')
    elif n == x:
        rating += 50
        print(f'There is a draw ({x})')