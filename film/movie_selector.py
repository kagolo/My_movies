from.models import(Movies, Subscription)

def get_movies():
    return Movies.objects.all()

def get_sub_in_movies(movie):
    return Subscription.objects.filter(movie=movie)

def get_movie(movie_id):
    return Movies.objects.get(pk=movie_id)



