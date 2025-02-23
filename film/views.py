from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# import requests

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

from django.http import HttpResponse
# from django.shortcuts import get_object_or_404



from .form import NewUserForm
from .filters import Movie_filter
from .filters import  Movie_title_filter
from .filters import Serie_filter
from .filters import Serie_title_filter
from.models import(Movies)
from.models import(Series)
from.models import(Episode)
from .movie_selector import(get_movie,get_movies)
from .category_selector import(get_category,get_categ)
from .carousel_selector import(get_carousel,get_carous)
from .serie_selector import(get_series,get_serie,get_season_in_serie,get_episode_in_season,get_season,get_episode)

# Create your views here.
# @login_required(login_url='login')
def manage_movie(request):
    get_moviys = get_movies()
    get_categorys=get_category()
    get_carousels=get_carousel()
    get_seriys=get_series()

    user_filter = Movie_filter(request.GET, queryset=get_moviys)

    get_moviy_title_filter =  Movie_title_filter(request.GET, queryset=get_moviys)

    user_series_filter = Serie_filter(request.GET, queryset=get_seriys)
    
    get_serititle_filter =  Serie_title_filter(request.GET, queryset=get_seriys)
   
   
    context={
        "user_filter":user_filter,
        "get_categorys":get_categorys,
        "get_carousels":get_carousels,
        "get_seriys":get_seriys,
        "get_moviy_title_filter":get_moviy_title_filter,
        "user_series_filter":user_series_filter,
        "get_serititle_filter":get_serititle_filter
    }
    return render (request,"index.html", context) 

# @staff_member_required(login_url='signup')
# @login_required(login_url='login')
# @user_passes_test(lambda u: u.is_staff, login_url='sub_payment')
# @user_passes_test(lambda u: u.is_superuser, login_url='sub_payment')
# @user_passes_test(lambda u: u.groups.filter(name='free').exists(),login_url='sub_payment')     
def manage_movie_detail(request,movie_id):

    movie_detail=get_movie(movie_id)
    context={
     "movie_detail":movie_detail
    }  
    return render(request,"movie_preview.html",context)


# @user_passes_test(lambda u: u.is_staff, login_url='sub_payment')
# @user_passes_test(lambda u: u.is_superuser, login_url='sub_payment')
# @user_passes_test(lambda u: u.groups.filter(name='free').exists(),login_url='sub_payment')  
def manage_episode_detail(request,episode_id):

    episode_detail=get_episode(episode_id)
    context={
     "episode_detail":episode_detail
    }  
    return render(request,"episode_preview.html",context)

# @user_passes_test(lambda u: u.is_staff, login_url='sub_payment')
# @user_passes_test(lambda u: u.is_superuser, login_url='sub_payment')
# @user_passes_test(lambda u: u.groups.filter(name='free').exists(),login_url='sub_payment')
def manage_serie_detail(request,serie_id):
    serie_detail=get_serie(serie_id)
    
    context={
        "serie_detail":serie_detail
       
    }
    return render(request,"serie_preview.html",context)
    
def manage_season_in_serie(request,serie_id):
    serie = get_serie(serie_id)
    serie_seasons = get_season_in_serie(serie)
    context={
        "serie_seasons":serie_seasons
    }

def manage_episode_in_season(request,season_id):
    season = get_season(season_id)
    episode_season = get_episode_in_season(season)
    context={
        "episode_season":episode_season
    }

def manage_search(request):
    get_moviys = get_movies()
   

    user_filter = Movie_title_filter(request.GET, queryset=get_moviys)

  
    context={
        "user_filter":user_filter,
       
    }
    return render (request,"search.html", context) 

def manage_serie_search(request):
    get_seriys=get_series()

    
    user_series_filter = Serie_title_filter(request.GET, queryset=get_seriys)

    context={
         "user_series_filter":user_series_filter
    }
    return render (request,"serie_search.html", context) 

# serie traslation status

def get_english_series(request):
    english_series_filter = Series.objects.filter(serie_translation_status = 'ENGLISH SERIE')
    context={
        "english_series_filter":english_series_filter,
    }
    return render(request, 'english_series.html', context)



# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("movie")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="register.html", context={"register_form":form})

# def login_request(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,'Invalid Credentials')
#             return redirect('login')
    
#     else:
#         return render (request,'login.html')  

def signup(request):
    form = NewUserForm()
    if request.method=="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Registered successfully'+user)
            return redirect("login")

    context={
        "form":form
    }
    return render(request, "signup.html",context)    

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('movie')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    
    else:
        return render (request,'login.html')      

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("movie")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="login.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")

def contact_me(request):
 return render(request, 'contact.html')


# Genre/catagories

def get_action(request):
    action_filter = Movies.objects.filter(movie_genre = 'SUPER ACTION')
    context={
        "action_filter":action_filter,
    }
    return render(request, 'actions_only.html', context)

def get_latest(request):
    latest_filter = Movies.objects.filter(movie_status1 = 'New Movie')
    context={
        "latest_filter":latest_filter,
    }
    return render(request, 'latest_movies.html', context)

