from imdb import IMDb
import json

ia = IMDb()
bot100 = ia.get_bottom100_movies()

movies = []
titles_list = []
directors_list = []

for i in range(0, 99):
    movie = ia.get_movie(bot100[i].movieID)
    titles_list.append(movie['title'])
    for director in movie['directors']:
        directors_list.append(director['name'])
        break
    movies.append({'Title': titles_list[i], "Directors": directors_list[i]})
    #print(movies) for debbuging 

sorted_movies = sorted(movies, key = lambda d: d['Directors'])

def write_to_json(d):
    with open('C:/path_to_file/movies.json', 'w') as file: #Used C:/ since my current system is Windows
        json.dump(d, file, indent=4)
        file.truncate()
        file.close()

write_to_json(sorted_movies)
