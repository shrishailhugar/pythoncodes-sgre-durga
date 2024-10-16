class Movie:
    def __init__(self,movie,hero,heroine):
        self.movie=movie
        self.hero=hero
        self.heroine=heroine

    def info(self):
         return (f'the movie is {self.movie} where {self.hero} and {self.heroine} acted as hero and heroine')


list_movies=[]

while True:
    movie,hero,heroine=input("enter movie name,hero,heorine").split()
    movie_obj=Movie(movie,hero,heroine)
    list_movies.append(movie_obj)
    user_mood=input('Enter NO to stop adding movies.')
    if user_mood.lower()=='no':
        break
for movie in list_movies:
    print(movie.info())