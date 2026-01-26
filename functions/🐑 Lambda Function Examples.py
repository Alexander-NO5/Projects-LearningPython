names = ['Anthony', 'Benedict', 'Colin', 'Daphne', 'Eloise']

filtered_names = list(filter(lambda name: name[0].upper() != 'A', names))

print(filtered_names)   # Output: ['Benedict', 'Colin', 'Daphne', 'Eloise']

#-----------------------------------------------------------------------------#

compound_word = lambda str1, str2: str1 + str2

word = compound_word('fire', 'fly')

print(f'The compound word is: {word}')
