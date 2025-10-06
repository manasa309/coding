#modulo: gives the reminder
score = 5 % 3  #output: 2 5/3=1 r=2
score = 5 % 1  #output: 0

#exponents: power 
score = 2**4  #2x2x2x2=16

# MAGIC BOX
import random as r

q = input('Question: ')

answers = [
    "Yes - definitely.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

ans = r.choice(answers)
print(ans)


# logistic and conditional operators
height = int(input('height (in cm): '))
credits = int(input('credits: '))

if height >= 137 and credits >= 10:
  print('enjoy yout ride!!!')
elif height < 137 and credits >= 10:
  print('your not tall enough...')
elif height >= 137 and credits < 10:
  print('you dont have enough credits...')
else:
  print('you dont meet requirements')


#HOGWARTS
g = 0
r = 0
h = 0
s = 0

print('WELCOME TO HOGWARTS!')

q1 = int(input('Q1) Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk\n'))
q2 =int(input('Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n'))
q3 = int(input('Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n'))

if q1==1:
  g=g+1 
  r=g+1
elif q1==2:
  h=h+1 
  s=s+1
else:
  print('wrong input')

if q2==1:
  h=h+2
elif q2==2: 
  s=s+2
elif q2==2:
  r=r+2
elif q2==4:
  g=g+2
else:
  print('wrong input')

if q3==1:
  h=h+4
elif q3==2:
  s=s+4
elif q3==2:
  r=r+4
elif q3==4:
  g=g+4
else:
  print('wrong input')

print(f'Gryffindor: {g}')
print(f'Ravenclaw: {r}')
print(f'Hufflepuff: {h}')
print(f'Slytherin: {s}')

# RATING
rating = float(input('rate(1-5): '))

if rating > 4.5:
  print('Extraordinary')
elif rating > 4:
  print('Excellent')
elif rating > 3:
  print('good')
elif rating > 2:
  print('Fair')
else:
  print('poor')


# RANDOM.RANDINT

import random as r

num = r.randint(1,5)
if num == 0:
  print('Flamingos turn pink from eating shrimp.')
elif num == 1:
  print('The only food that doesn\'t spoil is honey.')
elif num == 2:
  print('Shrimp can only swim backwards.')
elif num == 3:
  print('A taste bud\'s life span is about 10 days.')
elif num == 4:
  print('It is impossible to sneeze while sleeping.')
elif num == 5:
  print('It is illegal to sing off-key in North Carolina.')


# WEATHER
month = int(input('which month is it: '))

if month in [1,2,3]:
  print('winter')
elif month in [4,5,6]:
  print('spring')
elif month in [7,8,9]:
  print('summer')
elif month in [10,11,12]:
  print('autum')
else:
  print('invaild')