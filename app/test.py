import requests

def image(name):
    url = "https://online-movie-database.p.rapidapi.com/auto-complete"
    # movie=input("Enter : ")
    querystring = {"q":f"{name}"}
    headers = {
    	"X-RapidAPI-Key": "bbe73ef5aamsh0f75fe09e0f4d99p19bca7jsn7b79608943c5",
    	"X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    movie_name = name


    movie_entry = None
    for entry in data['d']:
        if entry.get('l') == movie_name:
            movie_entry = entry
            break

    if movie_entry:
        image_url = movie_entry['i']['imageUrl']
        print(image_url)
    else:
        print('Movie', movie_name, 'not found in the dictionary')


