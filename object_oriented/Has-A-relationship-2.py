class SportsNews:
    def __init__(self):
        pass
    def get_sports_news(self):
        print('There is ipl today')
class MovieNews:
    def get_movie_news(self):
        print('There is kanthar movie')

class PoliticsNews:
    def get_politics_news(self):
        print('Election on march 26')
class PrajaNews:
    def __init__(self):
        self.sports=SportsNews()
        self.movie=MovieNews()
        self.politics=PoliticsNews()
    def get_whole_news(self):
        self.sports.get_sports_news()
        self.movie.get_movie_news()
        self.politics.get_politics_news()

wn=PrajaNews()
wn.get_whole_news()