class Song:
   def __init__(self, performer, title, album, year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year

   def __str__(self):
      return f"""Performer: {self.performer}
Title: {self.title}
Album: {self.album}
Year: {self.year}
---------------------------------"""

# Creating an instance of the Car class
song1 = Song("Ed Sheeran","Hearts Don't Break Around Here","Divide",2017)
song2 = Song("Queen","Bohemian Rhapsody","A Night at the Opera",1975)

# Print the object
print(song1)  # Output: 2021 Toyota Corolla
print(song2)  # Output: 2021 Toyota Corolla
