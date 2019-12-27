from django.urls import path

#import app views
from basic_app import views

# TEMPLATE TAGGING

#TEMPLATE URLS!
app_name = 'basic_app'




urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
