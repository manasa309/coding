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