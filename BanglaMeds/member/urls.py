from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [

    path('signUp', views.signUp, name='signUp'),
    path('logIn', views.logIn, name='logIn'),
    path('logOut', views.logOut, name='logOut'),

    path('signUpConfirmation', views.signUpConfirmation, name='signUpConfirmation'),
    path('logInAttempt',views.logInAttempt, name='logInAttempt'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)