def get_horror(request):
    horror_filter = Movies.objects.filter(movie_genre = 'HORROR THRILLER')
    context={
        "horror_filter":horror_filter,
    }
    return render(request, 'horror_only.html', context)

def get_adventure(request):
    adventure_filter = Movies.objects.filter(movie_genre = 'ADVENTURE')
    context={
        "adventure_filter":adventure_filter,
    }
    return render(request, 'adventure_only.html', context)

def get_sciefi(request):
    sciefi_filter = Movies.objects.filter(movie_genre = 'SCIENCE FRICTION')
    context={
        "sciefi_filter":sciefi_filter,
    }
    return render(request, 'science_fric_only.html', context)

def get_action_comedy(request):
    act_comedy_filter = Movies.objects.filter(movie_genre = 'ACTION COMEDY')
    context={
        "act_comedy_filter":act_comedy_filter,
    }
    return render(request, 'action_comedy_only.html', context)

def get_romantic_action(request):
    rom_action_filter = Movies.objects.filter(movie_genre = 'ROMANTIC ACTION')
    context={
        "rom_action_filter":rom_action_filter,
    }
    return render(request, 'romantic_action_only.html', context)

def get_action_detective(request):
    action_detective_filter = Movies.objects.filter(movie_genre = 'ACTION DETECTIVE')
    context={
        "action_detective_filter":action_detective_filter,
    }
    return render(request, 'action_detective_only.html', context)

def get_love_story(request):
    love_story_filter = Movies.objects.filter(movie_genre = 'LOVE STORY')
    context={
        "love_story_filter":love_story_filter,
    }
    return render(request, 'love_story_only.html', context)

def get_romantic_comedy(request):
    rom_comedy_filter = Movies.objects.filter(movie_genre = 'ROMANTIC COMEDY')
    context={
        "rom_comedy_filter":rom_comedy_filter,
    }
    return render(request, 'romantic_comedy_only.html', context)

def get_comedy(request):
    comedy_filter = Movies.objects.filter(movie_genre = 'COMEDY')
    context={
        "comedy_filter":comedy_filter,
    }
    return render(request, 'comedy_only.html', context)

def get_indian(request):
    indian_filter = Movies.objects.filter(movie_genre = 'INDIAN')
    context={
        "indian_filter":indian_filter,
    }
    return render(request, 'indian_only.html', context)

def get_animitions(request):
    animitions_filter = Movies.objects.filter(movie_genre = 'CARTOON')
    context={
        "animitions_filter":animitions_filter,
    }
    return render(request, 'animitions.html', context)

def get_family_movies(request):
    family_movies_filter = Movies.objects.filter(movie_genre = 'FAMILY MOVIE')
    context={
        "family_movies_filter":family_movies_filter,
    }
    return render(request, 'family_movies.html', context)


# vjs views

def get_english(request):
    english_filter = Movies.objects.filter(movie_VJ = 'ENGLISH')
    context={
        "english_filter":english_filter,
    }
    return render(request, 'english.html', context)

def get_vj_junior(request):
    vj_junior_filter = Movies.objects.filter(movie_VJ = 'VJ.JUNIOR')
    context={
        "vj_junior_filter":vj_junior_filter,
    }
    return render(request, 'vj_junior.html', context)

def get_vj_emmy(request):
    vj_emmy_filter = Movies.objects.filter(movie_VJ = 'VJ.EMMY')
    context={
        "vj_emmy_filter":vj_emmy_filter,
    }
    return render(request, 'vj_emmy.html', context)

def get_vj_ice_p(request):
    vj_ice_p_filter = Movies.objects.filter(movie_VJ = 'VJ.ICE.P')
    context={
        "vj_ice_p_filter":vj_ice_p_filter,
    }
    return render(request, 'vj_ice_p.html', context)

def get_vj_jingo(request):
    vj_jingo_filter = Movies.objects.filter(movie_VJ = 'VJ.JINGO')
    context={
        "vj_jingo_filter":vj_jingo_filter,
    }
    return render(request, 'vj_jingo.html', context)

def get_other_vjs(request):
    other_vjs_filter = Movies.objects.filter(movie_VJ = 'OTHER VJs')
    context={
        "other_vjs_filter":other_vjs_filter,
    }
    return render(request, 'other_vjs.html', context)



def Subscription_payment(request):
    return render(request,'success.html')


# payment

def payment(request):
    return render(request,'pay.html')

# trial

def single_movie(request,movie_id):

    sub_movie_detail=get_movie(movie_id)
    context={
     "sub_movie_detail":sub_movie_detail
    }  
    return render(request,"paid_movie.html",context)


# downloading movie video file 

def download_movie(request, movie_id):
    uploaded_file = Movies.objects.get(pk=movie_id)
    response = HttpResponse(uploaded_file.movie_video, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.movie_video.name}"'
    return response

# downloading serie video file 

def download_episode(request, episode_id):
    uploaded_epis_file = Episode.objects.get(pk=episode_id)
    response = HttpResponse(uploaded_epis_file.episode_video, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_epis_file.episode_video.name}"'
    return response


# downloading app 

def downloadapp(request):
    return render(request,'downloadapp.html')