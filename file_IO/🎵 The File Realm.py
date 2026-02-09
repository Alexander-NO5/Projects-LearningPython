# Define a dictionary to store liked songs with their artists
liked_songs = {
  'Praf de stele': 'Vita de vie',
  'Doua limbi' : 'Generatia 99',
  'Fiecare eu' : 'Smiley x Alex Velea x Connect-R',
  'End of Beginning' : 'Djo',
  'Nebun de alb' : 'Emeric Imre'
}

# Function to display and write liked songs to a file
def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write('Liked Songs:\n')
        for song, artist in liked_songs.items():
            file.write(f'{song} - {artist}\n')

# Write liked songs to a .txt file
write_liked_songs_to_file(liked_songs, 'liked_songs.txt')
