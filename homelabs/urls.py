from django.urls import path
from . import views
app_name = "homelabs"
urlpatterns = [
    # homelabs views
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('guides/', views.guide_list, name='guide_list'),
    path('guides/view/<int:id>/', views.guide_view, name='guide_view'),
    path('guides/suggestion/', views.guide_suggestion, name='guide_suggestion'),

    path('guides/add/', views.guide_add, name='guide_add')

]