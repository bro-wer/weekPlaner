from django.conf.urls import *
from . import views
 
app_name='calendarManager'
 
urlpatterns = [
    # urls for websites
    url(r"^$", views.HomePage.as_view(), name="home"),
]
