from django.conf.urls import *
from . import views

app_name='calendarManager'

urlpatterns = [
    # urls for websites
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"roles", views.RolesPage.as_view(), name="roles"),
    url(r"goals", views.GoalsPage.as_view(), name="goals"),
    url(r"todos", views.TodosPage.as_view(), name="todos"),

    # urls for AJAX requests
    url(r"renderCalendar", views.renderCalendar, name="todos"),
]
