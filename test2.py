# # Sample dictionary
# data = {
#     'd': [
#         {'i': {'height': 1000, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BMjU5YjMwNDgtNTA0NS00ZjIxLWFiNmUtMGI5NmY0ZjkzZDgyXkEyXkFqcGdeQXVyMTk2ODc0MjY@._V1_.jpg', 'width': 675},
#          'id': '/imdbpicks/hispanic-heritage-month', 'l': 'IMDb Picks - Hispanic Heritage Month',
#          's': 'A Celebration of Hispanic and Latino Stories and Storytellers'},
#         {'i': {'height': 1929,
#               'imageUrl': 'https://m.media-amazon.com/images/M/MV5BMzI0NmVkMjEtYmY4MS00ZDMxLTlkZmEtMzU4MDQxYTMzMjU2XkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_.jpg',
#               'width': 1299},
#          'id': 'tt9362722', 'l': 'Spider-Man: Across the Spider-Verse', 'q': 'feature', 'qid': 'movie', 'rank': 70,
#          's': 'Shameik Moore, Hailee Steinfeld', 'y': 2023},
#         # ... other entries ...
#     ],
#     'q': 'spider-man',
#     'v': 1
# }
data={'d': [{'i': {'height': 1000, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BMjU5YjMwNDgtNTA0NS00ZjIxLWFiNmUtMGI5NmY0ZjkzZDgyXkEyXkFqcGdeQXVyMTk2ODc0MjY@._V1_.jpg', 'width': 675}, 'id': '/imdbpicks/hispanic-heritage-month', 'l': 'IMDb Picks - Hispanic Heritage Month', 's': 'A Celebration of Hispanic and Latino Stories and Storytellers'}, {'i': {'height': 1929, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BMzI0NmVkMjEtYmY4MS00ZDMxLTlkZmEtMzU4MDQxYTMzMjU2XkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_.jpg', 'width': 1299}, 'id': 'tt9362722', 'l': 'Spider-Man: Across the Spider-Verse', 'q': 'feature', 'qid': 'movie', 'rank': 70, 's': 'Shameik Moore, Hailee Steinfeld', 'y': 2023}, {'i': {'height': 755, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BZDEyN2NhMjgtMjdhNi00MmNlLWE5YTgtZGE4MzNjMTRlMGEwXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_.jpg', 'width': 511}, 'id': 'tt0145487', 'l': 'Spider-Man', 'q': 'feature', 'qid': 'movie', 'rank': 724, 's': 'Tobey Maguire, Kirsten Dunst', 'y': 2002}, {'i': {'height': 2048, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BMjMwNDkxMTgzOF5BMl5BanBnXkFtZTgwNTkwNTQ3NjM@._V1_.jpg', 'width': 1381}, 'id': 'tt4633694', 'l': 'Spider-Man: Into the Spider-Verse', 'q': 'feature', 'qid': 'movie', 'rank': 568, 's': 'Shameik Moore, Jake Johnson', 'y': 2018}, {'i': {'height': 4000, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_.jpg', 'width': 2699}, 'id': 'tt10872600', 'l': 'Spider-Man: No Way Home', 'q': 'feature', 'qid': 'movie', 'rank': 429, 's': 'Tom Holland, Zendaya', 'y': 2021}, {'i': {'height': 1024, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_.jpg', 'width': 674}, 'id': 'tt2250912', 'l': 'Spider-Man: Homecoming', 'q': 'feature', 'qid': 'movie', 'rank': 1725, 's': 'Tom Holland, Michael Keaton', 'y': 2017}, {'i': {'height': 1240, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BYWJlNThmNWMtZWE5Zi00YWJiLWJiOTQtZWY1Y2I3ZmNhMDYwXkEyXkFqcGdeQXVyMTk2OTAzNTI@._V1_.jpg', 'width': 840}, 'id': 'tt16360004', 'l': 'Spider-Man: Beyond the Spider-Verse', 'q': 'feature', 'qid': 'movie', 'rank': 2155, 's': 'Shameik Moore, Hailee Steinfeld'}, {'i': {'height': 1115, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BYTk3MDljOWQtNGI2My00OTEzLTlhYjQtOTQ4ODM2MzUwY2IwXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_.jpg', 'width': 750}, 'id': 'tt0413300', 'l': 'Spider-Man 3', 'q': 'feature', 'qid': 'movie', 'rank': 2017, 's': 'Tobey Maguire, Kirsten Dunst', 'y': 2007}], 'q': 'spider-man', 'v': 1}

# Movie name to search for
movie_name = input()

# Find the entry with the given movie name
movie_entry = None
for entry in data['d']:
    if entry.get('l') == movie_name:
        movie_entry = entry
        break

# Extract and print the image URL if the movie is found
if movie_entry:
    image_url = movie_entry['i']['imageUrl']
    print('Image URL for', movie_name, ':', image_url)
else:
    print('Movie', movie_name, 'not found in the dictionary')
