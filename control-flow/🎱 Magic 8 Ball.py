# Magic 8 Ball

import random

question = input('Question: ')

num = random.randint(1, 9)

if num == 1:
  answear = 'Yes - definitely.'
elif num == 2:
  answear = 'It is decidedly so.'
elif num == 3:
  answear = 'Without a doubt.'
elif num == 4:
  answear = 'Reply hazy, try again.'
elif num == 5:
  answear = 'Ask again later.'
elif num == 6:
  answear = 'Better not tell you now.'
elif num == 7:
  answear = 'My sources say no.'
elif num == 8:
  answear = 'Outlook not so good.'
elif num == 9:
  answear = 'Very doubtful.'

print('Magic 8 Ball: ' + answear)
