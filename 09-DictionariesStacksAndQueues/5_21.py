import json

favorite_movie = {
    "title": "Gladiator",
    "director": "Ridley Scott",
    "year": 2000,
    "genre": "Historical Drama",
    "lead_actor": "Russell Crowe"
}

file_name = "favorite_movie.json"

with open(file_name, 'w') as file:
    json.dump(favorite_movie, file, indent=4)
    print("Data has been written to", file_name)