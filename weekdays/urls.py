from django.urls import path
from .import views

app_name = 'week'


urlpatterns = [
   
    # path('monday',views.monday),
    # path('tuesday',views.tuesday),
    # path('wednesday',views.wednesday),
    # path('<str:day>',views.daily_msg)
    # path('index',views.index),
    # path('hello',views.hello),
    path('',views.week_list,name='index'),
    path('<int:num>',views.display_num),
    path('<str:day>',views.display,name='home'),

  



]