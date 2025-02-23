from django.urls import path
from . import views


urlpatterns = [
    path('',views.manage_movie,name="movie"),
    path('mov_details/<int:movie_id>/',views.manage_movie_detail,name='mov_detail'),
    path('seri_details/<int:serie_id>/',views.manage_serie_detail,name='seri_detail'),
    #  path('season_details/<int:season>/',views.manage_season_in_serie,name='season_detail'),
    path("Search_items",views.manage_search,name="search_items"),
    path("Search_serie_items",views.manage_serie_search,name="search_serie_items"),
    path('epis_details/<int:episode_id>/',views.manage_episode_detail,name='epis_detail'),
    path("English_series",views.get_english_series,name='english_series'),
    
    path('mov_sub_details/<int:movie_id>/',views.single_movie,name='mov_sub_detail'),
    path("Actions",views.get_action,name="actions"),
    path("Latest",views.get_latest,name="latest"),
    path("Horror",views.get_horror,name="horror"),
    path("Adventure",views.get_adventure,name="adventure"),
    path("Science_friction",views.get_sciefi,name="science_friction"),
    path("Action_comedy",views.get_action_comedy,name="action_comedy"),
    path("Romantic_action",views.get_romantic_action,name="romantic_action"),
    path("Action_detective",views.get_action_detective,name="action_detective"),
    path("Love_story",views.get_love_story,name="love_story"), 
    path("Romantic_comedy",views.get_romantic_comedy,name="romantic_comedy"),
    path("Other_Comedy",views.get_comedy,name="comedy"),
    path("Indian",views.get_indian,name="indian"), 
    path("Animitions",views.get_animitions,name="animitions"),
    path("Family_movies",views.get_family_movies,name="family_movies"),

    path("English",views.get_english,name="english"),
    path("Vj_junior",views.get_vj_junior,name="vj_junior"),
    path("Vj_emmy",views.get_vj_emmy,name="vj_emmy"),
    path("Vj_ice_p",views.get_vj_ice_p,name="vj_ice_p"),
    path("Vj_jingo",views.get_vj_jingo,name="vj_jingo"),
    path("Other_vjs",views.get_other_vjs,name="other_vjs"),

    path("signup", views.signup, name= "signup"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("Contact",views.contact_me,name="contact"),
    path("Sub_payment",views. Subscription_payment, name="sub_payment"), 
    path("Pay",views. payment, name="pay"),    
    
    path('download/<int:movie_id>/',views.download_movie, name='download_movie'),
    path('download/<int:episode_id>/',views.download_episode, name='download_episode'),
    path('Downloadapp',views.downloadapp, name='downloadapp'),


]
