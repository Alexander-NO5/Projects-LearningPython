import random

def play():
  answer = 'Y'
  while answer == 'Y': 
    symbols = ['🍒',' 🍇', '🍉', '7️⃣']

    results = random.choices(symbols, k=3)

    print(f'{results[0]} | {results[1]} | {results[2]}')

    if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
      print('Jackpot! 💰')
    else:
      print('Thanks for playing!')

    answer = input('Do you want to play again? (Y/N) ')

play()
