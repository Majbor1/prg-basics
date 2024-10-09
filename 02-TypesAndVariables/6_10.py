###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# display number of characters
print('Number of characters: ', len(movie))

# display title in capital letters
print(movie.upper())

# display title in small letters
print(movie.casefold())

# display how many times the vowel "e" appears in the title
print('Number e: ', movie.count("e"))

# display where in the text is the word "Lord"
print('Index of Lord: ', movie.find("Lord"))

# display where in the text is the word "dragon"
print('Index of dragon: ', movie.find("dragon"))
