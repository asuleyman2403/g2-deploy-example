from user.views import login_page, register_page, logout_page, settings_page
from django.urls import path

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('register/', register_page, name='register_page'),
    path('settings/', settings_page, name='settings_page')
]
