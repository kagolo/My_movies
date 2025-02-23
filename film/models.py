from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User


# Create your models here.

class Register_users(models.Model):
    User_name=models.CharField(max_length=200,null=False)
    Email=models.EmailField()
    password=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)

class Movies(models.Model):
    movie_title=models.CharField(max_length=200,null=False)
    movie_actor=models.CharField(max_length=200,null=False)
    movie_director=models.CharField(max_length=200,null=False)
    CATEGORY_CHOICES=[
        ('SUPER ACTION','SUPER ACTION'),
        ('ACTION COMEDY','ACTION COMEDY'),
        ('ROMANTIC ACTION','ROMANTIC ACTION'),
        ('HORROR THRILLER','HORROR THRILLER'),
        ('SCIENCE FRICTION','SCIENCE FRICTION'),
        ('LOVE STORY','LOVE STORY'),
        ('INDIAN','INDIAN'),
        ('ACTION DETECTIVE','ACTION DETECTIVE'),
        ('COMEDY','COMEDY'),
        ('ROMANTIC COMEDY','ROMANTIC COMEDY'),
        ('ADVENTURE','ADVENTURE'),
        ('CARTOON','CARTOON'),
        ('FAMILY MOVIE','FAMILY MOVIE')
        
    ]
    movie_genre=models.CharField(max_length=300,null=False,choices=CATEGORY_CHOICES,default='ACTION')
    CATEGORY2_CHOICES=[
        ('VJ.JUNIOR','VJ.JUNIOR'),
        ('VJ.EMMY','VJ.EMMY'),
        ('VJ.ICE.P','VJ.ICE.P'),
        ('VJ.JINGO','VJ.JINGO'),
        ('ENGLISH','ENGLISH'),
        ('VJ.ULIO','VJ.ULIO'),
        ('VJ.MARK','VJ.MARK'),
        ('VJ.KEVO','VJ.KEVO'),
        ('VJ.MARTIN K','VJ.MARTIN K'),
        ('OTHER VJs','OTHER VJs'),
    ]
    movie_VJ=models.CharField(max_length=300,null=False,choices=CATEGORY2_CHOICES,default='VJ')
    movie_cost=models.CharField(max_length=300)
    STATUS1_TYPE_CHOICES=[
        ('New Movie','New Movie'),
        ('Featured','Featured')
    ]
    movie_status1=models.CharField(max_length=300,null=False,choices=STATUS1_TYPE_CHOICES,default='New')
    STATUS2_TYPE_CHOICES=[
        ('Free','Free'),
        ('Paid','Paid')
    ]
    movie_status2=models.CharField(max_length=200,choices=STATUS2_TYPE_CHOICES)
    movie_release_date=models.DateField(auto_now_add=True)
    movie_release_year=models.CharField(max_length=200,null=False)
    movie_image=models.ImageField(upload_to='pic')
    movie_video=models.FileField(upload_to='m_videos')
    file_size=models.CharField(max_length=200,null=True, blank=True)
    movie_description=models.CharField(max_length=3000,null=True, blank=True)

    def __str__(self):
        return self.movie_title

class Series(models.Model):
    serie_title=models.CharField(max_length=200,null=False)
    serie_actor=models.CharField(max_length=200,null=False)
    serie_director=models.CharField(max_length=200,null=False)
    serie_general=models.CharField(max_length=300,null=False)
    serie_VJ=models.CharField(max_length=200)
    serie_cost=models.CharField(max_length=200)
    # serie_cost=models.CharField(max_length=200, verbose_name="Omuwendo")

    STATUS0_TYPE_CHOICES=[
      
        ('ENGLISH SERIE','ENGLISH SERIE'),
        ('LUGANDA TRANSLATED SERIE','LUGANDA TRANSLATED SERIE')
    ]
    serie_translation_status=models.CharField(max_length=300,null=False,choices=STATUS0_TYPE_CHOICES)
  
    STATUS1_TYPE_CHOICES=[
      
        ('New','New'),
        ('Featured','Featured')
    ]
    serie_status1=models.CharField(max_length=300,null=False,choices=STATUS1_TYPE_CHOICES)
    
    STATUS2_TYPE_CHOICES=[
        ('Free','Free'),
        ('Paid','Paid')
    ]
    serie_status2=models.CharField(max_length=200,choices=STATUS2_TYPE_CHOICES)
    # serie_status2=models.CharField(max_length=200,choices=STATUS2_TYPE_CHOICES)
    serie_release_date=models.DateField(auto_now_add=True)
    serie_release_year=models.CharField(max_length=200,null=False)
    serie_image=models.ImageField(upload_to='pic')

    def __str__(self):
        return self.serie_title
    

class Season(models.Model):
    season_name=models.CharField(max_length=200)
    serie=models.ForeignKey(Series,on_delete=CASCADE)
    release_date=models.DateField()
    description=models.CharField(max_length=1000)

    def __str__(self):
        return self.season_name

class Episode(models.Model):
    episode_name=models.CharField(max_length=200)
    season=models.ForeignKey(Season,on_delete=CASCADE)
    release_date=models.DateField()
    description=models.CharField(max_length=2000,null=True, blank=True)
    file_size=models.CharField(max_length=200,null=True, blank=True)
    episode_video=models.FileField(upload_to='s_videos')

    def __str__(self):
        return self.episode_name


class Carousel(models.Model):
    image_name=models.CharField(max_length=200)
    carousel_image=models.ImageField(upload_to='c_pic')
    carousel_video=models.FileField(upload_to='c_videos')

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    
class Plan(models.Model):
    plan_name=models.CharField(max_length=200)
    plan_amount=models.CharField(max_length=100)

class Subscription(models.Model):
    movie=models.ForeignKey(Movies,on_delete=CASCADE)
    user=models.ForeignKey(User,on_delete=CASCADE)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    plan=models.ForeignKey(Plan,on_delete=CASCADE)
    STATUS_TYPE_CHOICES=[
        ('PAID','PAID'),
        ('FREE','FREE')
    ]
    subscription_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)    
    






    


