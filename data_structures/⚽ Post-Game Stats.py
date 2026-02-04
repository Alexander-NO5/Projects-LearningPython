barcelona_players = [
  {'name': 'Lamine Yamal', 'position': 'Right Winger', 'age': 18, 'shirt_number': 29, 'appearences': 29, 'goals' : 14, 'minutes_played' : 2413},
  {'name': 'Raphinha', 'position': 'Left Winger', 'age': 29, 'shirt_number': 24, 'appearences': 22, 'goals' : 13, 'minutes_played' : 1409},
  {'name': 'Robert Lewandowski', 'position': 'Centre-Forward', 'age': 37, 'shirt_number': 30, 'appearences': 27, 'goals' : 12, 'minutes_played' : 1414}
]

print('Positions in dictionary list:', ", ".join(player['position'] for player in barcelona_players))

barcelona_players[0]['goals'] = 18

print(f"{barcelona_players[0]['name']} updated number of golas is {barcelona_players[0]['goals']}")

print(f"The average number of goals is {(barcelona_players[0]['goals'] + barcelona_players[1]['goals'] + barcelona_players[2]['goals']) / len(barcelona_players)}\n"
      f"The average of minutes played is {(barcelona_players[0]['minutes_played'] + barcelona_players[1]['minutes_played'] + barcelona_players[2]['minutes_played']) / len(barcelona_players)}"
      )
